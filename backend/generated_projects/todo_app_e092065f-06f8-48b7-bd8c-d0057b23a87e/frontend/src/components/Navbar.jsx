import React from 'react';

const Navbar = () => {
  const handleLogout = () => {
    // Implement your logout logic here, e.g., clear token, redirect
    console.log('Logout clicked');
    alert('Logging out...'); // Placeholder for demonstration
  };

  return (
    <nav className="bg-gray-800 p-4">
      <div className="container mx-auto flex justify-between items-center">
        {/* Title Section */}
        <div className="text-white text-2xl font-bold">
          My App
        </div>

        {/* Logout Button Section */}
        <div>
          <button
            onClick={handleLogout}
            className="bg-red-600 hover:bg-red-700 text-white font-semibold py-2 px-4 rounded-md shadow-md transition duration-300 ease-in-out"
          >
            Logout
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;