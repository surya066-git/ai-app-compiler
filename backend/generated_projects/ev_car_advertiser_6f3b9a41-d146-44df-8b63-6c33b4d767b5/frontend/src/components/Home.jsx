import React from 'react';

function HomeDashboard() {
  return (
    <div className="flex flex-col h-screen">
      <header className="bg-blue-500 text-white p-4 text-lg font-bold">
        Home Dashboard
      </header>
      <main className="flex-1 p-4">
        <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-4">
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold mb-2">Card 1</h2>
            <p className="text-gray-600">This is a sample card.</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold mb-2">Card 2</h2>
            <p className="text-gray-600">This is another sample card.</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold mb-2">Card 3</h2>
            <p className="text-gray-600">This is yet another sample card.</p>
          </div>
        </section>
        <section className="mb-4">
          <h2 className="text-lg font-bold mb-2">Table Placeholder</h2>
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
                  <td className="px-4 py-2 border-b border-gray-200">Cell 1</td>
                  <td className="px-4 py-2 border-b border-gray-200">Cell 2</td>
                  <td className="px-4 py-2 border-b border-gray-200">Cell 3</td>
                </tr>
                <tr>
                  <td className="px-4 py-2 border-b border-gray-200">Cell 4</td>
                  <td className="px-4 py-2 border-b border-gray-200">Cell 5</td>
                  <td className="px-4 py-2 border-b border-gray-200">Cell 6</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>
        <section>
          <h2 className="text-lg font-bold mb-2">Chart Placeholder</h2>
          <div className="bg-white p-4 rounded shadow h-64"></div>
        </section>
      </main>
    </div>
  );
}

export default HomeDashboard;