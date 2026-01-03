import Link from 'next/link';

export const metadata = { title: 'Post-Construction Cleanup | Elite Clean Group' };

export default function ConstructionPage() {
  return (
    <main className="min-h-screen bg-white">
      <section className="relative h-[60vh] flex items-center justify-center bg-gray-900 text-white">
        <div className="absolute inset-0 overflow-hidden">
          <img src="https://images.unsplash.com/photo-1581578731117-104f2a417954?auto=format&fit=crop&q=80" className="w-full h-full object-cover opacity-30" alt="Construction" />
        </div>
        <div className="relative z-10 text-center max-w-4xl px-4">
          <span className="text-orange-500 font-bold tracking-widest uppercase text-sm mb-4 block">WSIB Insured & Bonded</span>
          <h1 className="text-5xl md:text-6xl font-bold mb-6">Construction Cleanup</h1>
          <p className="text-xl text-gray-300 mb-8">Rough, final, and touch-up cleaning for new developments.</p>
          <Link href="/quote?service=construction" className="bg-orange-600 text-white px-8 py-3 rounded font-bold hover:bg-orange-500">Request Site Visit</Link>
        </div>
      </section>

      <section className="py-20 px-6 max-w-7xl mx-auto">
        <div className="text-center mb-16">
            <h2 className="text-3xl font-bold text-gray-900">The 3 Phases of Construction Cleaning</h2>
            <p className="text-gray-500 mt-2">We handle the mess so you can handle the handover.</p>
        </div>
        
        <div className="grid md:grid-cols-3 gap-8 mb-16">
            <div className="border p-8 rounded-xl hover:shadow-lg transition bg-white">
                <h3 className="text-xl font-bold mb-3">Phase 1: Rough Clean</h3>
                <p className="text-gray-600 text-sm">Removal of large debris, packaging, and trash. Scraping floors for paint and drywall mud. Preparing for flooring.</p>
            </div>
            <div className="border p-8 rounded-xl hover:shadow-lg transition bg-blue-50 border-blue-200">
                <h3 className="text-xl font-bold mb-3">Phase 2: Final Clean</h3>
                <p className="text-gray-600 text-sm">Deep vacuuming of all surfaces, window sticker removal, polishing fixtures, and cleaning inside cabinets.</p>
            </div>
            <div className="border p-8 rounded-xl hover:shadow-lg transition bg-white">
                <h3 className="text-xl font-bold mb-3">Phase 3: Touch-Up</h3>
                <p className="text-gray-600 text-sm">A final pass after the movers or last-minute tradesmen leave to ensure the property is perfect.</p>
            </div>
        </div>

        {/* SAFETY SECTION */}
        <div className="bg-gray-100 rounded-2xl p-8 md:p-12 flex flex-col md:flex-row items-center gap-8">
            <div className="flex-1">
                <h2 className="text-2xl font-bold text-gray-900 mb-4">Safety First Compliance</h2>
                <p className="text-gray-600 mb-4">Construction sites are dangerous. Our team is fully trained on safety protocols to ensure zero accidents.</p>
                <ul className="grid grid-cols-2 gap-2 text-sm text-gray-700">
                    <li>✅ PPE Required (Hard hats, boots)</li>
                    <li>✅ WHMIS Certified Staff</li>
                    <li>✅ Liability Insurance ($5M)</li>
                    <li>✅ WSIB Coverage</li>
                </ul>
            </div>
            <div>
                 <Link href="/quote?service=construction" className="bg-gray-900 text-white px-8 py-3 rounded font-bold hover:bg-gray-800">Get Quote</Link>
            </div>
        </div>
      </section>
    </main>
  );
}