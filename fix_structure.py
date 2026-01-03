import os

# Define the file structure and content
# Key: File path relative to project root
# Value: Content of the file
project_files = {
    # --- 1. MIDDLEWARE (Crucial for Admin Protection) ---
    "src/middleware.js": """
import { NextResponse } from 'next/server';

export function middleware(request) {
  // Simple check for an auth cookie
  const authCookie = request.cookies.get('auth_token');
  const { pathname } = request.nextUrl;

  // Protect /admin routes
  if (pathname.startsWith('/admin') && !authCookie) {
    const loginUrl = new URL('/login', request.url);
    return NextResponse.redirect(loginUrl);
  }

  return NextResponse.next();
}

export const config = {
  matcher: '/admin/:path*',
};
""",

    # --- 2. SHARED UTILS ---
    "src/lib/db.js": """
// Placeholder for Database connection (Prisma/Mongoose)
export const db = {
  // Mock data for now
  leads: [],
};
""",

    # --- 3. PUBLIC PAGES ---
    "src/app/page.js": """
import Link from 'next/link';

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold mb-8">Elite Clean Group</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Link href="/airbnb-turnover" className="p-6 border rounded hover:bg-gray-100">
          Airbnb Turnover
        </Link>
        <Link href="/construction-cleanup" className="p-6 border rounded hover:bg-gray-100">
          Construction Cleanup
        </Link>
      </div>
      <Link href="/quote" className="mt-8 bg-blue-600 text-white px-6 py-3 rounded">
        Get a Quote
      </Link>
    </main>
  );
}
""",
    "src/app/quote/page.js": """
'use client';
import { useState } from 'react';

export default function QuotePage() {
  const [status, setStatus] = useState('');

  async function handleSubmit(e) {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData);

    const res = await fetch('/api/quote', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });

    if (res.ok) setStatus('Quote request sent!');
  }

  return (
    <div className="p-8 max-w-lg mx-auto">
      <h1 className="text-2xl font-bold mb-4">Request a Quote</h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input name="name" placeholder="Your Name" required className="w-full p-2 border" />
        <input name="email" type="email" placeholder="Email" required className="w-full p-2 border" />
        <textarea name="details" placeholder="Job Details" className="w-full p-2 border" />
        <button type="submit" className="bg-green-600 text-white px-4 py-2 rounded">Submit</button>
      </form>
      {status && <p className="mt-4 text-green-600">{status}</p>}
    </div>
  );
}
""",

    # --- 4. ADMIN SECTION ---
    # Admin Layout (New)
    "src/app/admin/layout.js": """
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
""",
    "src/app/admin/page.js": """
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
""",

    # --- 5. API ROUTES ---
    # Auth
    "src/app/api/auth/login/route.js": """
import { NextResponse } from 'next/server';
import { cookies } from 'next/headers';

export async function POST(request) {
  const body = await request.json();
  
  // MOCK AUTH - Replace with real logic
  if (body.username === 'admin' && body.password === 'admin123') {
    cookies().set('auth_token', 'valid-token', { secure: true, httpOnly: true });
    return NextResponse.json({ success: true });
  }
  
  return NextResponse.json({ error: 'Invalid credentials' }, { status: 401 });
}
""",
    
    # Leads: GET (List) and POST (Create is handled by Quote)
    "src/app/api/leads/route.js": """
import { NextResponse } from 'next/server';

// Mock Data
const leads = [
    { id: 1, name: 'John Doe', details: 'Airbnb cleaning needed', status: 'New' }
];

export async function GET() {
  return NextResponse.json(leads);
}
""",

    # Quote Submission
    "src/app/api/quote/route.js": """
import { NextResponse } from 'next/server';

export async function POST(request) {
  const data = await request.json();
  console.log("New Quote Received:", data);
  
  // TODO: Insert into Database
  
  return NextResponse.json({ success: true, message: 'Quote received' });
}
""",

    # FIXED: Dynamic Route for Updates instead of 'api/leads/update'
    "src/app/api/leads/[id]/route.js": """
import { NextResponse } from 'next/server';

export async function PATCH(request, { params }) {
  const { id } = params;
  const body = await request.json();
  
  // TODO: Update lead with ID `id` in database
  console.log(`Updating lead ${id} with`, body);
  
  return NextResponse.json({ success: true, id });
}

export async function DELETE(request, { params }) {
  const { id } = params;
  // TODO: Delete from DB
  return NextResponse.json({ success: true, id });
}
"""
}

def create_project_structure():
    print("🚀 Restructuring Elite Clean Group Project...")
    
    # 1. Clean up old incorrect folders (Optional, be careful)
    old_path = "src/app/api/leads/update"
    if os.path.exists(old_path):
        print(f"⚠️  Note: You can manually delete '{old_path}' as we are replacing it with '[id]'.")

    # 2. Create files
    for file_path, content in project_files.items():
        # Ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Write file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        
        print(f"✅ Created/Updated: {file_path}")

    print("\n🎉 Fix Complete! Don't forget to run 'npm run dev' to test.")

if __name__ == "__main__":
    create_project_structure()
