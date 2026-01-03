import os

project_files = {
    # --- 1. AIRBNB TURNOVER (Focus: Automation & Ratings) ---
    "src/app/airbnb-turnover/page.js": """
import Link from 'next/link';

export const metadata = {
  title: 'Airbnb & Vacation Rental Cleaning Service | Elite Clean Group',
  description: 'Automated turnover cleaning for Superhosts. Linen service, restocking, and damage reporting. 5-star standard guaranteed.',
};

export default function AirbnbPage() {
  const jsonLd = {
    '@context': 'https://schema.org',
    '@type': 'Service',
    'name': 'Airbnb Turnover Cleaning',
    'provider': {
      '@type': 'LocalBusiness',
      'name': 'Elite Clean Group'
    },
    'areaServed': 'Toronto',
    'description': 'Complete turnover service including linens and restocking.'
  };

  return (
    <main className="min-h-screen bg-white">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />
      
      {/* HERO */}
      <section className="relative h-[60vh] flex items-center justify-center bg-gray-900 text-white overflow-hidden">
        <div className="absolute inset-0 z-0">
          <img src="https://images.unsplash.com/photo-1556911220-bff31c812dba?auto=format&fit=crop&q=80" className="w-full h-full object-cover opacity-30" alt="Airbnb Bedroom" />
        </div>
        <div className="relative z-10 text-center px-4 max-w-4xl mx-auto">
          <span className="text-blue-400 font-bold tracking-widest uppercase text-sm mb-4 block">For Hosts Who Value Reviews</span>
          <h1 className="text-5xl md:text-6xl font-extrabold mb-6">Automate Your Turnover</h1>
          <p className="text-xl text-gray-300 mb-8 max-w-2xl mx-auto">Don't let a stray hair cost you a 5-star review. We provide hotel-standard cleaning, linen changes, and inventory checks.</p>
          <Link href="/quote?service=airbnb" className="bg-blue-600 text-white px-8 py-4 rounded-lg font-bold hover:bg-blue-500 transition">
            Get Pricing
          </Link>
        </div>
      </section>

      {/* PAIN POINTS */}
      <section className="py-20 px-6 max-w-7xl mx-auto grid md:grid-cols-2 gap-12 items-center">
        <div>
           <h2 className="text-3xl font-bold text-gray-900 mb-6">You're in the hospitality business,<br/>not the cleaning business.</h2>
           <p className="text-gray-600 text-lg mb-6">Managing multiple properties is stressful enough without worrying if the cleaner showed up. We integrate with your booking calendar to ensure your unit is ready 100% of the time.</p>
           <ul className="space-y-4">
             <li className="flex items-center text-gray-700">
               <span className="w-6 h-6 bg-green-100 text-green-600 rounded-full flex items-center justify-center mr-3">✓</span>
               Photo evidence sent after every clean
             </li>
             <li className="flex items-center text-gray-700">
               <span className="w-6 h-6 bg-green-100 text-green-600 rounded-full flex items-center justify-center mr-3">✓</span>
               Damage and low-supply reporting
             </li>
             <li className="flex items-center text-gray-700">
               <span className="w-6 h-6 bg-green-100 text-green-600 rounded-full flex items-center justify-center mr-3">✓</span>
               Off-site laundry service available
             </li>
           </ul>
        </div>
        <div className="bg-gray-100 rounded-2xl p-8 border border-gray-200">
            <h3 className="font-bold text-xl mb-4">The "Superhost" Checklist</h3>
            <div className="space-y-3 text-sm text-gray-600">
                <div className="flex justify-between border-b pb-2"><span>Change all linens & towels</span> <span>✅</span></div>
                <div className="flex justify-between border-b pb-2"><span>Check under beds/sofas</span> <span>✅</span></div>
                <div className="flex justify-between border-b pb-2"><span>Sanitize remotes & switches</span> <span>✅</span></div>
                <div className="flex justify-between border-b pb-2"><span>Restock coffee/toiletries</span> <span>✅</span></div>
                <div className="flex justify-between border-b pb-2"><span>Arrange welcome basket</span> <span>✅</span></div>
            </div>
        </div>
      </section>

      {/* SEO FAQ SECTION */}
      <section className="bg-gray-50 py-20 px-6">
        <div className="max-w-4xl mx-auto">
            <h2 className="text-3xl font-bold text-center mb-12">Frequently Asked Questions</h2>
            <div className="space-y-6">
                <details className="bg-white p-6 rounded-lg shadow-sm cursor-pointer">
                    <summary className="font-bold text-lg">Do you bring your own supplies?</summary>
                    <p className="mt-2 text-gray-600">Yes, we bring all professional-grade equipment and supplies. If you prefer specific eco-friendly products for your guests, we can accommodate that.</p>
                </details>
                <details className="bg-white p-6 rounded-lg shadow-sm cursor-pointer">
                    <summary className="font-bold text-lg">How does scheduling work?</summary>
                    <p className="mt-2 text-gray-600">We can sync directly with your Airbnb/VRBO calendar or use a shared Google Calendar to automatically schedule cleans upon checkout.</p>
                </details>
            </div>
        </div>
      </section>

      {/* CTA */}
      <section className="bg-blue-900 text-white text-center py-24 px-6">
        <h2 className="text-4xl font-bold mb-6">Ready to automate?</h2>
        <Link href="/quote?service=airbnb" className="bg-white text-blue-900 px-10 py-4 rounded-lg font-bold text-lg hover:bg-gray-100 transition">
            Get a Quote
        </Link>
      </section>
    </main>
  );
}
""",

    # --- 2. CONSTRUCTION CLEANUP (Focus: Heavy Duty & Safety) ---
    "src/app/construction-cleanup/page.js": """
import Link from 'next/link';

export const metadata = {
  title: 'Post-Construction Cleaning Services | Elite Clean Group',
  description: 'Rough, Final, and Touch-up cleaning for new developments. We remove stickers, paint splatter, and drywall dust. WSIB Insured.',
};

export default function ConstructionPage() {
  const jsonLd = {
    '@context': 'https://schema.org',
    '@type': 'Service',
    'name': 'Post-Construction Cleaning',
    'provider': { '@type': 'LocalBusiness', 'name': 'Elite Clean Group' },
    'areaServed': 'Toronto',
    'description': 'Heavy duty debris removal and final detailing.'
  };

  return (
    <main className="min-h-screen bg-white">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />

      <section className="relative h-[60vh] flex items-center justify-center bg-gray-900 text-white overflow-hidden">
        <div className="absolute inset-0 z-0">
          <img src="https://images.unsplash.com/photo-1581578731117-104f2a417954?auto=format&fit=crop&q=80" className="w-full h-full object-cover opacity-30" alt="Construction Site" />
        </div>
        <div className="relative z-10 text-center px-4 max-w-4xl mx-auto">
          <span className="text-orange-500 font-bold tracking-widest uppercase text-sm mb-4 block">WSIB Insured & Bonded</span>
          <h1 className="text-5xl md:text-6xl font-extrabold mb-6">From Job Site to Showroom</h1>
          <p className="text-xl text-gray-300 mb-8 max-w-2xl mx-auto">Construction leaves a mess that standard cleaners can't handle. We specialize in heavy dust removal, sticker peeling, and final detailing.</p>
          <Link href="/quote?service=construction" className="bg-orange-600 text-white px-8 py-4 rounded-lg font-bold hover:bg-orange-500 transition">
            Request Site Visit
          </Link>
        </div>
      </section>

      <section className="py-20 px-6 max-w-7xl mx-auto">
        <div className="text-center mb-16">
            <h2 className="text-3xl font-bold text-gray-900">The 3 Phases of Construction Cleaning</h2>
            <p className="text-gray-500 mt-2">We can handle one phase or the entire project lifecycle.</p>
        </div>
        
        <div className="grid md:grid-cols-3 gap-8">
            <div className="border p-8 rounded-xl hover:shadow-lg transition bg-white">
                <div className="text-4xl mb-4">🏗️</div>
                <h3 className="text-xl font-bold mb-3">Phase 1: Rough Clean</h3>
                <p className="text-gray-600 text-sm">Removal of large debris, trash, and packaging. scraping floors for paint/drywall mud, and preparing the site for flooring installation.</p>
            </div>
            <div className="border p-8 rounded-xl hover:shadow-lg transition bg-blue-50 border-blue-200">
                <div className="text-4xl mb-4">✨</div>
                <h3 className="text-xl font-bold mb-3">Phase 2: Final Clean</h3>
                <p className="text-gray-600 text-sm">Deep vacuuming of all surfaces (including HVAC vents), cleaning inside cabinets/drawers, removing window stickers, and polishing fixtures.</p>
            </div>
            <div className="border p-8 rounded-xl hover:shadow-lg transition bg-white">
                <div className="text-4xl mb-4">🔍</div>
                <h3 className="text-xl font-bold mb-3">Phase 3: Touch-Up</h3>
                <p className="text-gray-600 text-sm">A final pass after the movers or last-minute tradesmen leave to ensure the property is 100% perfect for the owner's walk-through.</p>
            </div>
        </div>
      </section>

      <section className="bg-gray-900 text-white py-24 px-6 text-center">
        <h2 className="text-4xl font-bold mb-6">Deadlines Matter.</h2>
        <p className="text-gray-400 text-xl mb-10 max-w-2xl mx-auto">We offer 24/7 flexibility to ensure your project handover happens on time.</p>
        <Link href="/quote?service=construction" className="bg-white text-gray-900 px-10 py-4 rounded-lg font-bold text-lg hover:bg-gray-100 transition">
            Get Construction Quote
        </Link>
      </section>
    </main>
  );
}
""",

    # --- 3. COMMERCIAL JANITORIAL (Focus: Reliability & Professionalism) ---
    "src/app/commercial-janitorial/page.js": """
import Link from 'next/link';

export const metadata = {
  title: 'Commercial Office Cleaning & Janitorial Services | Elite Clean Group',
  description: 'Reliable nightly office cleaning. Trash removal, floor care, and restroom sanitation for Toronto businesses.',
};

export default function CommercialPage() {
  const jsonLd = {
    '@context': 'https://schema.org',
    '@type': 'Service',
    'name': 'Commercial Janitorial Services',
    'provider': { '@type': 'LocalBusiness', 'name': 'Elite Clean Group' },
    'areaServed': 'Toronto',
    'description': 'Office cleaning and building maintenance.'
  };

  return (
    <main className="min-h-screen bg-white">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />

      <section className="relative h-[60vh] flex items-center justify-center bg-gray-900 text-white overflow-hidden">
        <div className="absolute inset-0 z-0">
          <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80" className="w-full h-full object-cover opacity-30" alt="Office Building" />
        </div>
        <div className="relative z-10 text-center px-4 max-w-4xl mx-auto">
          <span className="text-blue-400 font-bold tracking-widest uppercase text-sm mb-4 block">Nightly & Weekly Service</span>
          <h1 className="text-5xl md:text-6xl font-extrabold mb-6">A Clean Office is a Productive Office</h1>
          <p className="text-xl text-gray-300 mb-8 max-w-2xl mx-auto">Your cleaning service should be invisible—you just notice that everything is perfect. We provide reliable janitorial solutions for offices, clinics, and retail.</p>
          <Link href="/quote?service=commercial" className="bg-blue-600 text-white px-8 py-4 rounded-lg font-bold hover:bg-blue-500 transition">
            Get Custom Proposal
          </Link>
        </div>
      </section>

      <section className="py-20 px-6 max-w-7xl mx-auto grid md:grid-cols-2 gap-16 items-center">
        <div>
            <h2 className="text-3xl font-bold text-gray-900 mb-6">Tailored to your Square Footage</h2>
            <p className="text-gray-600 text-lg mb-6">
                We don't do cookie-cutter quotes. We walk your site to understand your specific needs, high-traffic areas, and security protocols.
            </p>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div className="bg-gray-50 p-4 rounded border">
                    <h4 className="font-bold text-gray-900">General Areas</h4>
                    <p className="text-sm text-gray-600">Dusting, vacuuming, trash removal.</p>
                </div>
                <div className="bg-gray-50 p-4 rounded border">
                    <h4 className="font-bold text-gray-900">Restrooms</h4>
                    <p className="text-sm text-gray-600">Sanitization, restocking paper products.</p>
                </div>
                <div className="bg-gray-50 p-4 rounded border">
                    <h4 className="font-bold text-gray-900">Kitchens</h4>
                    <p className="text-sm text-gray-600">Countertops, sinks, appliance exteriors.</p>
                </div>
                <div className="bg-gray-50 p-4 rounded border">
                    <h4 className="font-bold text-gray-900">Floors</h4>
                    <p className="text-sm text-gray-600">Mopping, buffing, carpet cleaning.</p>
                </div>
            </div>
        </div>
        
        {/* Visual "Why Us" */}
        <div className="space-y-6">
            <div className="flex gap-4">
                <div className="flex-shrink-0 w-12 h-12 bg-blue-100 text-blue-600 flex items-center justify-center rounded-full font-bold">1</div>
                <div>
                    <h3 className="text-xl font-bold">Dedicated Account Manager</h3>
                    <p className="text-gray-600">You won't talk to a call center. You get a direct line to a manager who knows your building.</p>
                </div>
            </div>
            <div className="flex gap-4">
                <div className="flex-shrink-0 w-12 h-12 bg-blue-100 text-blue-600 flex items-center justify-center rounded-full font-bold">2</div>
                <div>
                    <h3 className="text-xl font-bold">Custom Schedules</h3>
                    <p className="text-gray-600">Need us at 6 PM? 2 AM? Weekends only? We build the schedule around your operations.</p>
                </div>
            </div>
            <div className="flex gap-4">
                <div className="flex-shrink-0 w-12 h-12 bg-blue-100 text-blue-600 flex items-center justify-center rounded-full font-bold">3</div>
                <div>
                    <h3 className="text-xl font-bold">Supply Management</h3>
                    <p className="text-gray-600">We can manage your inventory of toilet paper, soap, and towels so you never run out.</p>
                </div>
            </div>
        </div>
      </section>

      <section className="bg-blue-900 text-white text-center py-24 px-6">
        <h2 className="text-4xl font-bold mb-6">Let's discuss your facility.</h2>
        <Link href="/quote?service=commercial" className="bg-white text-blue-900 px-10 py-4 rounded-lg font-bold text-lg hover:bg-gray-100 transition">
            Get Janitorial Quote
        </Link>
      </section>
    </main>
  );
}
"""
}

def upgrade_inner_pages():
    print("🚀 Upgrading Inner Pages to 'Pro' Standard...")
    print("📝 Injecting JSON-LD Schema for SEO...")

    for file_path, content in project_files.items():
        # Ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Write file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        
        print(f"✅ Upgraded: {file_path}")

    print("\n🎉 Upgrade Complete!")
    print("👉 Check /airbnb-turnover")
    print("👉 Check /construction-cleanup")
    print("👉 Check /commercial-janitorial")

if __name__ == "__main__":
    upgrade_inner_pages()
