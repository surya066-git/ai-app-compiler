import React from 'react';

function AnalyticsDashboard() {
  return (
    <div className="flex h-screen flex-col">
      <header className="bg-gray-900 text-white p-4">
        <h1 className="text-3xl font-bold">Analytics Dashboard</h1>
      </header>
      <main className="flex-1 p-4">
        <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Total Users</h2>
            <p className="text-3xl font-bold">10,000</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Total Sessions</h2>
            <p className="text-3xl font-bold">50,000</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Bounce Rate</h2>
            <p className="text-3xl font-bold">20%</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Average Session Duration</h2>
            <p className="text-3xl font-bold">5 minutes</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Top Referring Sites</h2>
            <ul>
              <li>Google</li>
              <li>Facebook</li>
              <li>Twitter</li>
            </ul>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Top Pages</h2>
            <ul>
              <li>/home</li>
              <li>/about</li>
              <li>/contact</li>
            </ul>
          </div>
        </div>
        <div className="mt-4">
          <h2 className="text-lg font-bold">Traffic Overview</h2>
          <div className="bg-white p-4 rounded shadow">
            <div className="h-64">
              {/* Chart placeholder */}
              <svg width="100%" height="100%" />
            </div>
          </div>
        </div>
        <div className="mt-4">
          <h2 className="text-lg font-bold">Recent Activity</h2>
          <div className="bg-white p-4 rounded shadow">
            <table className="w-full">
              <thead>
                <tr>
                  <th>Date</th>
                  <th>Event</th>
                  <th>User</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>2023-01-01</td>
                  <td>Login</td>
                  <td>John Doe</td>
                </tr>
                <tr>
                  <td>2023-01-02</td>
                  <td>Logout</td>
                  <td>Jane Doe</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </main>
    </div>
  );
}

export default AnalyticsDashboard;