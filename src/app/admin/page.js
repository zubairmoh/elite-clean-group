// This would usually fetch data from the DB
async function getLeads() {
  // In a real app, call your DB directly here since this is a Server Component
  // For now, we fetch from our own API for demo purposes
  const res = await fetch('http://localhost:3000/api/leads', { cache: 'no-store' });
  if (!res.ok) return [];
  return res.json();
}

export default async function AdminDashboard() {
  const leads = await getLeads();

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Leads Dashboard</h1>
      <div className="bg-white shadow rounded-lg overflow-hidden">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Name</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Details</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Status</th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {leads.length === 0 ? (
                <tr><td colSpan="3" className="p-4 text-center">No leads found.</td></tr>
            ) : (
                leads.map((lead) => (
                <tr key={lead.id}>
                    <td className="px-6 py-4">{lead.name}</td>
                    <td className="px-6 py-4">{lead.details}</td>
                    <td className="px-6 py-4">
                    <span className="px-2 py-1 text-sm rounded bg-blue-100 text-blue-800">{lead.status}</span>
                    </td>
                </tr>
                ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}