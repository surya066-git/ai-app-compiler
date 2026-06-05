import React from 'react';

const WeatherDashboard = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4 sm:p-6 lg:p-8 font-sans">
      {/* Dashboard Header */}
      <header className="mb-8 text-center md:text-left">
        <h1 className="text-4xl sm:text-5xl font-extrabold text-gray-900 leading-tight drop-shadow-sm">
          WeatherDisplay Dashboard
        </h1>
        <p className="text-lg sm:text-xl text-gray-600 mt-3 max-w-2xl mx-auto md:mx-0">
          Get real-time weather updates and forecasts at a glance.
        </p>
      </header>

      {/* Main Content Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

        {/* Section for Weather Cards */}
        <section className="lg:col-span-2 grid grid-cols-1 md:grid-cols-2 gap-6">

          {/* Card 1: Current Temperature */}
          <div className="bg-white rounded-2xl shadow-xl p-6 flex flex-col transform transition-all duration-300 hover:scale-[1.02] hover:shadow-2xl border border-gray-100">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-semibold text-gray-800">Current Temperature</h2>
              <span className="text-blue-500 text-3xl">☀️</span> {/* Example icon */}
            </div>
            <p className="text-5xl font-bold text-blue-600 mb-2">28°C</p>
            <p className="text-gray-500 text-lg">Feels like 30°C, Mostly Sunny</p>
            <div className="mt-auto pt-4 border-t border-gray-100 text-sm text-gray-400">
              Last updated: Just now
            </div>
          </div>

          {/* Card 2: Humidity */}
          <div className="bg-white rounded-2xl shadow-xl p-6 flex flex-col transform transition-all duration-300 hover:scale-[1.02] hover:shadow-2xl border border-gray-100">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-semibold text-gray-800">Humidity Level</h2>
              <span className="text-green-500 text-3xl">💧</span> {/* Example icon */}
            </div>
            <p className="text-5xl font-bold text-green-600 mb-2">68%</p>
            <p className="text-gray-500 text-lg">Comfortable, with light breeze</p>
            <div className="mt-auto pt-4 border-t border-gray-100 text-sm text-gray-400">
              Dew Point: 20°C
            </div>
          </div>

          {/* Card 3: Wind Speed */}
          <div className="bg-white rounded-2xl shadow-xl p-6 flex flex-col transform transition-all duration-300 hover:scale-[1.02] hover:shadow-2xl border border-gray-100">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-semibold text-gray-800">Wind Speed</h2>
              <span className="text-purple-500 text-3xl">🌬️</span> {/* Example icon */}
            </div>
            <p className="text-5xl font-bold text-purple-600 mb-2">15 km/h</p>
            <p className="text-gray-500 text-lg">Moderate breeze from the East</p>
            <div className="mt-auto pt-4 border-t border-gray-100 text-sm text-gray-400">
              Gusts up to: 25 km/h
            </div>
          </div>

          {/* Card 4: Precipitation Chance */}
          <div className="bg-white rounded-2xl shadow-xl p-6 flex flex-col transform transition-all duration-300 hover:scale-[1.02] hover:shadow-2xl border border-gray-100">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-semibold text-gray-800">Precipitation Chance</h2>
              <span className="text-red-500 text-3xl">🌧️</span> {/* Example icon */}
            </div>
            <p className="text-5xl font-bold text-red-600 mb-2">20%</p>
            <p className="text-gray-500 text-lg">Low chance of scattered showers</p>
            <div className="mt-auto pt-4 border-t border-gray-100 text-sm text-gray-400">
              Next 24 hours forecast
            </div>
          </div>
        </section>

        {/* Chart/Table Placeholder */}
        <section className="bg-white rounded-2xl shadow-xl p-6 border border-gray-100">
          <h2 className="text-2xl font-semibold text-gray-800 mb-5">7-Day Temperature Trend</h2>
          <div className="h-80 bg-gray-50 border border-dashed border-gray-300 rounded-xl flex items-center justify-center text-gray-400 text-lg p-4">
            <p className="text-center">
              Chart Placeholder
              <br />
              (e.g., Line Chart for daily max/min temperatures)
            </p>
          </div>
          <p className="text-sm text-gray-500 mt-4">
            This section would display a dynamic chart or detailed table for historical or forecasted data using a charting library (e.g., Chart.js, Recharts) or a table component.
          </p>
        </section>
      </div>

      {/* Additional Section for Alerts or Extended Forecast */}
      <section className="mt-8 bg-white rounded-2xl shadow-xl p-6 border border-gray-100">
        <h2 className="text-2xl font-semibold text-gray-800 mb-5">Weather Alerts & Warnings</h2>
        <div className="h-48 bg-yellow-50 border border-dashed border-yellow-300 rounded-xl flex items-center justify-center text-yellow-600 text-lg p-4">
          <p className="text-center">
            No active weather alerts or warnings at this time.
            <br />
            (This area would show critical advisories if any)
          </p>
        </div>
        <p className="text-sm text-gray-500 mt-4">
          Stay informed about severe weather conditions impacting your area.
        </p>
      </section>
    </div>
  );
};

export default WeatherDashboard;