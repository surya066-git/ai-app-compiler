import React from 'react';

function LoginDashboard() {
  return (
    <div className="h-screen bg-gray-100 flex justify-center items-center">
      <div className="max-w-5xl mx-auto p-4 md:p-6 lg:p-8 bg-white rounded-lg shadow-md">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-2xl font-bold">Login Dashboard</h2>
          <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            Login
          </button>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-4">
          <div className="bg-white rounded-lg shadow-md p-4">
            <h3 className="text-lg font-bold mb-2">Card 1</h3>
            <p className="text-gray-600">This is a sample card.</p>
          </div>
          <div className="bg-white rounded-lg shadow-md p-4">
            <h3 className="text-lg font-bold mb-2">Card 2</h3>
            <p className="text-gray-600">This is another sample card.</p>
          </div>
          <div className="bg-white rounded-lg shadow-md p-4">
            <h3 className="text-lg font-bold mb-2">Card 3</h3>
            <p className="text-gray-600">This is yet another sample card.</p>
          </div>
        </div>
        <div className="bg-white rounded-lg shadow-md p-4 mb-4">
          <h2 className="text-lg font-bold mb-2">Table Placeholder</h2>
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
        <div className="bg-white rounded-lg shadow-md p-4">
          <h2 className="text-lg font-bold mb-2">Chart Placeholder</h2>
          <div className="h-64 bg-gray-200 rounded-lg"></div>
        </div>
      </div>
    </div>
  );
}

export default LoginDashboard;