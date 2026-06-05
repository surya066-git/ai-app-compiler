import React from 'react';
import { Activity, CheckCircle2, Clock3 } from 'lucide-react';

const rows = [
  { name: 'Primary workflow', status: 'Ready', owner: 'Operations' },
  { name: 'Validation checks', status: 'Passing', owner: 'Compiler' },
  { name: 'Deployment package', status: 'Prepared', owner: 'Runtime' },
];

export default function Metrics() {
  return (
    <section className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold text-slate-950">Metrics</h1>
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
            {rows.map((row) => (
              <tr key={row.name}>
                <td className="px-4 py-3 font-medium text-slate-900">{row.name}</td>
                <td className="px-4 py-3 text-emerald-700">{row.status}</td>
                <td className="px-4 py-3 text-slate-600">{row.owner}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}