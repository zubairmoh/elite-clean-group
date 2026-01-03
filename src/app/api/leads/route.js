import { NextResponse } from 'next/server';

// Mock Data
const leads = [
    { id: 1, name: 'John Doe', details: 'Airbnb cleaning needed', status: 'New' }
];

export async function GET() {
  return NextResponse.json(leads);
}