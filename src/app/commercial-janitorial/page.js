import Link from 'next/link';

export const metadata = { title: 'Commercial Janitorial | Elite Clean Group' };

export default function CommercialPage() {
  return (
    <main className="min-h-screen bg-white">
      {/* HERO */}
      <section className="relative h-[60vh] flex items-center justify-center bg-gray-900 text-white">
        <div className="absolute inset-0 overflow-hidden">
          <img src="https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&q=80" className="w-full h-full object-cover opacity-30" alt="Office" />
        </div>
        <div className="relative z-10 text-center max-w-4xl px-4">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">Commercial Janitorial</h1>
          <p className="text-xl text-gray-300 mb-8">Reliable nightly office cleaning tailored to your schedule.</p>
          <Link href="/quote?service=commercial" className="bg-blue-600 text-white px-8 py-3 rounded font-bold hover:bg-blue-500">Get Custom Proposal</Link>
        </div>
      </section>

      {/* DETAILED CHECKLIST */}
      <section className="py-20 px-6 max-w-7xl mx-auto">
        <div className="grid md:grid-cols-2 gap-12 items-start">
            <div>
                <h2 className="text-3xl font-bold text-gray-900 mb-6">What We Clean</h2>
                <p className="text-gray-600 mb-6">A clean office boosts morale and productivity. Our comprehensive checklist covers every corner.</p>
                <div className="space-y-4">
                    <details className="group border rounded-lg p-4 bg-gray-50 open:bg-white">
                        <summary className="font-bold cursor-pointer list-none flex justify-between items-center text-gray-900">
                            🏢 General Areas & Offices <span className="text-blue-600">+</span>
                        </summary>
                        <ul className="mt-4 text-sm text-gray-600 space-y-2 pl-4 list-disc">
                            <li>Dusting desktops, monitors, and shelves</li>
                            <li>Vacuuming carpets and mopping hard floors</li>
                            <li>Emptying trash and recycling bins</li>
                            <li>Wiping down door handles and light switches</li>
                        </ul>
                    </details>
                    <details className="group border rounded-lg p-4 bg-gray-50 open:bg-white">
                        <summary className="font-bold cursor-pointer list-none flex justify-between items-center text-gray-900">
                            🚽 Restrooms <span className="text-blue-600">+</span>
                        </summary>
                        <ul className="mt-4 text-sm text-gray-600 space-y-2 pl-4 list-disc">
                            <li>Sanitizing toilets, urinals, and sinks</li>
                            <li>Polishing mirrors and chrome fixtures</li>
                            <li>Restocking toilet paper, towels, and soap</li>
                            <li>Mopping with hospital-grade disinfectant</li>
                        </ul>
                    </details>
                    <details className="group border rounded-lg p-4 bg-gray-50 open:bg-white">
                        <summary className="font-bold cursor-pointer list-none flex justify-between items-center text-gray-900">
                            🍽️ Kitchen & Breakrooms <span className="text-blue-600">+</span>
                        </summary>
                        <ul className="mt-4 text-sm text-gray-600 space-y-2 pl-4 list-disc">
                            <li>Wiping countertops and tables</li>
                            <li>Cleaning sink and exterior of appliances</li>
                            <li>Refilling paper towel dispensers</li>
                            <li>Spot cleaning walls and cabinets</li>
                        </ul>
                    </details>
                </div>
            </div>
            
            {/* OUR PROCESS */}
            <div className="bg-blue-900 text-white p-8 rounded-2xl">
                <h3 className="text-2xl font-bold mb-6">Our Onboarding Process</h3>
                <div className="space-y-8">
                    <div className="flex gap-4">
                        <div className="w-8 h-8 rounded-full bg-blue-500 flex items-center justify-center font-bold">1</div>
                        <div>
                            <h4 className="font-bold text-lg">Site Walkthrough</h4>
                            <p className="text-gray-300 text-sm">We visit your facility to identify high-traffic areas and specific needs.</p>
                        </div>
                    </div>
                    <div className="flex gap-4">
                        <div className="w-8 h-8 rounded-full bg-blue-500 flex items-center justify-center font-bold">2</div>
                        <div>
                            <h4 className="font-bold text-lg">Custom Proposal</h4>
                            <p className="text-gray-300 text-sm">You get a detailed quote tailored to your square footage and frequency.</p>
                        </div>
                    </div>
                    <div className="flex gap-4">
                        <div className="w-8 h-8 rounded-full bg-blue-500 flex items-center justify-center font-bold">3</div>
                        <div>
                            <h4 className="font-bold text-lg">The "First Deep Clean"</h4>
                            <p className="text-gray-300 text-sm">We start every new contract with a deep clean to bring the facility up to our standard.</p>
                        </div>
                    </div>
                </div>
                <div className="mt-8 pt-8 border-t border-blue-800 text-center">
                    <Link href="/quote?service=commercial" className="inline-block bg-white text-blue-900 px-6 py-3 rounded font-bold hover:bg-gray-100">Start Your Proposal</Link>
                </div>
            </div>
        </div>
      </section>
    </main>
  );
}