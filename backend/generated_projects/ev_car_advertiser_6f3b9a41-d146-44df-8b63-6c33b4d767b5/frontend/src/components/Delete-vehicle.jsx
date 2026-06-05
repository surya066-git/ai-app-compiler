import React from 'react';

function DeleteVehicleDashboard() {
  return (
    <div className="flex h-screen bg-gray-100">
      <div className="w-full max-w-md mx-auto p-4 md:p-6 lg:p-8 bg-white rounded shadow-md">
        <h2 className="mb-4 text-2xl font-bold text-gray-600">Delete Vehicle</h2>
        <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
          <div className="bg-white rounded shadow-md p-4">
            <h3 className="mb-2 text-lg font-bold text-gray-600">Total Vehicles</h3>
            <p className="text-2xl font-bold text-gray-900">100</p>
          </div>
          <div className="bg-white rounded shadow-md p-4">
            <h3 className="mb-2 text-lg font-bold text-gray-600">Deleted Vehicles</h3>
            <p className="text-2xl font-bold text-gray-900">20</p>
          </div>
          <div className="bg-white rounded shadow-md p-4">
            <h3 className="mb-2 text-lg font-bold text-gray-600">Available Vehicles</h3>
            <p className="text-2xl font-bold text-gray-900">80</p>
          </div>
        </div>
        <div className="mt-8">
          <h2 className="mb-4 text-2xl font-bold text-gray-600">Vehicles Table</h2>
          <div className="overflow-x-auto">
            <table className="w-full table-auto">
              <thead className="bg-gray-100">
                <tr>
                  <th className="px-4 py-2 text-lg font-bold text-gray-600">ID</th>
                  <th className="px-4 py-2 text-lg font-bold text-gray-600">Vehicle Name</th>
                  <th className="px-4 py-2 text-lg font-bold text-gray-600">Delete</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td className="px-4 py-2 text-lg text-gray-900">1</td>
                  <td className="px-4 py-2 text-lg text-gray-900">Vehicle 1</td>
                  <td className="px-4 py-2 text-lg text-gray-900">
                    <button className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
                      Delete
                    </button>
                  </td>
                </tr>
                <tr>
                  <td className="px-4 py-2 text-lg text-gray-900">2</td>
                  <td className="px-4 py-2 text-lg text-gray-900">Vehicle 2</td>
                  <td className="px-4 py-2 text-lg text-gray-900">
                    <button className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
                      Delete
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}

export default DeleteVehicleDashboard;