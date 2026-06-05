import React from 'react';

function LoginPage() {
  return (
    <div className="flex h-screen justify-center items-center bg-gray-100">
      <div className="max-w-5xl mx-auto p-4 md:p-6 lg:p-8 bg-white rounded-lg shadow-md">
        <div className="flex flex-col md:flex-row justify-center items-center mb-4">
          <h1 className="text-3xl font-bold text-gray-700 mb-4 md:mb-0">Login Page</h1>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-4">
          <div className="bg-blue-500 p-4 rounded-lg shadow-md text-white">
            <h2 className="text-2xl font-bold mb-2">Card 1</h2>
            <p className="text-lg">This is a sample card.</p>
          </div>
          <div className="bg-green-500 p-4 rounded-lg shadow-md text-white">
            <h2 className="text-2xl font-bold mb-2">Card 2</h2>
            <p className="text-lg">This is another sample card.</p>
          </div>
          <div className="bg-yellow-500 p-4 rounded-lg shadow-md text-white">
            <h2 className="text-2xl font-bold mb-2">Card 3</h2>
            <p className="text-lg">This is a third sample card.</p>
          </div>
        </div>
        <div className="overflow-x-auto mb-4">
          <table className="w-full table-auto border-collapse border border-gray-400">
            <thead className="bg-gray-100">
              <tr>
                <th className="px-4 py-2 border border-gray-400">Column 1</th>
                <th className="px-4 py-2 border border-gray-400">Column 2</th>
                <th className="px-4 py-2 border border-gray-400">Column 3</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="px-4 py-2 border border-gray-400">Cell 1</td>
                <td className="px-4 py-2 border border-gray-400">Cell 2</td>
                <td className="px-4 py-2 border border-gray-400">Cell 3</td>
              </tr>
              <tr>
                <td className="px-4 py-2 border border-gray-400">Cell 4</td>
                <td className="px-4 py-2 border border-gray-400">Cell 5</td>
                <td className="px-4 py-2 border border-gray-400">Cell 6</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div className="h-64 bg-gray-200 rounded-lg shadow-md mb-4"></div>
        <form className="flex flex-col justify-center items-center">
          <input type="email" placeholder="Email" className="w-full md:w-1/2 lg:w-1/3 p-4 mb-4 border border-gray-400 rounded-lg" />
          <input type="password" placeholder="Password" className="w-full md:w-1/2 lg:w-1/3 p-4 mb-4 border border-gray-400 rounded-lg" />
          <button className="w-full md:w-1/2 lg:w-1/3 p-4 bg-blue-500 text-white rounded-lg hover:bg-blue-700">Login</button>
        </form>
      </div>
    </div>
  );
}

export default LoginPage;