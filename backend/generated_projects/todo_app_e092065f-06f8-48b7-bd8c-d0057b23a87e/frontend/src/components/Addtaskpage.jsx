import React from 'react';

function AddTaskPage() {
  return (
    <div className="flex h-screen bg-gray-100">
      <div className="flex-1 p-6">
        <h1 className="text-3xl font-bold mb-4">Add Task Page</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-8">
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold mb-2">Total Tasks</h2>
            <p className="text-2xl font-bold">100</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold mb-2">Completed Tasks</h2>
            <p className="text-2xl font-bold">50</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold mb-2">Pending Tasks</h2>
            <p className="text-2xl font-bold">50</p>
          </div>
        </div>
        <div className="bg-white p-4 rounded shadow mb-8">
          <h2 className="text-lg font-bold mb-4">Task Chart</h2>
          <div className="h-64 bg-gray-200 rounded"></div>
        </div>
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-lg font-bold mb-4">Task Table</h2>
          <table className="w-full table-auto">
            <thead className="bg-gray-100">
              <tr>
                <th className="px-4 py-2">Task Name</th>
                <th className="px-4 py-2">Status</th>
                <th className="px-4 py-2">Due Date</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="px-4 py-2">Task 1</td>
                <td className="px-4 py-2">Completed</td>
                <td className="px-4 py-2">2024-01-01</td>
              </tr>
              <tr>
                <td className="px-4 py-2">Task 2</td>
                <td className="px-4 py-2">Pending</td>
                <td className="px-4 py-2">2024-01-15</td>
              </tr>
              <tr>
                <td className="px-4 py-2">Task 3</td>
                <td className="px-4 py-2">Completed</td>
                <td className="px-4 py-2">2024-02-01</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default AddTaskPage;