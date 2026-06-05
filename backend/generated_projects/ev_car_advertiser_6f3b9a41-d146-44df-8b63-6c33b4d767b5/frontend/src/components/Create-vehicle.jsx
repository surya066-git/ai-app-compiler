import React from 'react';

function CreateVehicleDashboard() {
  return (
    <div className="flex h-screen bg-gray-100">
      <div className="w-full p-4 md:p-6 lg:p-8">
        <h1 className="text-3xl font-bold mb-4">Create Vehicle</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div className="bg-white p-4 rounded shadow-md">
            <h2 className="text-xl font-bold mb-2">Vehicle Information</h2>
            <form>
              <div className="mb-4">
                <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="vehicleName">
                  Vehicle Name
                </label>
                <input
                  className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  id="vehicleName"
                  type="text"
                  placeholder="Enter vehicle name"
                />
              </div>
              <div className="mb-4">
                <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="vehicleType">
                  Vehicle Type
                </label>
                <select
                  className="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                  id="vehicleType"
                >
                  <option>Car</option>
                  <option>Truck</option>
                  <option>Motorcycle</option>
                </select>
              </div>
              <button
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                type="submit"
              >
                Create Vehicle
              </button>
            </form>
          </div>
          <div className="bg-white p-4 rounded shadow-md">
            <h2 className="text-xl font-bold mb-2">Vehicle Specifications</h2>
            <table className="w-full table-auto">
              <thead className="bg-gray-100">
                <tr>
                  <th className="px-4 py-2">Specification</th>
                  <th className="px-4 py-2">Value</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td className="px-4 py-2 border">Engine Type</td>
                  <td className="px-4 py-2 border">Gasoline</td>
                </tr>
                <tr>
                  <td className="px-4 py-2 border">Transmission</td>
                  <td className="px-4 py-2 border">Automatic</td>
                </tr>
                <tr>
                  <td className="px-4 py-2 border">Fuel Capacity</td>
                  <td className="px-4 py-2 border">15 gallons</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div className="bg-white p-4 rounded shadow-md">
            <h2 className="text-xl font-bold mb-2">Vehicle Chart</h2>
            <div className="h-64">
              {/* Chart placeholder */}
              <svg
                className="w-full h-full"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 400 200"
              >
                <rect x="50" y="50" width="300" height="100" fill="#ccc" />
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default CreateVehicleDashboard;