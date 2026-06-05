import React from 'react';
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