
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';

import WeatherDisplay from './components/WeatherDisplay';

function App() {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <div className="flex flex-1 overflow-hidden">
        <Sidebar />
        <main className="flex-1 overflow-y-auto bg-gray-100 p-4">
          <Routes>
            <Route path='/weatherdisplay' element={<WeatherDisplay />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}

export default App;
