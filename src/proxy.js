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