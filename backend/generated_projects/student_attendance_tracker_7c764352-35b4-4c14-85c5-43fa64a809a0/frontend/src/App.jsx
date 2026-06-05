
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';

import Dashboard from './components/Dashboard';\nimport Students from './components/Students';\nimport Attendance from './components/Attendance';

function App() {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <div className="flex flex-1 overflow-hidden">
        <Sidebar />
        <main className="flex-1 overflow-y-auto bg-gray-100 p-4">
          <Routes>
            <Route path='/dashboard' element={<Dashboard />} />\n            <Route path='/students' element={<Students />} />\n            <Route path='/attendance' element={<Attendance />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}

export default App;
