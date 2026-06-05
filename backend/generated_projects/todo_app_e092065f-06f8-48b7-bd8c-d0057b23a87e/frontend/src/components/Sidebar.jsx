import React from 'react';
import { Link } from 'react-router-dom';
import { Home, LogIn, UserPlus, ClipboardList, CirclePlus } from 'lucide-react';

const Sidebar = () => {
    const navLinks = [
        { name: 'Home Page', path: '/', icon: Home },
        { name: 'Login Page', path: '/login', icon: LogIn },
        { name: 'Register Page', path: '/register', icon: UserPlus },
        { name: 'Task List Page', path: '/tasks', icon: ClipboardList },
        { name: 'Add Task Page', path: '/add-task', icon: CirclePlus },
    ];

    return (
        <aside className="w-64 bg-gray-800 text-white h-screen flex flex-col p-4 shadow-lg">
            <div className="text-2xl font-semibold mb-8 text-gray-100">
                TaskFlow
            </div>
            <nav className="flex-1">
                <ul className="space-y-2">
                    {navLinks.map((link) => (
                        <li key={link.name}>
                            <Link
                                to={link.path}
                                className="flex items-center space-x-3 p-3 rounded-lg text-gray-300 hover:bg-gray-700 hover:text-white transition-colors duration-200"
                            >
                                <link.icon className="w-5 h-5" />
                                <span className="text-lg">{link.name}</span>
                            </Link>
                        </li>
                    ))}
                </ul>
            </nav>
            <div className="mt-auto pt-4 border-t border-gray-700 text-sm text-gray-500">
                &copy; {new Date().getFullYear()} TaskFlow
            </div>
        </aside>
    );
};

export default Sidebar;