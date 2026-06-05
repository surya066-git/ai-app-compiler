import React from 'react';

function ContactsDashboard() {
  return (
    <div className="flex h-screen flex-col">
      <header className="bg-blue-500 text-white p-4">
        <h1 className="text-3xl font-bold">Contacts Dashboard</h1>
      </header>
      <main className="flex-1 p-4">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Total Contacts</h2>
            <p className="text-3xl font-bold">100</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">New Contacts</h2>
            <p className="text-3xl font-bold">20</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Active Contacts</h2>
            <p className="text-3xl font-bold">50</p>
          </div>
        </div>
        <div className="mt-4">
          <h2 className="text-lg font-bold">Contacts Table</h2>
          <table className="w-full table-auto border-collapse border border-gray-200">
            <thead className="bg-gray-100">
              <tr>
                <th className="px-4 py-2 border border-gray-200">Name</th>
                <th className="px-4 py-2 border border-gray-200">Email</th>
                <th className="px-4 py-2 border border-gray-200">Phone</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="px-4 py-2 border border-gray-200">John Doe</td>
                <td className="px-4 py-2 border border-gray-200">john@example.com</td>
                <td className="px-4 py-2 border border-gray-200">123-456-7890</td>
              </tr>
              <tr>
                <td className="px-4 py-2 border border-gray-200">Jane Doe</td>
                <td className="px-4 py-2 border border-gray-200">jane@example.com</td>
                <td className="px-4 py-2 border border-gray-200">987-654-3210</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div className="mt-4">
          <h2 className="text-lg font-bold">Contacts Chart</h2>
          <div className="h-64 bg-white p-4 rounded shadow">
            {/* Chart placeholder */}
          </div>
        </div>
      </main>
    </div>
  );
}

export default ContactsDashboard;