import React from 'react';

function Dashboard() {
  return (
    <div className="flex h-screen flex-col">
      <header className="bg-blue-500 text-white p-4 text-center">
        <h1 className="text-3xl font-bold">Dashboard</h1>
      </header>
      <main className="flex-1 p-4 overflow-y-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold mb-2">Card 1</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold mb-2">Card 2</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold mb-2">Card 3</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
          </div>
        </div>
        <div className="mt-4">
          <h2 className="text-lg font-bold mb-2">Table/Chart Placeholder</h2>
          <div className="bg-white p-4 rounded shadow">
            <table className="w-full table-auto">
              <thead className="bg-gray-100">
                <tr>
                  <th className="px-4 py-2">Column 1</th>
                  <th className="px-4 py-2">Column 2</th>
                  <th className="px-4 py-2">Column 3</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td className="px-4 py-2">Cell 1</td>
                  <td className="px-4 py-2">Cell 2</td>
                  <td className="px-4 py-2">Cell 3</td>
                </tr>
                <tr>
                  <td className="px-4 py-2">Cell 4</td>
                  <td className="px-4 py-2">Cell 5</td>
                  <td className="px-4 py-2">Cell 6</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </main>
    </div>
  );
}

export default Dashboard;