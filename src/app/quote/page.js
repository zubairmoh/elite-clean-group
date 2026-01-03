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