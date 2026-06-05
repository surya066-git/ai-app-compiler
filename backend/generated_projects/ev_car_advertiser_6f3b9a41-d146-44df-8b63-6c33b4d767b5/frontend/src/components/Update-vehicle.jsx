import React from 'react';

function UpdateVehicleDashboard() {
  return (
    <div className="flex h-screen flex-col">
      <header className="bg-gray-900 text-white p-4">
        <h1 className="text-3xl font-bold">Update Vehicle Dashboard</h1>
      </header>
      <main className="flex-1 p-4">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Vehicle Information</h2>
            <ul>
              <li>Vehicle ID: <input type="text" className="border p-1" /></li>
              <li>Vehicle Type: <select className="border p-1">
                <option>Car</option>
                <option>Truck</option>
                <option>Motorcycle</option>
              </select></li>
              <li>License Plate: <input type="text" className="border p-1" /></li>
            </ul>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Vehicle Status</h2>
            <ul>
              <li>Status: <select className="border p-1">
                <option>Active</option>
                <option>Inactive</option>
              </select></li>
              <li>Last Updated: <input type="date" className="border p-1" /></li>
            </ul>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Update History</h2>
            <table className="w-full border-collapse">
              <thead>
                <tr>
                  <th className="border p-2">Date</th>
                  <th className="border p-2">Updated By</th>
                  <th className="border p-2">Changes</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td className="border p-2">2022-01-01</td>
                  <td className="border p-2">John Doe</td>
                  <td className="border p-2">Updated vehicle type</td>
                </tr>
                <tr>
                  <td className="border p-2">2022-01-15</td>
                  <td className="border p-2">Jane Doe</td>
                  <td className="border p-2">Updated license plate</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </main>
      <footer className="bg-gray-900 text-white p-4 text-center">
        <p>&copy; 2023 Update Vehicle Dashboard</p>
      </footer>
    </div>
  );
}

export default UpdateVehicleDashboard;