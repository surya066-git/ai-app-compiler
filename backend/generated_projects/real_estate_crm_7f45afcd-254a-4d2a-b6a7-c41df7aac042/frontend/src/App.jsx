
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';

import Dashboard from './components/Dashboard.jsx';
import Leads from './components/Leads.jsx';
import Properties from './components/Properties.jsx';
import Agents from './components/Agents.jsx';
import Metrics from './components/Metrics.jsx';
import Reports from './components/Reports.jsx';

function App() {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <div className="flex flex-1 overflow-hidden">
        <Sidebar />
        <main className="flex-1 overflow-y-auto bg-gray-100 p-4">
          <Routes>
            <Route path='/' element={<Dashboard />} />
            <Route path='/dashboard' element={<Dashboard />} />
            <Route path='/leads' element={<Leads />} />
            <Route path='/properties' element={<Properties />} />
            <Route path='/agents' element={<Agents />} />
            <Route path='/metrics' element={<Metrics />} />
            <Route path='/reports' element={<Reports />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}

export default App;
