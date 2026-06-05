import React from 'react';

function DeleteUserDashboard() {
  return (
    <div className="flex h-screen bg-gray-100">
      <div className="w-full p-4 md:p-6 lg:p-8">
        <h1 className="text-3xl font-bold mb-4">Delete User Dashboard</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-8">
          <div className="bg-white p-4 rounded-lg shadow-md">
            <h2 className="text-xl font-bold mb-2">Total Users</h2>
            <p className="text-3xl font-bold">1000</p>
          </div>
          <div className="bg-white p-4 rounded-lg shadow-md">
            <h2 className="text-xl font-bold mb-2">Active Users</h2>
            <p className="text-3xl font-bold">500</p>
          </div>
          <div className="bg-white p-4 rounded-lg shadow-md">
            <h2 className="text-xl font-bold mb-2">Deleted Users</h2>
            <p className="text-3xl font-bold">200</p>
          </div>
        </div>
        <div className="bg-white p-4 rounded-lg shadow-md mb-8">
          <h2 className="text-xl font-bold mb-4">User Table</h2>
          <table className="w-full table-auto">
            <thead className="bg-gray-100">
              <tr>
                <th className="px-4 py-2">ID</th>
                <th className="px-4 py-2">Name</th>
                <th className="px-4 py-2">Email</th>
                <th className="px-4 py-2">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="px-4 py-2">1</td>
                <td className="px-4 py-2">John Doe</td>
                <td className="px-4 py-2">john@example.com</td>
                <td className="px-4 py-2">
                  <button className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
                    Delete
                  </button>
                </td>
              </tr>
              <tr>
                <td className="px-4 py-2">2</td>
                <td className="px-4 py-2">Jane Doe</td>
                <td className="px-4 py-2">jane@example.com</td>
                <td className="px-4 py-2">
                  <button className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
                    Delete
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div className="bg-white p-4 rounded-lg shadow-md">
          <h2 className="text-xl font-bold mb-4">User Chart</h2>
          <div className="h-64 w-full bg-gray-200 rounded-lg"></div>
        </div>
      </div>
    </div>
  );
}

export default DeleteUserDashboard;