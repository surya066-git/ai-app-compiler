import React from 'react';

function UpdateUserDashboard() {
  return (
    <div className="flex h-screen bg-gray-100">
      <div className="w-full p-4 md:p-6 lg:p-8">
        <h1 className="text-3xl font-bold mb-4">Update User Dashboard</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-8">
          <div className="bg-white p-4 rounded-lg shadow-md">
            <h2 className="text-lg font-bold mb-2">Total Users</h2>
            <p className="text-2xl font-bold">1000</p>
          </div>
          <div className="bg-white p-4 rounded-lg shadow-md">
            <h2 className="text-lg font-bold mb-2">Active Users</h2>
            <p className="text-2xl font-bold">500</p>
          </div>
          <div className="bg-white p-4 rounded-lg shadow-md">
            <h2 className="text-lg font-bold mb-2">Inactive Users</h2>
            <p className="text-2xl font-bold">500</p>
          </div>
        </div>
        <div className="bg-white p-4 rounded-lg shadow-md mb-8">
          <h2 className="text-lg font-bold mb-4">User Update Form</h2>
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
              <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="email">
                Email
              </label>
              <input
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="email"
                type="email"
                placeholder="Email"
              />
            </div>
            <button
              className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              type="submit"
            >
              Update User
            </button>
          </form>
        </div>
        <div className="bg-white p-4 rounded-lg shadow-md">
          <h2 className="text-lg font-bold mb-4">User Data</h2>
          <table className="w-full table-auto">
            <thead className="bg-gray-100">
              <tr>
                <th className="px-4 py-2">ID</th>
                <th className="px-4 py-2">Username</th>
                <th className="px-4 py-2">Email</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="px-4 py-2">1</td>
                <td className="px-4 py-2">johnDoe</td>
                <td className="px-4 py-2">johndoe@example.com</td>
              </tr>
              <tr>
                <td className="px-4 py-2">2</td>
                <td className="px-4 py-2">janeDoe</td>
                <td className="px-4 py-2">janedoe@example.com</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default UpdateUserDashboard;