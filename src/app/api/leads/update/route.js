import { NextResponse } from 'next/server';
import db from '@/lib/db';

export async function POST(request) {
  const { id, status } = await request.json();
  await sql`UPDATE leads SET status = ${status} WHERE id = ${id}`;
  return NextResponse.json({ success: true });
}
