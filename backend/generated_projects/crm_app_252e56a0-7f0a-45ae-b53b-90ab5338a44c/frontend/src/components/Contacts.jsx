import React from 'react';

function ContactsDashboard() {
  return (
    <div className="flex h-screen flex-col">
      <header className="bg-blue-500 text-white p-4 text-lg font-bold">
        Contacts Dashboard
      </header>
      <main className="flex-1 p-4 overflow-y-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold mb-2">Total Contacts</h2>
            <p className="text-3xl font-bold">100</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold mb-2">New Contacts</h2>
            <p className="text-3xl font-bold">20</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold mb-2">Active Contacts</h2>
            <p className="text-3xl font-bold">50</p>
          </div>
        </div>
        <div className="mt-4">
          <h2 className="text-lg font-bold mb-2">Contacts Table</h2>
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
          <h2 className="text-lg font-bold mb-2">Contacts Chart</h2>
          <div className="bg-white p-4 rounded shadow h-64"></div>
        </div>
      </main>
    </div>
  );
}

export default ContactsDashboard;