import { Link } from 'react-router-dom';
import { Home, UserGroup, Clipboard } from 'lucide-react';

function Sidebar() {
  return (
    <aside className="w-64 bg-gray-100 p-4 h-screen fixed top-0 left-0">
      <ul>
        <li className="mb-4">
          <Link to="/dashboard" className="flex items-center text-gray-600 hover:text-gray-900">
            <Home size={20} className="mr-2" />
            Dashboard
          </Link>
        </li>
        <li className="mb-4">
          <Link to="/students" className="flex items-center text-gray-600 hover:text-gray-900">
            <UserGroup size={20} className="mr-2" />
            Students
          </Link>
        </li>
        <li className="mb-4">
          <Link to="/attendance" className="flex items-center text-gray-600 hover:text-gray-900">
            <Clipboard size={20} className="mr-2" />
            Attendance
          </Link>
        </li>
      </ul>
    </aside>
  );
}

export default Sidebar;