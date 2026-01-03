import { NextResponse } from 'next/server';

export async function POST(request) {
  const data = await request.json();
  console.log("New Quote Received:", data);
  
  // TODO: Insert into Database
  
  return NextResponse.json({ success: true, message: 'Quote received' });
}