
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';

import Dashboard from './components/Dashboard.jsx';
import Products from './components/Products.jsx';
import Carts from './components/Carts.jsx';
import Orders from './components/Orders.jsx';
import Payments from './components/Payments.jsx';
import Vehicles from './components/Vehicles.jsx';

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
            <Route path='/products' element={<Products />} />
            <Route path='/carts' element={<Carts />} />
            <Route path='/orders' element={<Orders />} />
            <Route path='/payments' element={<Payments />} />
            <Route path='/vehicles' element={<Vehicles />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}

export default App;
