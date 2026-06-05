
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';

import home from './components/home';\nimport vehicles from './components/vehicles';\nimport create-vehicle from './components/create-vehicle';\nimport update-vehicle from './components/update-vehicle';\nimport delete-vehicle from './components/delete-vehicle';\nimport users from './components/users';\nimport create-user from './components/create-user';\nimport update-user from './components/update-user';\nimport delete-user from './components/delete-user';

function App() {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <div className="flex flex-1 overflow-hidden">
        <Sidebar />
        <main className="flex-1 overflow-y-auto bg-gray-100 p-4">
          <Routes>
            <Route path='/home' element={<home />} />\n            <Route path='/vehicles' element={<vehicles />} />\n            <Route path='/create-vehicle' element={<create-vehicle />} />\n            <Route path='/update-vehicle' element={<update-vehicle />} />\n            <Route path='/delete-vehicle' element={<delete-vehicle />} />\n            <Route path='/users' element={<users />} />\n            <Route path='/create-user' element={<create-user />} />\n            <Route path='/update-user' element={<update-user />} />\n            <Route path='/delete-user' element={<delete-user />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}

export default App;
