import json
import re
from typing import Dict, List

from llm.base_provider import BaseProvider


class LocalDeterministicProvider(BaseProvider):
    """Offline provider used for deterministic demos, tests, and quota fallback."""

    name = "local_deterministic"

    async def generate(self, system_prompt: str, user_prompt: str, response_format: str = "text") -> str:
        system_lower = system_prompt.lower()

        if "failed validation" in system_lower or "please fix the code" in system_lower:
            return user_prompt

        if response_format == "json":
            if "missing_details" in system_lower and "conflicts" in system_lower:
                return json.dumps(self._ambiguity_report(user_prompt))
            if "json list of string assumptions" in system_lower:
                return json.dumps(self._assumptions(user_prompt))
            if "appir" in system_lower or "json schema" in system_lower:
                return json.dumps(self._ir_for_prompt(user_prompt))
            if "database_tables" in system_lower and "features" in system_lower:
                return json.dumps(self._intent_for_prompt(user_prompt))
            return json.dumps({"message": "Generated locally", "prompt": user_prompt[:120]})

        if "sidebar component" in user_prompt.lower():
            return self._sidebar_component(user_prompt)
        if "navbar component" in user_prompt.lower():
            return self._navbar_component()
        if "sqlalchemy models.py" in system_lower:
            return self._models_for_prompt(user_prompt)
        if "react dashboard page" in user_prompt.lower():
            page = self._extract_page_name(user_prompt)
            return self._page_component(page)

        return "Generated deterministically by the local fallback provider."

    def _intent_for_prompt(self, prompt: str) -> Dict:
        tables = self._domain_tables(prompt)
        pages = ["Dashboard"] + [self._human_name(t) for t in tables if t != "users"][:5]
        return {
            "app_name": self._app_name(prompt),
            "features": self._features(prompt, tables),
            "database_tables": tables,
            "pages": pages,
        }

    def _ir_for_prompt(self, prompt: str) -> Dict:
        tables = self._domain_tables(prompt)
        pages = ["Dashboard"] + [self._component_name(self._human_name(t)) for t in tables if t != "users"][:5]
        endpoints = []
        for table in tables:
            plural = table.lower()
            endpoints.extend(
                [
                    {
                        "method": "GET",
                        "path": f"/api/{plural}",
                        "requires_auth": table != "users",
                        "description": f"List {self._human_name(table).lower()} records",
                    },
                    {
                        "method": "POST",
                        "path": f"/api/{plural}",
                        "requires_auth": table != "users",
                        "description": f"Create a {self._human_name(table).lower()} record",
                    },
                    {
                        "method": "GET",
                        "path": f"/api/{plural}/{{id}}",
                        "requires_auth": table != "users",
                        "description": f"Fetch one {self._human_name(table).lower()} record",
                    },
                ]
            )

        return {
            "app_name": self._app_name(prompt),
            "description": prompt.strip() or "Generated business application",
            "tables": [
                {
                    "name": table,
                    "fields": self._fields_for_table(table),
                }
                for table in tables
            ],
            "endpoints": endpoints,
            "pages": [
                {
                    "name": page,
                    "route": f"/{page.lower()}",
                    "description": f"{page} workspace",
                    "requires_auth": page != "Dashboard",
                }
                for page in pages
            ],
            "roles": ["admin", "user"],
            "assumptions": self._assumptions(prompt),
        }

    def _ambiguity_report(self, prompt: str) -> Dict:
        lower = prompt.lower()
        missing = []
        conflicts = []
        if len(prompt.split()) < 8 or any(word in lower for word in ["app.", "website for my business", "secure bank app"]):
            missing.extend(["target users", "core workflows", "data model"])
        if "without passwords" in lower and "passwords are required" in lower:
            conflicts.append("Authentication cannot both require and avoid passwords")
        if "no database" in lower and ("permanently" in lower or "stores" in lower):
            conflicts.append("Permanent storage requires a persistence layer")
        if "no data is ever sent to the server" in lower and "social network" in lower:
            conflicts.append("Social network collaboration requires server-side synchronization")
        return {
            "is_ambiguous": bool(missing or conflicts),
            "missing_details": missing,
            "conflicts": conflicts,
        }

    def _assumptions(self, prompt: str) -> List[str]:
        report = self._ambiguity_report(prompt)
        assumptions = [
            "JWT authentication is used for protected pages and APIs.",
            "SQLite is used for local runtime validation and PostgreSQL is configured for deployment.",
            "CRUD endpoints are generated for the primary domain tables.",
        ]
        if report["conflicts"]:
            assumptions.append("Conflicting requirements are resolved in favor of a runnable, secure baseline.")
        if report["missing_details"]:
            assumptions.append("Missing workflow details are filled with conservative dashboard-first defaults.")
        return assumptions

    def _domain_tables(self, prompt: str) -> List[str]:
        lower = prompt.lower()
        tables = ["users"]
        rules = [
            (["task", "todo", "project"], ["projects", "tasks"]),
            (["e-commerce", "ecommerce", "shop", "cart", "checkout", "product"], ["products", "carts", "orders", "payments"]),
            (["chat", "message", "room"], ["rooms", "messages"]),
            (["crm", "real estate", "lead", "property"], ["leads", "properties", "agents"]),
            (["blog", "markdown", "post", "tag"], ["posts", "categories", "tags"]),
            (["recipe", "meal"], ["recipes", "ratings", "meal_plans"]),
            (["inventory", "stock", "supplier", "barcode"], ["items", "suppliers", "stock_movements"]),
            (["fitness", "workout", "calorie"], ["workouts", "goals", "progress_entries"]),
            (["job", "candidate", "resume", "employer"], ["jobs", "applications", "employers", "candidates"]),
            (["finance", "bank", "budget", "expense"], ["accounts", "transactions", "budgets"]),
            (["health", "patient", "record"], ["patients", "records", "appointments"]),
            (["analytics", "dashboard", "metrics"], ["metrics", "reports"]),
            (["social", "facebook"], ["profiles", "posts", "messages"]),
            (["vehicle", "car", "ev"], ["vehicles", "campaigns", "leads"]),
            (["attendance", "student"], ["students", "attendance_records", "classes"]),
        ]
        for keywords, additions in rules:
            if any(keyword in lower for keyword in keywords):
                tables.extend(additions)
        if len(tables) == 1:
            tables.extend(["items", "activities"])
        return list(dict.fromkeys(tables))[:7]

    def _fields_for_table(self, table: str) -> List[Dict]:
        if table == "users":
            return [
                {"name": "id", "type": "Integer", "is_primary_key": True},
                {"name": "username", "type": "String"},
                {"name": "hashed_password", "type": "String"},
            ]
        return [
            {"name": "id", "type": "Integer", "is_primary_key": True},
            {"name": "name", "type": "String"},
            {"name": "status", "type": "String"},
            {"name": "description", "type": "String"},
        ]

    def _features(self, prompt: str, tables: List[str]) -> List[str]:
        features = ["Authentication", "Dashboard", "Validation", "ZIP export"]
        features.extend([f"{self._human_name(table)} management" for table in tables if table != "users"])
        if "real-time" in prompt.lower() or "chat" in prompt.lower():
            features.append("Realtime-ready messaging model")
        return features[:8]

    def _app_name(self, prompt: str) -> str:
        lower = prompt.lower()
        names = [
            ("task", "Task Management System"),
            ("todo", "Todo App"),
            ("e-commerce", "Digital Commerce Platform"),
            ("ecommerce", "Digital Commerce Platform"),
            ("chat", "Team Chat App"),
            ("crm", "Real Estate CRM"),
            ("blog", "Blog Engine"),
            ("recipe", "Recipe Sharing App"),
            ("inventory", "Inventory Manager"),
            ("fitness", "Fitness Tracker"),
            ("job", "Job Board"),
            ("finance", "Personal Finance Tracker"),
            ("bank", "Secure Banking Portal"),
            ("health", "Healthcare Portal"),
            ("analytics", "Analytics Dashboard"),
            ("social", "Social Network"),
            ("attendance", "Student Attendance Tracker"),
            ("vehicle", "EV Car Advertiser"),
        ]
        for keyword, name in names:
            if keyword in lower:
                return name
        return "Generated Application"

    def _human_name(self, value: str) -> str:
        return value.replace("_", " ").title()

    def _component_name(self, value: str) -> str:
        words = re.findall(r"[A-Za-z0-9]+", value)
        return "".join(word.capitalize() for word in words) or "Dashboard"

    def _extract_page_name(self, prompt: str) -> str:
        match = re.search(r"for '([^']+)'", prompt)
        if match:
            return self._component_name(match.group(1))
        return "Dashboard"

    def _sidebar_component(self, prompt: str) -> str:
        links_match = re.search(r"Links should be:\s*(.+?)\.", prompt, re.S)
        links = ["Dashboard"]
        if links_match:
            links = [self._component_name(item.strip()) for item in links_match.group(1).split(",") if item.strip()]
        link_markup = "\n".join(
            f"        <Link className=\"rounded-md px-3 py-2 text-sm font-medium text-slate-700 hover:bg-slate-100\" to=\"/{link.lower()}\">{self._human_name(link)}</Link>"
            for link in links
        )
        return f"""import React from 'react';
import {{ Link }} from 'react-router-dom';

export default function Sidebar() {{
  return (
    <aside className="w-60 shrink-0 border-r border-slate-200 bg-white p-4">
      <div className="mb-5 text-xs font-semibold uppercase tracking-wider text-slate-500">Workspace</div>
      <nav className="flex flex-col gap-1">
{link_markup}
      </nav>
    </aside>
  );
}}
"""

    def _navbar_component(self) -> str:
        return """import React from 'react';
import { ShieldCheck } from 'lucide-react';

export default function Navbar() {
  return (
    <nav className="flex h-14 items-center justify-between border-b border-slate-200 bg-white px-5">
      <div className="flex items-center gap-2 text-sm font-semibold text-slate-900">
        <ShieldCheck className="h-4 w-4 text-emerald-600" />
        Runtime Verified App
      </div>
      <button className="rounded-md border border-slate-300 px-3 py-1.5 text-sm text-slate-700 hover:bg-slate-50">Logout</button>
    </nav>
  );
}
"""

    def _page_component(self, page: str) -> str:
        title = self._human_name(page)
        return f"""import React from 'react';
import {{ Activity, CheckCircle2, Clock3 }} from 'lucide-react';

const rows = [
  {{ name: 'Primary workflow', status: 'Ready', owner: 'Operations' }},
  {{ name: 'Validation checks', status: 'Passing', owner: 'Compiler' }},
  {{ name: 'Deployment package', status: 'Prepared', owner: 'Runtime' }},
];

export default function {page}() {{
  return (
    <section className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold text-slate-950">{title}</h1>
        <p className="mt-1 text-sm text-slate-600">Operational view generated from the compiler IR.</p>
      </div>
      <div className="grid gap-4 md:grid-cols-3">
        <div className="rounded-lg border border-slate-200 bg-white p-4">
          <Activity className="mb-3 h-5 w-5 text-blue-600" />
          <p className="text-sm text-slate-500">Active records</p>
          <p className="mt-1 text-2xl font-semibold text-slate-950">24</p>
        </div>
        <div className="rounded-lg border border-slate-200 bg-white p-4">
          <CheckCircle2 className="mb-3 h-5 w-5 text-emerald-600" />
          <p className="text-sm text-slate-500">Healthy APIs</p>
          <p className="mt-1 text-2xl font-semibold text-slate-950">100%</p>
        </div>
        <div className="rounded-lg border border-slate-200 bg-white p-4">
          <Clock3 className="mb-3 h-5 w-5 text-amber-600" />
          <p className="text-sm text-slate-500">Runtime checks</p>
          <p className="mt-1 text-2xl font-semibold text-slate-950">Live</p>
        </div>
      </div>
      <div className="overflow-hidden rounded-lg border border-slate-200 bg-white">
        <table className="w-full text-left text-sm">
          <thead className="bg-slate-50 text-slate-500">
            <tr><th className="px-4 py-3">Workflow</th><th className="px-4 py-3">Status</th><th className="px-4 py-3">Owner</th></tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            {{rows.map((row) => (
              <tr key={{row.name}}>
                <td className="px-4 py-3 font-medium text-slate-900">{{row.name}}</td>
                <td className="px-4 py-3 text-emerald-700">{{row.status}}</td>
                <td className="px-4 py-3 text-slate-600">{{row.owner}}</td>
              </tr>
            ))}}
          </tbody>
        </table>
      </div>
    </section>
  );
}}
"""

    def _models_for_prompt(self, prompt: str) -> str:
        return "from sqlalchemy import Column, Integer, String\nfrom database import Base\n\nclass User(Base):\n    __tablename__ = 'users'\n    id = Column(Integer, primary_key=True, index=True)\n    username = Column(String, unique=True, index=True)\n    hashed_password = Column(String)\n"
