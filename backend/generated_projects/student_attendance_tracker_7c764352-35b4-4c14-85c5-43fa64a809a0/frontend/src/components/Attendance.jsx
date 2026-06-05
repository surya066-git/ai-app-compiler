import React from 'react';

function AttendanceDashboard() {
  return (
    <div className="max-w-7xl mx-auto py-10 px-4 sm:px-6 lg:px-8">
      <h1 className="text-3xl font-bold mb-4">Attendance Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div className="bg-white rounded-lg shadow-md p-4">
          <h2 className="text-lg font-bold mb-2">Total Students</h2>
          <p className="text-3xl font-bold">1000</p>
        </div>
        <div className="bg-white rounded-lg shadow-md p-4">
          <h2 className="text-lg font-bold mb-2">Present Students</h2>
          <p className="text-3xl font-bold">800</p>
        </div>
        <div className="bg-white rounded-lg shadow-md p-4">
          <h2 className="text-lg font-bold mb-2">Absent Students</h2>
          <p className="text-3xl font-bold">200</p>
        </div>
      </div>
      <div className="mt-8">
        <h2 className="text-lg font-bold mb-4">Attendance Chart</h2>
        <div className="bg-white rounded-lg shadow-md p-4 h-96">
          {/* Chart placeholder */}
          <div className="h-full w-full bg-gray-200"></div>
        </div>
      </div>
      <div className="mt-8">
        <h2 className="text-lg font-bold mb-4">Attendance Table</h2>
        <div className="bg-white rounded-lg shadow-md p-4">
          <table className="w-full table-auto">
            <thead className="bg-gray-100">
              <tr>
                <th className="px-4 py-2">Student Name</th>
                <th className="px-4 py-2">Attendance Status</th>
              </tr>
            </thead>
            <tbody>
              {/* Table data placeholder */}
              <tr>
                <td className="px-4 py-2">John Doe</td>
                <td className="px-4 py-2">Present</td>
              </tr>
              <tr>
                <td className="px-4 py-2">Jane Doe</td>
                <td className="px-4 py-2">Absent</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default AttendanceDashboard;