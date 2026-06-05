
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';

import Login from './components/Login.jsx';
import Contacts from './components/Contacts.jsx';
import Dashboard from './components/Dashboard.jsx';
import Premium from './components/Premium.jsx';

function App() {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <div className="flex flex-1 overflow-hidden">
        <Sidebar />
        <main className="flex-1 overflow-y-auto bg-gray-100 p-4">
          <Routes>
            <Route path='/' element={<Login />} />
            <Route path='/login' element={<Login />} />
            <Route path='/contacts' element={<Contacts />} />
            <Route path='/dashboard' element={<Dashboard />} />
            <Route path='/premium' element={<Premium />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}

export default App;
