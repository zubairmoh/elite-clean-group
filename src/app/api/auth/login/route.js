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