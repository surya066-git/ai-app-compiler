import React from 'react';

function VehicleDashboard() {
  return (
    <div className="flex flex-col h-screen">
      <header className="bg-blue-500 text-white p-4">
        <h1 className="text-3xl font-bold">Vehicles Dashboard</h1>
      </header>
      <main className="flex-1 p-4">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Total Vehicles</h2>
            <p className="text-3xl font-bold">100</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Available Vehicles</h2>
            <p className="text-3xl font-bold">50</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Booked Vehicles</h2>
            <p className="text-3xl font-bold">30</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Maintenance Vehicles</h2>
            <p className="text-3xl font-bold">20</p>
          </div>
        </div>
        <div className="mt-4">
          <h2 className="text-lg font-bold">Vehicles Table</h2>
          <table className="w-full table-auto border border-gray-200">
            <thead className="bg-gray-100">
              <tr>
                <th className="px-4 py-2 border border-gray-200">ID</th>
                <th className="px-4 py-2 border border-gray-200">Type</th>
                <th className="px-4 py-2 border border-gray-200">Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="px-4 py-2 border border-gray-200">1</td>
                <td className="px-4 py-2 border border-gray-200">Car</td>
                <td className="px-4 py-2 border border-gray-200">Available</td>
              </tr>
              <tr>
                <td className="px-4 py-2 border border-gray-200">2</td>
                <td className="px-4 py-2 border border-gray-200">Truck</td>
                <td className="px-4 py-2 border border-gray-200">Booked</td>
              </tr>
              <tr>
                <td className="px-4 py-2 border border-gray-200">3</td>
                <td className="px-4 py-2 border border-gray-200">Motorcycle</td>
                <td className="px-4 py-2 border border-gray-200">Maintenance</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div className="mt-4">
          <h2 className="text-lg font-bold">Vehicles Chart</h2>
          <div className="bg-white p-4 rounded shadow h-64">
            {/* Chart placeholder */}
          </div>
        </div>
      </main>
    </div>
  );
}

export default VehicleDashboard;