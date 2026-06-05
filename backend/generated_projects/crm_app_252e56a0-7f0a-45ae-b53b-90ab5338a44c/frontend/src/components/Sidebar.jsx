import { Link } from 'react-router-dom';
import { Lock, Phone, Dashboard, ChartBar } from 'lucide-react';

function Sidebar() {
  return (
    <aside className="w-64 bg-gray-100 p-4 flex flex-col h-screen">
      <h2 className="text-lg font-bold mb-4">Menu</h2>
      <ul>
        <li className="mb-2">
          <Link to="/login" className="flex items-center text-gray-600 hover:text-gray-900">
            <Lock size={20} className="mr-2" />
            Login
          </Link>
        </li>
        <li className="mb-2">
          <Link to="/contacts" className="flex items-center text-gray-600 hover:text-gray-900">
            <Phone size={20} className="mr-2" />
            Contacts
          </Link>
        </li>
        <li className="mb-2">
          <Link to="/dashboard" className="flex items-center text-gray-600 hover:text-gray-900">
            <Dashboard size={20} className="mr-2" />
            Dashboard
          </Link>
        </li>
        <li className="mb-2">
          <Link to="/analytics" className="flex items-center text-gray-600 hover:text-gray-900">
            <ChartBar size={20} className="mr-2" />
            Analytics
          </Link>
        </li>
      </ul>
    </aside>
  );
}

export default Sidebar;