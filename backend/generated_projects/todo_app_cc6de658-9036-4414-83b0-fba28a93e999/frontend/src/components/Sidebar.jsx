<aside className="w-64 h-screen p-4 bg-gray-50 dark:bg-gray-800 border-r border-gray-200 dark:border-gray-700 shadow-md flex flex-col">
    <div className="flex items-center justify-between pb-4 border-b border-gray-200 dark:border-gray-700 mb-4">
        <span className="text-2xl font-extrabold text-gray-900 dark:text-white">Todo App</span>
    </div>
    <nav className="flex-1 space-y-2">
        {/* Todo List Link */}
        {/* Assumes ClipboardList icon is imported from 'lucide-react' */}
        <Link 
            to="/todos" 
            className="flex items-center p-3 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group transition-colors duration-200"
        >
            <ClipboardList className="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
            <span className="ml-4 text-base font-medium whitespace-nowrap">Todo List</span>
        </Link>

        {/* Add Todo Link */}
        {/* Assumes PlusSquare icon is imported from 'lucide-react' */}
        <Link 
            to="/todos/add" 
            className="flex items-center p-3 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group transition-colors duration-200"
        >
            <PlusSquare className="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
            <span className="ml-4 text-base font-medium whitespace-nowrap">Add Todo</span>
        </Link>
    </nav>
</aside>