import React from 'react';

const Navbar = () => {
  const handleLogout = () => {
    // Add logout logic here
  };

  return (
    <nav className="flex justify-between items-center py-4 bg-gray-800 text-white">
      <h1 className="text-2xl font-bold ml-4">My App</h1>
      <button
        className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded mr-4"
        onClick={handleLogout}
      >
        Logout
      </button>
    </nav>
  );
};

export default Navbar;