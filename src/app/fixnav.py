import os
import shutil

# 1. FIX THE LAYOUT (Clickable Logo)
layout_content = """
import './globals.css';
import { Inter } from 'next/font/google';
import Link from 'next/link';

const inter = Inter({ subsets: ['latin'] });

export const metadata = {
  title: 'Elite Clean Group',
  description: 'Professional Commercial & Residential Cleaning',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        {/* TOP BAR */}
        <div className="bg-blue-900 text-white text-xs py-2 px-4 flex justify-between items-center">
          <div className="hidden md:flex space-x-4">
             <span>📍 Serving Greater Toronto Area</span>
             <span>🏆 WSIB Insured & Bonded</span>
          </div>
          <div className="flex space-x-4 font-bold">
             <a href="tel:416-555-0199">📞 (416) 555-0199</a>
             <a href="mailto:info@elitecleangroup.com" className="hidden sm:inline">✉️ info@elitecleangroup.com</a>
          </div>
        </div>

        {/* MAIN NAV */}
        <nav className="border-b sticky top-0 bg-white/95 backdrop-blur z-50">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16 items-center">
              {/* FIXED: Logo is now a Link */}
              <Link href="/" className="text-2xl font-extrabold text-blue-900 tracking-tight hover:opacity-80 transition">
                ELITE<span className="text-blue-600">CLEAN</span>
              </Link>
              
              <div className="hidden md:flex space-x-8 text-sm font-medium text-gray-700">
                <Link href="/commercial-janitorial" className="hover:text-blue-600">Commercial</Link>
                <Link href="/construction-cleanup" className="hover:text-blue-600">Construction</Link>
                <Link href="/airbnb-turnover" className="hover:text-blue-600">Airbnb</Link>
              </div>
              <div>
                <Link href="/quote" className="bg-blue-600 text-white px-5 py-2.5 rounded-full text-sm font-bold shadow-lg hover:bg-blue-700 transition transform hover:-translate-y-0.5">
                  Get Quote
                </Link>
              </div>
            </div>
          </div>
        </nav>

        {children}
        
        {/* FOOTER */}
        <footer className="bg-gray-900 text-gray-400 py-12 border-t border-gray-800">
            <div className="max-w-7xl mx-auto px-6 grid md:grid-cols-4 gap-8">
                <div>
                    <h3 className="text-white font-bold mb-4">ELITE CLEAN GROUP</h3>
                    <p className="text-sm">Professional cleaning standards for businesses that care about first impressions.</p>
                </div>
                <div>
                    <h4 className="text-white font-bold mb-4">Services</h4>
                    <ul className="space-y-2 text-sm">
                        <li><Link href="/commercial-janitorial">Janitorial Services</Link></li>
                        <li><Link href="/construction-cleanup">Post-Construction</Link></li>
                        <li><Link href="/airbnb-turnover">Airbnb Turnover</Link></li>
                    </ul>
                </div>
                <div>
                    <h4 className="text-white font-bold mb-4">Legal</h4>
                    <ul className="space-y-2 text-sm">
                        <li>Privacy Policy</li>
                        <li>Terms of Service</li>
                        <li>WSIB Certificates</li>
                    </ul>
                </div>
                <div>
                    <h4 className="text-white font-bold mb-4">Contact</h4>
                    <p className="text-sm">Toronto, ON</p>
                    <p className="text-white font-bold mt-2">(416) 555-0199</p>
                </div>
            </div>
        </footer>
      </body>
    </html>
  );
}
"""

# 2. FIX INNER PAGES (Unified Hero Design)
# We use the exact same 'relative bg-gray-900 py-32' structure from the home page.

airbnb_content = """
import Link from 'next/link';

export const metadata = {
  title: 'Airbnb Turnover Services | Elite Clean Group',
  description: 'Automated turnover cleaning for Superhosts.',
};

export default function AirbnbPage() {
  return (
    <main className="min-h-screen bg-white">
      {/* UNIFIED HERO */}
      <section className="relative bg-gray-900 text-white py-32 px-6">
        <div className="absolute inset-0 z-0">
            <img 
                src="https://images.unsplash.com/photo-1556911220-bff31c812dba?auto=format&fit=crop&q=80"
                className="w-full h-full object-cover opacity-20"
                alt="Airbnb Background"
            />
        </div>
        <div className="relative z-10 max-w-4xl mx-auto text-center">
          <span className="inline-block py-1 px-3 rounded-full bg-blue-800/50 border border-blue-500 text-blue-300 text-sm font-semibold mb-6">
            For Superhosts
          </span>
          <h1 className="text-5xl md:text-6xl font-extrabold tracking-tight mb-6">
            Automated <span className="text-blue-400">Turnover</span>
          </h1>
          <p className="text-xl text-gray-300 mb-10 max-w-2xl mx-auto">
            Hotel-standard cleaning, linen service, and damage reporting. We sync with your calendar so you never miss a check-in.
          </p>
          <Link href="/quote?service=airbnb" className="bg-blue-600 text-white px-8 py-4 rounded-lg font-bold text-lg hover:bg-blue-500 shadow-lg transition">
            Get Pricing
          </Link>
        </div>
      </section>

      {/* CONTENT */}
      <section className="py-20 px-6 max-w-7xl mx-auto grid md:grid-cols-2 gap-12 items-center">
        <div>
           <h2 className="text-3xl font-bold text-gray-900 mb-6">Protect your reviews.</h2>
           <p className="text-gray-600 text-lg mb-6">A single stray hair can ruin a guest's experience. Our team follows a strict 50-point checklist designed for short-term rentals.</p>
           <ul className="space-y-4 font-medium text-gray-700">
             <li className="flex items-center">✅ Photo evidence sent after every clean</li>
             <li className="flex items-center">✅ Supply restocking (coffee, TP, soap)</li>
             <li className="flex items-center">✅ Off-site laundry service available</li>
           </ul>
        </div>
        <div className="bg-gray-100 p-8 rounded-2xl border">
            <h3 className="font-bold text-xl mb-4">Our Standard Checklist</h3>
            <div className="space-y-3 text-sm text-gray-600">
                <div className="flex justify-between border-b border-gray-300 pb-2"><span>Change Linens</span> <span>Included</span></div>
                <div className="flex justify-between border-b border-gray-300 pb-2"><span>Sanitize Surfaces</span> <span>Included</span></div>
                <div className="flex justify-between border-b border-gray-300 pb-2"><span>Check for Damages</span> <span>Included</span></div>
                <div className="flex justify-between border-b border-gray-300 pb-2"><span>Welcome Gift Setup</span> <span>Optional</span></div>
            </div>
        </div>
      </section>
    </main>
  );
}
"""

construction_content = """
import Link from 'next/link';

export const metadata = {
  title: 'Post-Construction Cleaning | Elite Clean Group',
  description: 'Rough, Final, and Touch-up cleaning.',
};

export default function ConstructionPage() {
  return (
    <main className="min-h-screen bg-white">
      {/* UNIFIED HERO */}
      <section className="relative bg-gray-900 text-white py-32 px-6">
        <div className="absolute inset-0 z-0">
            <img 
                src="https://images.unsplash.com/photo-1581578731117-104f2a417954?auto=format&fit=crop&q=80"
                className="w-full h-full object-cover opacity-20"
                alt="Construction Background"
            />
        </div>
        <div className="relative z-10 max-w-4xl mx-auto text-center">
          <span className="inline-block py-1 px-3 rounded-full bg-orange-900/50 border border-orange-500 text-orange-300 text-sm font-semibold mb-6">
            WSIB Insured
          </span>
          <h1 className="text-5xl md:text-6xl font-extrabold tracking-tight mb-6">
            Post-Construction <span className="text-orange-500">Cleanup</span>
          </h1>
          <p className="text-xl text-gray-300 mb-10 max-w-2xl mx-auto">
            From rough clean to final detail. We remove stickers, paint splatter, and drywall dust so your project is move-in ready.
          </p>
          <Link href="/quote?service=construction" className="bg-orange-600 text-white px-8 py-4 rounded-lg font-bold text-lg hover:bg-orange-500 shadow-lg transition">
            Request Site Visit
          </Link>
        </div>
      </section>

      {/* CONTENT */}
      <section className="py-20 px-6 max-w-7xl mx-auto">
        <div className="grid md:grid-cols-3 gap-8">
            <div className="border p-8 rounded-xl hover:shadow-lg transition bg-white">
                <h3 className="text-xl font-bold mb-3">Phase 1: Rough Clean</h3>
                <p className="text-gray-600">Removal of large debris, trash, and packaging. Preparing floors for final installation.</p>
            </div>
            <div className="border p-8 rounded-xl hover:shadow-lg transition bg-blue-50 border-blue-200">
                <h3 className="text-xl font-bold mb-3">Phase 2: Final Clean</h3>
                <p className="text-gray-600">Deep vacuuming, window sticker removal, and polishing all fixtures and glass.</p>
            </div>
            <div className="border p-8 rounded-xl hover:shadow-lg transition bg-white">
                <h3 className="text-xl font-bold mb-3">Phase 3: Touch-Up</h3>
                <p className="text-gray-600">A final pass after movers leave to ensure perfection for the owner's walk-through.</p>
            </div>
        </div>
      </section>
    </main>
  );
}
"""

commercial_content = """
import Link from 'next/link';

export const metadata = {
  title: 'Commercial Janitorial | Elite Clean Group',
  description: 'Office and Building Maintenance.',
};

export default function CommercialPage() {
  return (
    <main className="min-h-screen bg-white">
      {/* UNIFIED HERO */}
      <section className="relative bg-gray-900 text-white py-32 px-6">
        <div className="absolute inset-0 z-0">
            <img 
                src="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80"
                className="w-full h-full object-cover opacity-20"
                alt="Office Background"
            />
        </div>
        <div className="relative z-10 max-w-4xl mx-auto text-center">
          <span className="inline-block py-1 px-3 rounded-full bg-blue-800/50 border border-blue-500 text-blue-300 text-sm font-semibold mb-6">
            Nightly & Weekly
          </span>
          <h1 className="text-5xl md:text-6xl font-extrabold tracking-tight mb-6">
            Commercial <span className="text-blue-400">Janitorial</span>
          </h1>
          <p className="text-xl text-gray-300 mb-10 max-w-2xl mx-auto">
            Reliable office cleaning that just works. We handle trash, floors, and restrooms so you can focus on business.
          </p>
          <Link href="/quote?service=commercial" className="bg-blue-600 text-white px-8 py-4 rounded-lg font-bold text-lg hover:bg-blue-500 shadow-lg transition">
            Get Custom Proposal
          </Link>
        </div>
      </section>

      {/* CONTENT */}
      <section className="py-20 px-6 max-w-7xl mx-auto grid md:grid-cols-2 gap-16 items-center">
        <div>
            <h2 className="text-3xl font-bold text-gray-900 mb-6">Tailored to your Facility</h2>
            <p className="text-gray-600 text-lg mb-6">We don't do cookie-cutter quotes. We walk your site to understand high-traffic areas and security protocols.</p>
            <ul className="grid grid-cols-2 gap-4 text-gray-600">
                <li className="p-4 bg-gray-50 rounded">🏢 Offices & Boardrooms</li>
                <li className="p-4 bg-gray-50 rounded">🚽 Restroom Sanitation</li>
                <li className="p-4 bg-gray-50 rounded">🍽️ Kitchens & Breakrooms</li>
                <li className="p-4 bg-gray-50 rounded">🗑️ Recycling & Waste</li>
            </ul>
        </div>
        <div className="bg-gray-900 text-white p-8 rounded-2xl">
            <h3 className="font-bold text-xl mb-4">Why Managers Choose Us</h3>
            <div className="space-y-4">
                <div>
                    <h4 className="text-blue-400 font-bold">Dedicated Account Manager</h4>
                    <p className="text-gray-400 text-sm">Direct line to a human, no call centers.</p>
                </div>
                <div>
                    <h4 className="text-blue-400 font-bold">Custom Schedules</h4>
                    <p className="text-gray-400 text-sm">We clean at 6 PM, 2 AM, or weekends.</p>
                </div>
            </div>
        </div>
      </section>
    </main>
  );
}
"""

def main():
    print("🚀 Applying Final Fixes...")
    
    # 1. Clear Next.js Cache (Crucial for visual updates)
    if os.path.exists(".next"):
        try:
            shutil.rmtree(".next")
            print("🧹 Cache (.next) cleared.")
        except Exception as e:
            print(f"⚠️ Could not clear cache: {e}")

    # 2. Map files
    files = {
        "src/app/layout.js": layout_content,
        "src/app/airbnb-turnover/page.js": airbnb_content,
        "src/app/construction-cleanup/page.js": construction_content,
        "src/app/commercial-janitorial/page.js": commercial_content,
    }

    # 3. Write files
    for path, content in files.items():
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"✅ Updated: {path}")

    print("\n🎉 DONE.")
    print("👉 IMPORTANT: You MUST run 'npm run dev' again for the rebuild to happen.")

if __name__ == "__main__":
    main()
