import Link from 'next/link';

export default function CommercialPage() {
  return (
    <main className="min-h-screen bg-white">
      {/* HERO SECTION */}
      <section className="relative h-[60vh] flex items-center justify-center bg-gray-900 text-white">
        <div className="absolute inset-0 overflow-hidden">
          <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80" className="w-full h-full object-cover opacity-30" alt="Office" />
        </div>
        <div className="relative z-10 text-center max-w-4xl px-4">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">Commercial Janitorial</h1>
          <p className="text-xl text-gray-300 mb-8">Reliable nightly office cleaning.</p>
          <Link href="/quote?service=commercial" className="bg-blue-600 text-white px-8 py-3 rounded font-bold hover:bg-blue-500">Get Custom Proposal</Link>
        </div>
      </section>

      {/* CONTENT */}
      <section className="py-20 px-6 max-w-4xl mx-auto">
        <h2 className="text-3xl font-bold mb-6 text-gray-900">A Clean Office is Productive</h2>
        <p className="text-gray-600 mb-6">Trash removal, floor care, and restroom sanitation.</p>
      </section>
    </main>
  );
}