import os

# We will use standard <img> tags for now to avoid Next.js Image Config issues
# until you are ready to configure next.config.mjs properly.

project_files = {
    # --- 1. NEW PAGE: Commercial Janitorial (Fixes the 404) ---
    "src/app/commercial-janitorial/page.js": """
import Link from 'next/link';

export const metadata = {
  title: 'Commercial Janitorial Services | Elite Clean Group',
  description: 'Reliable office cleaning and janitorial services for businesses. Nightly cleaning, trash removal, and sanitization.',
};

export default function CommercialPage() {
  return (
    <main className="min-h-screen bg-white">
      {/* Hero Section */}
      <div className="relative h-64 bg-gray-900 flex items-center justify-center">
        <img 
          src="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80" 
          alt="Office Cleaning" 
          className="absolute inset-0 w-full h-full object-cover opacity-40"
        />
        <h1 className="relative text-4xl font-bold text-white z-10">Commercial Janitorial</h1>
      </div>

      <div className="max-w-4xl mx-auto p-8">
        <div className="prose lg:prose-xl">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">Keep Your Office Spotless & Professional</h2>
          <p className="text-gray-600 mb-6">
            A clean office is essential for productivity and first impressions. Elite Clean Group provides 
            comprehensive janitorial services tailored to your business hours. Whether you need nightly 
            cleaning or weekly maintenance, our team ensures your workspace is sanitized and welcoming.
          </p>

          <h3 className="text-xl font-semibold text-gray-800 mb-3">Our Commercial Services Include:</h3>
          <ul className="list-disc pl-5 space-y-2 text-gray-600 mb-8">
            <li>Daily/Nightly office cleaning</li>
            <li>Trash removal and recycling management</li>
            <li>Restroom sanitization and restocking</li>
            <li>Breakroom and kitchen cleaning</li>
            <li>Floor care (vacuuming, mopping, buffing)</li>
          </ul>
        </div>

        <div className="mt-8 bg-blue-50 p-6 rounded-lg border border-blue-100">
          <h3 className="text-lg font-bold text-blue-900">Ready for a cleaner workspace?</h3>
          <p className="text-blue-700 mb-4">Contact us today for a custom proposal based on your square footage.</p>
          <Link href="/quote?service=commercial" className="inline-block bg-blue-600 text-white px-6 py-3 rounded hover:bg-blue-700 font-medium">
            Request Commercial Quote
          </Link>
        </div>
      </div>
    </main>
  );
}
""",

    # --- 2. UPDATE: Construction Cleanup (Better SEO + Working Image) ---
    "src/app/construction-cleanup/page.js": """
import Link from 'next/link';

export const metadata = {
  title: 'Post-Construction Cleaning | Elite Clean Group',
  description: 'Professional post-construction cleanup. We remove debris, dust, and residue to make your new build move-in ready.',
};

export default function ConstructionPage() {
  return (
    <main className="min-h-screen bg-white">
      <div className="relative h-64 bg-gray-900 flex items-center justify-center">
        <img 
          src="https://images.unsplash.com/photo-1581578731117-104f2a417954?auto=format&fit=crop&q=80" 
          alt="Construction Site Cleaning" 
          className="absolute inset-0 w-full h-full object-cover opacity-40"
        />
        <h1 className="relative text-4xl font-bold text-white z-10">Construction Cleanup</h1>
      </div>

      <div className="max-w-4xl mx-auto p-8">
        <h2 className="text-2xl font-bold text-gray-800 mb-4">From Chaos to Move-In Ready</h2>
        <p className="text-gray-600 mb-6">
            Construction leaves behind a mess that standard cleaning can't handle. Our specialized team 
            removes heavy dust, stickers, paint splatter, and debris, ensuring your new property 
            is safe and sparkling for the final walk-through.
        </p>

        <div className="grid md:grid-cols-2 gap-6 mb-8">
            <div className="p-4 border rounded bg-gray-50">
                <h3 className="font-bold text-gray-900">Rough Clean</h3>
                <p className="text-sm text-gray-600">Removal of large debris, trash, and stickers from windows/appliances.</p>
            </div>
            <div className="p-4 border rounded bg-gray-50">
                <h3 className="font-bold text-gray-900">Final Detail Clean</h3>
                <p className="text-sm text-gray-600">Deep vacuuming, dusting all surfaces, and polishing fixtures.</p>
            </div>
        </div>

        <Link href="/quote?service=construction" className="inline-block bg-orange-600 text-white px-6 py-3 rounded hover:bg-orange-700 font-medium">
            Get Construction Quote
        </Link>
      </div>
    </main>
  );
}
""",

    # --- 3. UPDATE: Airbnb Turnover (Better SEO + Working Image) ---
    "src/app/airbnb-turnover/page.js": """
import Link from 'next/link';

export const metadata = {
  title: 'Airbnb & Vacation Rental Cleaning | Elite Clean Group',
  description: 'Fast and reliable Airbnb turnover services. Hotel-quality cleaning, linen changes, and restocking for your guests.',
};

export default function AirbnbPage() {
  return (
    <main className="min-h-screen bg-white">
      <div className="relative h-64 bg-gray-900 flex items-center justify-center">
        <img 
          src="https://images.unsplash.com/photo-1556911220-bff31c812dba?auto=format&fit=crop&q=80" 
          alt="Clean Kitchen" 
          className="absolute inset-0 w-full h-full object-cover opacity-40"
        />
        <h1 className="relative text-4xl font-bold text-white z-10">Airbnb Turnover</h1>
      </div>

      <div className="max-w-4xl mx-auto p-8">
        <h2 className="text-2xl font-bold text-gray-800 mb-4">Protect Your Superhost Status</h2>
        <p className="text-gray-600 mb-6">
            In the vacation rental business, a single hair can lead to a bad review. We understand 
            the high standards of Airbnb hosts. Our turnover service includes laundry, 
            inventory checks, and hotel-standard presentation.
        </p>

        <ul className="grid grid-cols-1 md:grid-cols-2 gap-2 text-gray-600 mb-8">
            <li className="flex items-center">✅ Same-day turnover</li>
            <li className="flex items-center">✅ Linen washing & changing</li>
            <li className="flex items-center">✅ Restocking essentials</li>
            <li className="flex items-center">✅ Damage reporting</li>
        </ul>

        <Link href="/quote?service=airbnb" className="inline-block bg-rose-600 text-white px-6 py-3 rounded hover:bg-rose-700 font-medium">
            Schedule a Turnover
        </Link>
      </div>
    </main>
  );
}
""",

    # --- 4. UPDATE: Home Page (Linking it all together) ---
    "src/app/page.js": """
import Link from 'next/link';

export const metadata = {
  title: 'Elite Clean Group | Professional Cleaning Services',
  description: 'Top-rated cleaning services for Airbnb, Commercial Offices, and Post-Construction sites.',
};

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col">
      {/* Hero */}
      <section className="bg-gray-900 text-white py-20 px-8 text-center">
        <h1 className="text-5xl font-bold mb-6">Professional Cleaning Standards</h1>
        <p className="text-xl text-gray-300 max-w-2xl mx-auto mb-8">
          Elite Clean Group specializes in high-stakes cleaning for businesses, construction sites, and vacation rentals.
        </p>
        <Link href="/quote" className="bg-blue-600 text-white px-8 py-4 rounded font-bold hover:bg-blue-500">
          Get a Free Quote
        </Link>
      </section>

      {/* Services Grid */}
      <section className="max-w-6xl mx-auto py-16 px-4 grid md:grid-cols-3 gap-8">
        
        {/* Card 1 */}
        <Link href="/airbnb-turnover" className="group block border rounded-lg overflow-hidden hover:shadow-lg transition">
          <div className="h-48 bg-gray-200 relative">
            <img src="https://images.unsplash.com/photo-1556911220-bff31c812dba?auto=format&fit=crop&q=80" className="w-full h-full object-cover" />
          </div>
          <div className="p-6">
            <h3 className="text-xl font-bold mb-2 group-hover:text-blue-600">Airbnb Turnover</h3>
            <p className="text-gray-600">Hotel-quality cleaning and linen service for your short-term rentals.</p>
          </div>
        </Link>

        {/* Card 2 */}
        <Link href="/construction-cleanup" className="group block border rounded-lg overflow-hidden hover:shadow-lg transition">
          <div className="h-48 bg-gray-200 relative">
            <img src="https://images.unsplash.com/photo-1581578731117-104f2a417954?auto=format&fit=crop&q=80" className="w-full h-full object-cover" />
          </div>
          <div className="p-6">
            <h3 className="text-xl font-bold mb-2 group-hover:text-blue-600">Construction Cleanup</h3>
            <p className="text-gray-600">Debris removal and final detailing for new builds and renovations.</p>
          </div>
        </Link>

        {/* Card 3 */}
        <Link href="/commercial-janitorial" className="group block border rounded-lg overflow-hidden hover:shadow-lg transition">
          <div className="h-48 bg-gray-200 relative">
            <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80" className="w-full h-full object-cover" />
          </div>
          <div className="p-6">
            <h3 className="text-xl font-bold mb-2 group-hover:text-blue-600">Commercial Janitorial</h3>
            <p className="text-gray-600">Reliable office cleaning and maintenance for your business.</p>
          </div>
        </Link>

      </section>
    </main>
  );
}
"""
}

def fix_content_seo():
    print("🚀 Fixing Content, Images, and SEO...")

    for file_path, content in project_files.items():
        # Ensure directory exists (Important for the new Commercial folder)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Write file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        
        print(f"✅ Updated/Created: {file_path}")

    print("\n🎉 All pages updated with working images and SEO text.")
    print("👉 Reload your browser. The 'Commercial' link should work now!")

if __name__ == "__main__":
    fix_content_seo()
