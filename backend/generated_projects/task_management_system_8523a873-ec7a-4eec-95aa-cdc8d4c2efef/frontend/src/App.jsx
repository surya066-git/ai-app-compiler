
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';

import Dashboard from './components/Dashboard.jsx';
import Projects from './components/Projects.jsx';
import Tasks from './components/Tasks.jsx';

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
            <Route path='/projects' element={<Projects />} />
            <Route path='/tasks' element={<Tasks />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}

export default App;
