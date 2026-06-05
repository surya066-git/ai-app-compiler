import React from 'react';
import { Link } from 'react-router-dom';
import { Home, CloudSun } from 'lucide-react';

const Sidebar = () => {
  return (
    <div className="flex flex-col h-screen w-64 bg-gray-800 text-white p-4 shadow-lg fixed left-0 top-0 z-50">
      <div className="text-2xl font-semibold mb-6 text-gray-100 border-b border-gray-700 pb-4">
        Weather App
      </div>
      <nav>
        <ul className="space-y-3">
          <li>
            <Link
              to="/"
              className="flex items-center p-3 rounded-lg text-gray-300 hover:bg-gray-700 hover:text-white transition-colors duration-200 group"
            >
              <Home className="mr-3 h-5 w-5 text-gray-400 group-hover:text-white transition-colors duration-200" />
              Home
            </Link>
          </li>
          <li>
            <Link
              to="/city-weather"
              className="flex items-center p-3 rounded-lg text-gray-300 hover:bg-gray-700 hover:text-white transition-colors duration-200 group"
            >
              <CloudSun className="mr-3 h-5 w-5 text-gray-400 group-hover:text-white transition-colors duration-200" />
              City Weather Detail
            </Link>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Sidebar;