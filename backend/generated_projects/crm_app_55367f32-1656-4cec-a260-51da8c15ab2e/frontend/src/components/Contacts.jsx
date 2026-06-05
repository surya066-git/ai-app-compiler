import React from 'react';

function ContactsDashboard() {
  return (
    <div className="flex h-screen flex-col">
      <header className="bg-gray-900 text-white p-4">
        <h1 className="text-3xl font-bold">Contacts Dashboard</h1>
      </header>
      <main className="flex-1 p-4">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Total Contacts</h2>
            <p className="text-3xl font-bold">1000</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">New Contacts</h2>
            <p className="text-3xl font-bold">50</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Active Contacts</h2>
            <p className="text-3xl font-bold">800</p>
          </div>
        </div>
        <div className="mt-4">
          <h2 className="text-lg font-bold">Contacts Table</h2>
          <div className="bg-white p-4 rounded shadow">
            <table className="w-full table-auto">
              <thead className="bg-gray-100">
                <tr>
                  <th className="px-4 py-2">Name</th>
                  <th className="px-4 py-2">Email</th>
                  <th className="px-4 py-2">Phone</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td className="px-4 py-2">John Doe</td>
                  <td className="px-4 py-2">john@example.com</td>
                  <td className="px-4 py-2">123-456-7890</td>
                </tr>
                <tr>
                  <td className="px-4 py-2">Jane Doe</td>
                  <td className="px-4 py-2">jane@example.com</td>
                  <td className="px-4 py-2">987-654-3210</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div className="mt-4">
          <h2 className="text-lg font-bold">Contacts Chart</h2>
          <div className="bg-white p-4 rounded shadow h-64">
            {/* Chart placeholder */}
          </div>
        </div>
      </main>
    </div>
  );
}

export default ContactsDashboard;