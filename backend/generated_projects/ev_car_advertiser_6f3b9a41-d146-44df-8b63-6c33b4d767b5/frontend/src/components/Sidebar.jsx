import { Link } from 'react-router-dom';
import { Home, Truck, User, Plus, Pencil, Trash } from 'lucide-react';

function Sidebar() {
  return (
    <aside className="w-64 bg-gray-100 p-4 h-screen fixed top-0 left-0">
      <h2 className="text-lg font-bold mb-4">Menu</h2>
      <ul>
        <li className="mb-2">
          <Link to="/" className="flex items-center text-gray-600 hover:text-gray-900">
            <Home size={20} className="mr-2" />
            Home
          </Link>
        </li>
        <li className="mb-2">
          <Link to="/vehicles" className="flex items-center text-gray-600 hover:text-gray-900">
            <Truck size={20} className="mr-2" />
            Vehicles
          </Link>
        </li>
        <li className="mb-2">
          <Link to="/create-vehicle" className="flex items-center text-gray-600 hover:text-gray-900">
            <Plus size={20} className="mr-2" />
            Create Vehicle
          </Link>
        </li>
        <li className="mb-2">
          <Link to="/update-vehicle" className="flex items-center text-gray-600 hover:text-gray-900">
            <Pencil size={20} className="mr-2" />
            Update Vehicle
          </Link>
        </li>
        <li className="mb-2">
          <Link to="/delete-vehicle" className="flex items-center text-gray-600 hover:text-gray-900">
            <Trash size={20} className="mr-2" />
            Delete Vehicle
          </Link>
        </li>
        <li className="mb-2">
          <Link to="/users" className="flex items-center text-gray-600 hover:text-gray-900">
            <User size={20} className="mr-2" />
            Users
          </Link>
        </li>
        <li className="mb-2">
          <Link to="/create-user" className="flex items-center text-gray-600 hover:text-gray-900">
            <Plus size={20} className="mr-2" />
            Create User
          </Link>
        </li>
        <li className="mb-2">
          <Link to="/update-user" className="flex items-center text-gray-600 hover:text-gray-900">
            <Pencil size={20} className="mr-2" />
            Update User
          </Link>
        </li>
        <li className="mb-2">
          <Link to="/delete-user" className="flex items-center text-gray-600 hover:text-gray-900">
            <Trash size={20} className="mr-2" />
            Delete User
          </Link>
        </li>
      </ul>
    </aside>
  );
}

export default Sidebar;