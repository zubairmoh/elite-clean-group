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