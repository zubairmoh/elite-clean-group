import os

project_files = {
    # --- 1. MAIN PAGE (Fixing the Missing Image) ---
    "src/app/page.js": """
'use client';
import Link from 'next/link';
import { useCity } from '../hooks/useCity';

export default function Home() {
  const city = useCity();

  return (
    <main className="flex min-h-screen flex-col">
      
      {/* HERO SECTION */}
      <section className="relative bg-gray-900 text-white py-32 px-6">
        <div className="absolute inset-0 z-0">
            <img 
                src="https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&q=80"
                className="w-full h-full object-cover opacity-20"
                alt="Office Background"
            />
        </div>
        
        <div className="relative z-10 max-w-4xl mx-auto text-center">
          <span className="inline-block py-1 px-3 rounded-full bg-blue-800/50 border border-blue-500 text-blue-300 text-sm font-semibold mb-6">
            🚀 Now serving {city} and surrounding areas
          </span>
          <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight mb-6 leading-tight">
            The Standard for <br/>
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300">
              Commercial Cleaning
            </span>
          </h1>
          <p className="text-xl text-gray-300 mb-10 max-w-2xl mx-auto">
            Stop worrying about reliability. We provide consistent, high-grade cleaning for {city}'s offices, construction sites, and short-term rentals.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link href="/quote" className="bg-blue-600 text-white px-8 py-4 rounded-lg font-bold text-lg hover:bg-blue-500 shadow-lg shadow-blue-900/50 transition">
              Get Custom Proposal
            </Link>
            <Link href="/commercial-janitorial" className="bg-transparent border border-gray-500 text-white px-8 py-4 rounded-lg font-bold text-lg hover:bg-gray-800 transition">
              View Services
            </Link>
          </div>
        </div>
      </section>

      {/* TRUST SIGNALS */}
      <section className="py-10 border-b bg-gray-50">
        <div className="max-w-7xl mx-auto px-6 text-center">
            <p className="text-sm font-bold text-gray-400 uppercase tracking-widest mb-6">Trusted by businesses in {city}</p>
            <div className="flex flex-wrap justify-center gap-8 md:gap-16 opacity-50 grayscale">
                <span className="text-2xl font-bold text-gray-600">RE/MAX</span>
                <span className="text-2xl font-bold text-gray-600">Scotiabank</span>
                <span className="text-2xl font-bold text-gray-600">WeWork</span>
                <span className="text-2xl font-bold text-gray-600">EllisDon</span>
            </div>
        </div>
      </section>

      {/* SERVICES GRID - FIXED IMAGE FOR COMMERCIAL */}
      <section className="bg-gray-900 text-white py-24 px-6">
        <div className="max-w-7xl mx-auto">
            <div className="flex justify-between items-end mb-12">
                <div>
                    <h2 className="text-3xl font-bold mb-2">Our Core Services</h2>
                    <p className="text-gray-400">Specialized teams for specific environments.</p>
                </div>
            </div>

            <div className="grid md:grid-cols-3 gap-8">
                {/* Airbnb */}
                <Link href="/airbnb-turnover" className="group block relative h-80 rounded-2xl overflow-hidden hover:ring-4 ring-blue-600 transition">
                    <img src="https://images.unsplash.com/photo-1556911220-bff31c812dba?auto=format&fit=crop&q=80" className="absolute inset-0 w-full h-full object-cover transition duration-500 group-hover:scale-110" />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/90 to-transparent"></div>
                    <div className="absolute bottom-0 p-8">
                        <h3 className="text-2xl font-bold mb-2">Airbnb Turnover</h3>
                        <p className="text-gray-300 text-sm">Automated scheduling for your short-term rentals.</p>
                    </div>
                </Link>

                {/* Commercial - FIXED IMAGE */}
                <Link href="/commercial-janitorial" className="group block relative h-80 rounded-2xl overflow-hidden hover:ring-4 ring-blue-600 transition">
                    <img src="https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&q=80" className="absolute inset-0 w-full h-full object-cover transition duration-500 group-hover:scale-110" />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/90 to-transparent"></div>
                    <div className="absolute bottom-0 p-8">
                        <h3 className="text-2xl font-bold mb-2">Office Janitorial</h3>
                        <p className="text-gray-300 text-sm">Nightly cleaning for professional workspaces.</p>
                    </div>
                </Link>

                {/* Construction */}
                <Link href="/construction-cleanup" className="group block relative h-80 rounded-2xl overflow-hidden hover:ring-4 ring-blue-600 transition">
                    <img src="https://images.unsplash.com/photo-1581578731117-104f2a417954?auto=format&fit=crop&q=80" className="absolute inset-0 w-full h-full object-cover transition duration-500 group-hover:scale-110" />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/90 to-transparent"></div>
                    <div className="absolute bottom-0 p-8">
                        <h3 className="text-2xl font-bold mb-2">Post-Construction</h3>
                        <p className="text-gray-300 text-sm">Heavy debris removal and final detailing.</p>
                    </div>
                </Link>
            </div>
        </div>
      </section>
      
       {/* CTA SECTION */}
      <section className="py-24 px-6 bg-blue-600 text-white text-center">
        <h2 className="text-3xl md:text-4xl font-bold mb-6">Ready to upgrade your cleaning standards?</h2>
        <p className="text-blue-100 text-xl mb-10 max-w-2xl mx-auto">Get a free quote in less than 24 hours. No contracts required for the first month.</p>
        <Link href="/quote" className="bg-white text-blue-900 px-10 py-4 rounded-lg font-bold text-lg hover:bg-gray-100 shadow-xl transition">
            Get Your Free Quote
        </Link>
      </section>
    </main>
  );
}
""",

    # --- 2. COMMERCIAL JANITORIAL (Added: Process & FAQ) ---
    "src/app/commercial-janitorial/page.js": """
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
""",

    # --- 3. CONSTRUCTION (Added: Safety & Phases) ---
    "src/app/construction-cleanup/page.js": """
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
""",

    # --- 4. AIRBNB (Added: Host Benefits) ---
    "src/app/airbnb-turnover/page.js": """
import Link from 'next/link';

export const metadata = { title: 'Airbnb Turnover | Elite Clean Group' };

export default function AirbnbPage() {
  return (
    <main className="min-h-screen bg-white">
      <section className="relative h-[60vh] flex items-center justify-center bg-gray-900 text-white">
        <div className="absolute inset-0 overflow-hidden">
          <img src="https://images.unsplash.com/photo-1556911220-bff31c812dba?auto=format&fit=crop&q=80" className="w-full h-full object-cover opacity-30" alt="Airbnb" />
        </div>
        <div className="relative z-10 text-center max-w-4xl px-4">
          <span className="text-blue-400 font-bold tracking-widest uppercase text-sm mb-4 block">For Superhosts</span>
          <h1 className="text-5xl md:text-6xl font-bold mb-6">Automated Turnover</h1>
          <p className="text-xl text-gray-300 mb-8">Hotel-quality cleaning, linen service, and damage reporting.</p>
          <Link href="/quote?service=airbnb" className="bg-blue-600 text-white px-8 py-3 rounded font-bold hover:bg-blue-500">Get Pricing</Link>
        </div>
      </section>

      <section className="py-20 px-6 max-w-7xl mx-auto grid md:grid-cols-2 gap-12 items-center">
        <div>
           <h2 className="text-3xl font-bold text-gray-900 mb-6">Don't lose your Superhost status.</h2>
           <p className="text-gray-600 text-lg mb-6">Managing multiple properties is stressful. We integrate with your booking calendar (Airbnb, VRBO, Guesty) to ensure your unit is ready 100% of the time.</p>
           
           <div className="space-y-6">
                <div className="flex gap-4">
                    <div className="text-2xl">📸</div>
                    <div><h4 className="font-bold text-gray-900">Photo Evidence</h4><p className="text-sm text-gray-600">We send photos after every clean so you know it's ready.</p></div>
                </div>
                <div className="flex gap-4">
                    <div className="text-2xl">🧺</div>
                    <div><h4 className="font-bold text-gray-900">Linen Service</h4><p className="text-sm text-gray-600">We wash linens on-site or off-site depending on your unit.</p></div>
                </div>
                <div className="flex gap-4">
                    <div className="text-2xl">🧴</div>
                    <div><h4 className="font-bold text-gray-900">Restocking</h4><p className="text-sm text-gray-600">We replenish coffee, toilet paper, and soap.</p></div>
                </div>
           </div>
        </div>
        <div className="bg-gray-100 p-8 rounded-2xl border">
            <h3 className="font-bold text-xl mb-4">Our Standard Checklist</h3>
            <div className="space-y-3 text-sm text-gray-600">
                <div className="flex justify-between border-b border-gray-300 pb-2"><span>Change Linens & Towels</span> <span>✅</span></div>
                <div className="flex justify-between border-b border-gray-300 pb-2"><span>Sanitize Kitchen & Bath</span> <span>✅</span></div>
                <div className="flex justify-between border-b border-gray-300 pb-2"><span>Check Under Beds/Sofas</span> <span>✅</span></div>
                <div className="flex justify-between border-b border-gray-300 pb-2"><span>Empty Fridge & Trash</span> <span>✅</span></div>
                <div className="flex justify-between border-b border-gray-300 pb-2"><span>Report Damages</span> <span>✅</span></div>
                <div className="flex justify-between border-b border-gray-300 pb-2"><span>Arrange Welcome Gift</span> <span>Optional</span></div>
            </div>
        </div>
      </section>
    </main>
  );
}
"""
}

def apply_boost():
    print("🚀 Boosting Content & Fixing Images...")
    
    for path, content in project_files.items():
        # Clean delete to ensure update
        if os.path.exists(path):
            os.remove(path)
            
        # Write
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"✅ Updated {path}")

    print("\n⚠️  IMPORTANT: RESTART SERVER NOW")
    print("1. Ctrl + C")
    print("2. npm run dev")
    print("3. Check the Main Page (Commercial Image) and Inner Pages (New Content)")

if __name__ == "__main__":
    apply_boost()
