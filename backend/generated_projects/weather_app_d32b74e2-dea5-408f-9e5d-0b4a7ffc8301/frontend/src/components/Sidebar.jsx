// This JSX assumes the following imports are available in the scope where it is used:
// import { Link } from 'react-router-dom';
// import { CloudSun } from 'lucide-react';

<div className="flex flex-col h-screen p-4 bg-gray-900 text-white w-64 shadow-lg">
    {/* Sidebar Header/Logo */}
    <div className="flex items-center justify-center h-16 border-b border-gray-700 mb-6">
        <span className="text-2xl font-semibold text-indigo-400">My App</span>
    </div>

    {/* Navigation Links */}
    <nav className="flex-1 space-y-3">
        {/* Weather Display Link */}
        <Link
            to="/weather"
            className="flex items-center p-3 text-gray-300 hover:bg-gray-700 hover:text-white rounded-lg transition-colors duration-200 group"
        >
            {/* Lucide icon for Weather Display */}
            <CloudSun className="w-5 h-5 mr-3 text-indigo-300 group-hover:text-white transition-colors duration-200" />
            <span className="text-lg font-medium">Weather Display</span>
        </Link>
    </nav>

    {/* Optional: Footer or other elements */}
    <div className="mt-auto pt-4 border-t border-gray-700 text-sm text-gray-500 text-center">
        &copy; 2023 My App
    </div>
</div>