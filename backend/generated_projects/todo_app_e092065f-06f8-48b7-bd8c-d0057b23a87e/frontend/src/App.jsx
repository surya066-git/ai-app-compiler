
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';

import HomePage from './components/HomePage';\nimport LoginPage from './components/LoginPage';\nimport RegisterPage from './components/RegisterPage';\nimport TaskListPage from './components/TaskListPage';\nimport AddTaskPage from './components/AddTaskPage';

function App() {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <div className="flex flex-1 overflow-hidden">
        <Sidebar />
        <main className="flex-1 overflow-y-auto bg-gray-100 p-4">
          <Routes>
            <Route path='/homepage' element={<HomePage />} />\n            <Route path='/loginpage' element={<LoginPage />} />\n            <Route path='/registerpage' element={<RegisterPage />} />\n            <Route path='/tasklistpage' element={<TaskListPage />} />\n            <Route path='/addtaskpage' element={<AddTaskPage />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}

export default App;
