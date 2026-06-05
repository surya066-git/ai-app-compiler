import React from 'react';

function Tasklistpage() {
  return (
    <div className="flex h-screen flex-col">
      <header className="bg-blue-500 text-white p-4 text-center">
        <h1 className="text-3xl font-bold">Task List Page</h1>
      </header>
      <main className="flex-1 p-4 overflow-y-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Total Tasks</h2>
            <p className="text-3xl font-bold">100</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Completed Tasks</h2>
            <p className="text-3xl font-bold">50</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Pending Tasks</h2>
            <p className="text-3xl font-bold">50</p>
          </div>
        </div>
        <div className="mt-4">
          <h2 className="text-lg font-bold">Task List</h2>
          <div className="bg-white p-4 rounded shadow">
            <table className="w-full table-auto">
              <thead className="bg-gray-100">
                <tr>
                  <th className="px-4 py-2">Task ID</th>
                  <th className="px-4 py-2">Task Name</th>
                  <th className="px-4 py-2">Status</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td className="px-4 py-2">1</td>
                  <td className="px-4 py-2">Task 1</td>
                  <td className="px-4 py-2">Completed</td>
                </tr>
                <tr>
                  <td className="px-4 py-2">2</td>
                  <td className="px-4 py-2">Task 2</td>
                  <td className="px-4 py-2">Pending</td>
                </tr>
                <tr>
                  <td className="px-4 py-2">3</td>
                  <td className="px-4 py-2">Task 3</td>
                  <td className="px-4 py-2">Completed</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div className="mt-4">
          <h2 className="text-lg font-bold">Task Chart</h2>
          <div className="bg-white p-4 rounded shadow h-64"></div>
        </div>
      </main>
    </div>
  );
}

export default Tasklistpage;