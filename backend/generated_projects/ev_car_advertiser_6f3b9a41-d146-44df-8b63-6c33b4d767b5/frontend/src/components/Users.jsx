import React from 'react';

function UsersDashboard() {
  return (
    <div className="flex h-screen flex-col">
      <header className="bg-blue-500 text-white p-4">
        <h1 className="text-3xl font-bold">Users Dashboard</h1>
      </header>
      <main className="flex-1 p-4">
        <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Total Users</h2>
            <p className="text-3xl font-bold">1000</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Active Users</h2>
            <p className="text-3xl font-bold">500</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">New Users</h2>
            <p className="text-3xl font-bold">200</p>
          </div>
        </div>
        <div className="mt-4">
          <h2 className="text-lg font-bold">Users Table</h2>
          <table className="w-full table-auto border border-gray-200">
            <thead className="bg-gray-100">
              <tr>
                <th className="px-4 py-2">ID</th>
                <th className="px-4 py-2">Name</th>
                <th className="px-4 py-2">Email</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="px-4 py-2 border-b border-gray-200">1</td>
                <td className="px-4 py-2 border-b border-gray-200">John Doe</td>
                <td className="px-4 py-2 border-b border-gray-200">john@example.com</td>
              </tr>
              <tr>
                <td className="px-4 py-2 border-b border-gray-200">2</td>
                <td className="px-4 py-2 border-b border-gray-200">Jane Doe</td>
                <td className="px-4 py-2 border-b border-gray-200">jane@example.com</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div className="mt-4">
          <h2 className="text-lg font-bold">Users Chart</h2>
          <div className="h-64 bg-white p-4 rounded shadow">
            {/* Chart placeholder */}
          </div>
        </div>
      </main>
    </div>
  );
}

export default UsersDashboard;