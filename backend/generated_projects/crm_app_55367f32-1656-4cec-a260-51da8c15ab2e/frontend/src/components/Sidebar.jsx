import { Link } from 'react-router-dom';
import { ArrowRight } from 'lucide-react';

function Sidebar() {
  return (
    <aside className="w-64 bg-gray-100 p-4 flex-shrink-0">
      <nav>
        <ul>
          <li className="mb-4">
            <Link
              to="/login"
              className="flex items-center text-gray-600 hover:text-gray-900"
            >
              <ArrowRight className="mr-2" size={20} />
              Login
            </Link>
          </li>
          <li className="mb-4">
            <Link
              to="/contacts"
              className="flex items-center text-gray-600 hover:text-gray-900"
            >
              <ArrowRight className="mr-2" size={20} />
              Contacts
            </Link>
          </li>
          <li className="mb-4">
            <Link
              to="/dashboard"
              className="flex items-center text-gray-600 hover:text-gray-900"
            >
              <ArrowRight className="mr-2" size={20} />
              Dashboard
            </Link>
          </li>
          <li className="mb-4">
            <Link
              to="/premium"
              className="flex items-center text-gray-600 hover:text-gray-900"
            >
              <ArrowRight className="mr-2" size={20} />
              Premium
            </Link>
          </li>
        </ul>
      </nav>
    </aside>
  );
}

export default Sidebar;