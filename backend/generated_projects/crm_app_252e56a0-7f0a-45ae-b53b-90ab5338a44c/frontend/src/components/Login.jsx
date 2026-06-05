import React from 'react';

function LoginDashboard() {
  return (
    <div className="flex h-screen bg-gray-100">
      <div className="m-auto p-4 w-full max-w-md bg-white rounded-lg shadow-md">
        <h2 className="text-3xl font-bold mb-4">Login Dashboard</h2>
        <form>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="username">
              Username
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="username"
              type="text"
              placeholder="Username"
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="password">
              Password
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="password"
              type="password"
              placeholder="Password"
            />
          </div>
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="submit"
          >
            Login
          </button>
        </form>
        <div className="mt-4">
          <h3 className="text-2xl font-bold mb-4">Generic Cards</h3>
          <div className="flex flex-wrap -mx-4">
            <div className="w-full md:w-1/2 xl:w-1/3 p-4">
              <div className="bg-white rounded-lg shadow-md p-4">
                <h4 className="text-xl font-bold mb-2">Card 1</h4>
                <p className="text-gray-700">This is a generic card.</p>
              </div>
            </div>
            <div className="w-full md:w-1/2 xl:w-1/3 p-4">
              <div className="bg-white rounded-lg shadow-md p-4">
                <h4 className="text-xl font-bold mb-2">Card 2</h4>
                <p className="text-gray-700">This is another generic card.</p>
              </div>
            </div>
            <div className="w-full md:w-1/2 xl:w-1/3 p-4">
              <div className="bg-white rounded-lg shadow-md p-4">
                <h4 className="text-xl font-bold mb-2">Card 3</h4>
                <p className="text-gray-700">This is yet another generic card.</p>
              </div>
            </div>
          </div>
        </div>
        <div className="mt-4">
          <h3 className="text-2xl font-bold mb-4">Table Placeholder</h3>
          <div className="overflow-x-auto">
            <table className="table-auto w-full">
              <thead className="bg-gray-100">
                <tr>
                  <th className="px-4 py-2">Column 1</th>
                  <th className="px-4 py-2">Column 2</th>
                  <th className="px-4 py-2">Column 3</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td className="border px-4 py-2">Cell 1</td>
                  <td className="border px-4 py-2">Cell 2</td>
                  <td className="border px-4 py-2">Cell 3</td>
                </tr>
                <tr>
                  <td className="border px-4 py-2">Cell 4</td>
                  <td className="border px-4 py-2">Cell 5</td>
                  <td className="border px-4 py-2">Cell 6</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div className="mt-4">
          <h3 className="text-2xl font-bold mb-4">Chart Placeholder</h3>
          <div className="h-64 bg-gray-200 rounded-lg shadow-md"></div>
        </div>
      </div>
    </div>
  );
}

export default LoginDashboard;