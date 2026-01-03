import os

# Define the file structure
project_files = {
    # --- 1. RENAME MIDDLEWARE TO PROXY (Next.js 16 Fix) ---
    "src/proxy.js": """
import { NextResponse } from 'next/server';

export function proxy(request) {
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

    # --- 2. LOGIN PAGE UI ---
    "src/app/login/page.js": """
'use client';
import { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const router = useRouter();

  async function handleLogin(e) {
    e.preventDefault();
    setError('');

    const res = await fetch('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password }),
    });

    if (res.ok) {
      router.push('/admin');
      router.refresh(); // Refresh to update middleware state
    } else {
      setError('Invalid credentials');
    }
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded shadow-md w-96">
        <h1 className="text-2xl font-bold mb-6 text-center">Admin Login</h1>
        <form onSubmit={handleLogin} className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-1">Username</label>
            <input 
              type="text" 
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full p-2 border rounded"
              placeholder="admin"
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Password</label>
            <input 
              type="password" 
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full p-2 border rounded"
              placeholder="admin123"
            />
          </div>
          {error && <p className="text-red-500 text-sm">{error}</p>}
          <button type="submit" className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700">
            Login
          </button>
        </form>
        <p className="mt-4 text-xs text-gray-400 text-center">Use: admin / admin123</p>
      </div>
    </div>
  );
}
""",

    # --- 3. FIX LOGIN API (Next.js 15/16 await cookies) ---
    "src/app/api/auth/login/route.js": """
import { NextResponse } from 'next/server';
import { cookies } from 'next/headers';

export async function POST(request) {
  const body = await request.json();
  
  // MOCK AUTH - Replace with real DB logic later
  if (body.username === 'admin' && body.password === 'admin123') {
    // In Next.js 15+, cookies() is async
    const cookieStore = await cookies();
    cookieStore.set('auth_token', 'valid-token', { 
        secure: process.env.NODE_ENV === 'production',
        httpOnly: true,
        path: '/',
        maxAge: 60 * 60 * 24 // 1 day
    });
    return NextResponse.json({ success: true });
  }
  
  return NextResponse.json({ error: 'Invalid credentials' }, { status: 401 });
}
""",

    # --- 4. LOGOUT ROUTE ---
    "src/app/api/auth/logout/route.js": """
import { NextResponse } from 'next/server';
import { cookies } from 'next/headers';

export async function GET(request) {
  const cookieStore = await cookies();
  cookieStore.delete('auth_token');
  
  const loginUrl = new URL('/login', request.url);
  return NextResponse.redirect(loginUrl);
}
"""
}

def fix_and_login():
    print("🚀 Applying Next.js 16 Fixes & Adding Login...")

    # 1. Remove old deprecated middleware if it exists
    if os.path.exists("src/middleware.js"):
        os.remove("src/middleware.js")
        print("🗑️  Removed deprecated src/middleware.js")

    # 2. Create/Update files
    for file_path, content in project_files.items():
        # Ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Write file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        
        print(f"✅ Created/Updated: {file_path}")

    print("\n🎉 Done! Restart your server (`Ctrl+C` then `npm run dev`) to see changes.")
    print("👉 Login at: http://localhost:3002/login")
    print("👉 Creds: admin / admin123")

if __name__ == "__main__":
    fix_and_login()
