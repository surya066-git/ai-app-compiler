import React from 'react';
import { Link } from 'react-router-dom';

export default function Sidebar() {
  return (
    <aside className="w-60 shrink-0 border-r border-slate-200 bg-white p-4">
      <div className="mb-5 text-xs font-semibold uppercase tracking-wider text-slate-500">Workspace</div>
      <nav className="flex flex-col gap-1">
        <Link className="rounded-md px-3 py-2 text-sm font-medium text-slate-700 hover:bg-slate-100" to="/dashboard">Dashboard</Link>
        <Link className="rounded-md px-3 py-2 text-sm font-medium text-slate-700 hover:bg-slate-100" to="/products">Products</Link>
        <Link className="rounded-md px-3 py-2 text-sm font-medium text-slate-700 hover:bg-slate-100" to="/carts">Carts</Link>
        <Link className="rounded-md px-3 py-2 text-sm font-medium text-slate-700 hover:bg-slate-100" to="/orders">Orders</Link>
        <Link className="rounded-md px-3 py-2 text-sm font-medium text-slate-700 hover:bg-slate-100" to="/payments">Payments</Link>
        <Link className="rounded-md px-3 py-2 text-sm font-medium text-slate-700 hover:bg-slate-100" to="/vehicles">Vehicles</Link>
      </nav>
    </aside>
  );
}