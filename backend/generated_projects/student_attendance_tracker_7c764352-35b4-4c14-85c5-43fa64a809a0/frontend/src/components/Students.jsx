import React from 'react';

function StudentDashboard() {
  return (
    <div className="max-w-7xl mx-auto py-10 px-4 sm:px-6 lg:px-8">
      <h1 className="text-3xl font-bold mb-4">Student Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div className="bg-white rounded-lg shadow-md p-4">
          <h2 className="text-lg font-bold mb-2">Total Students</h2>
          <p className="text-3xl font-bold">1000</p>
        </div>
        <div className="bg-white rounded-lg shadow-md p-4">
          <h2 className="text-lg font-bold mb-2">Active Students</h2>
          <p className="text-3xl font-bold">800</p>
        </div>
        <div className="bg-white rounded-lg shadow-md p-4">
          <h2 className="text-lg font-bold mb-2">Inactive Students</h2>
          <p className="text-3xl font-bold">200</p>
        </div>
      </div>
      <div className="mt-8">
        <h2 className="text-lg font-bold mb-4">Student Performance Chart</h2>
        <div className="bg-white rounded-lg shadow-md p-4 h-96">
          {/* Chart placeholder */}
        </div>
      </div>
      <div className="mt-8">
        <h2 className="text-lg font-bold mb-4">Student List</h2>
        <table className="w-full table-auto border-collapse border border-gray-200">
          <thead className="bg-gray-100">
            <tr>
              <th className="py-2 px-4 border border-gray-200">Name</th>
              <th className="py-2 px-4 border border-gray-200">Email</th>
              <th className="py-2 px-4 border border-gray-200">Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td className="py-2 px-4 border border-gray-200">John Doe</td>
              <td className="py-2 px-4 border border-gray-200">john@example.com</td>
              <td className="py-2 px-4 border border-gray-200">Active</td>
            </tr>
            <tr>
              <td className="py-2 px-4 border border-gray-200">Jane Doe</td>
              <td className="py-2 px-4 border border-gray-200">jane@example.com</td>
              <td className="py-2 px-4 border border-gray-200">Inactive</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default StudentDashboard;