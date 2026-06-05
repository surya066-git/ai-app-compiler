import React from 'react';

function AnalyticsDashboard() {
  return (
    <div className="flex h-screen flex-col">
      <header className="bg-gray-900 text-white p-4">
        <h1 className="text-3xl font-bold">Analytics Dashboard</h1>
      </header>
      <main className="flex-1 p-4">
        <section className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
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
            <h2 className="text-lg font-bold">Total Page Views</h2>
            <p className="text-3xl font-bold">100,000</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-lg font-bold">Unique Page Views</h2>
            <p className="text-3xl font-bold">50,000</p>
          </div>
        </section>
        <section className="mt-4">
          <h2 className="text-lg font-bold">Traffic Overview</h2>
          <div className="bg-white p-4 rounded shadow">
            <table className="w-full table-auto">
              <thead className="bg-gray-100">
                <tr>
                  <th className="px-4 py-2">Date</th>
                  <th className="px-4 py-2">Sessions</th>
                  <th className="px-4 py-2">Bounce Rate</th>
                  <th className="px-4 py-2">Average Session Duration</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td className="px-4 py-2">2022-01-01</td>
                  <td className="px-4 py-2">100</td>
                  <td className="px-4 py-2">20%</td>
                  <td className="px-4 py-2">5 minutes</td>
                </tr>
                <tr>
                  <td className="px-4 py-2">2022-01-02</td>
                  <td className="px-4 py-2">150</td>
                  <td className="px-4 py-2">25%</td>
                  <td className="px-4 py-2">10 minutes</td>
                </tr>
                <tr>
                  <td className="px-4 py-2">2022-01-03</td>
                  <td className="px-4 py-2">200</td>
                  <td className="px-4 py-2">30%</td>
                  <td className="px-4 py-2">15 minutes</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>
        <section className="mt-4">
          <h2 className="text-lg font-bold">Chart</h2>
          <div className="bg-white p-4 rounded shadow h-64"></div>
        </section>
      </main>
    </div>
  );
}

export default AnalyticsDashboard;