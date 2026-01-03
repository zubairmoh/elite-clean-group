import Link from 'next/link';

export default function ConstructionPage() {
  return (
    <main className="min-h-screen bg-white">
      {/* HERO SECTION */}
      <section className="relative h-[60vh] flex items-center justify-center bg-gray-900 text-white">
        <div className="absolute inset-0 overflow-hidden">
          <img src="https://images.unsplash.com/photo-1581578731117-104f2a417954?auto=format&fit=crop&q=80" className="w-full h-full object-cover opacity-30" alt="Construction" />
        </div>
        <div className="relative z-10 text-center max-w-4xl px-4">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">Construction Cleanup</h1>
          <p className="text-xl text-gray-300 mb-8">Rough, final, and touch-up cleaning.</p>
          <Link href="/quote?service=construction" className="bg-orange-600 text-white px-8 py-3 rounded font-bold hover:bg-orange-500">Request Site Visit</Link>
        </div>
      </section>

      {/* CONTENT */}
      <section className="py-20 px-6 max-w-4xl mx-auto">
        <h2 className="text-3xl font-bold mb-6 text-gray-900">Move-In Ready</h2>
        <p className="text-gray-600 mb-6">We remove stickers, paint splatter, and drywall dust.</p>
      </section>
    </main>
  );
}