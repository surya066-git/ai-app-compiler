
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';

import TodoList from './components/TodoList';\nimport AddTodo from './components/AddTodo';

function App() {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <div className="flex flex-1 overflow-hidden">
        <Sidebar />
        <main className="flex-1 overflow-y-auto bg-gray-100 p-4">
          <Routes>
            <Route path='/todolist' element={<TodoList />} />\n            <Route path='/addtodo' element={<AddTodo />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}

export default App;
