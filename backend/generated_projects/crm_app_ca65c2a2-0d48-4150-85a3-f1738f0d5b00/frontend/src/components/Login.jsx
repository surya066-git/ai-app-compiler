import React from 'react';

function LoginDashboard() {
  return (
    <div className="flex h-screen bg-gray-100">
      <div className="m-auto p-4 md:p-6 lg:p-8">
        <div className="flex flex-col md:flex-row justify-center items-center">
          <div className="w-full md:w-1/2 xl:w-1/3 p-6 bg-white rounded-lg shadow-md">
            <h2 className="text-3xl font-bold mb-4">Login</h2>
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
              <div className="flex items-center justify-between">
                <button
                  className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                  type="submit"
                >
                  Login
                </button>
                <a
                  className="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800"
                  href="#"
                >
                  Forgot Password?
                </a>
              </div>
            </form>
          </div>
          <div className="w-full md:w-1/2 xl:w-2/3 p-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="bg-white rounded-lg shadow-md p-4">
                <h3 className="text-xl font-bold mb-2">Card 1</h3>
                <p className="text-gray-600">This is a sample card.</p>
              </div>
              <div className="bg-white rounded-lg shadow-md p-4">
                <h3 className="text-xl font-bold mb-2">Card 2</h3>
                <p className="text-gray-600">This is another sample card.</p>
              </div>
            </div>
            <div className="mt-4">
              <h3 className="text-xl font-bold mb-2">Table Placeholder</h3>
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
                      <td className="px-4 py-2">Cell 1</td>
                      <td className="px-4 py-2">Cell 2</td>
                      <td className="px-4 py-2">Cell 3</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default LoginDashboard;