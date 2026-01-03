export default function AdminLayout({ children }) {
  return (
    <div className="flex min-h-screen">
      <aside className="w-64 bg-gray-900 text-white p-4">
        <h2 className="text-xl font-bold mb-6">Admin Panel</h2>
        <nav>
          <a href="/admin" className="block py-2 hover:text-gray-300">Dashboard</a>
          <a href="/api/auth/logout" className="block py-2 text-red-400 mt-4">Logout</a>
        </nav>
      </aside>
      <main className="flex-1 p-8 bg-gray-50">
        {children}
      </main>
    </div>
  );
}