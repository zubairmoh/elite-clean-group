import os
import shutil

# DIRECTORIES TO UPDATE
files_to_fix = {
    # 1. LAYOUT: Added 'cursor-pointer' and 'relative' to the logo link to force clickability
    "src/app/layout.js": """
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
        <div className="bg-blue-900 text-white text-xs py-2 px-4 flex justify-between items-center z-50 relative">
          <div className="hidden md:flex space-x-4">
             <span>📍 Serving Greater Toronto Area</span>
             <span>🏆 WSIB Insured & Bonded</span>
          </div>
          <div className="flex space-x-4 font-bold">
             <a href="tel:416-555-0199">📞 (416) 555-0199</a>
          </div>
        </div>

        {/* MAIN NAV - Z-INDEX 50 TO ENSURE IT IS CLICKABLE */}
        <nav className="border-b sticky top-0 bg-white/95 backdrop-blur z-[100]">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16 items-center">
              
              {/* --- CLICKABLE LOGO FIX --- */}
              <Link href="/" className="cursor-pointer group relative z-50">
                <span className="text-2xl font-extrabold text-blue-900 tracking-tight group-hover:opacity-80 transition">
                  ELITE<span className="text-blue-600">CLEAN</span>
                </span>
              </Link>
              {/* ------------------------- */}

              <div className="hidden md:flex space-x-8 text-sm font-medium text-gray-700">
                <Link href="/commercial-janitorial" className="hover:text-blue-600 py-2">Commercial</Link>
                <Link href="/construction-cleanup" className="hover:text-blue-600 py-2">Construction</Link>
                <Link href="/airbnb-turnover" className="hover:text-blue-600 py-2">Airbnb</Link>
              </div>
              <div>
                <Link href="/quote" className="bg-blue-600 text-white px-5 py-2.5 rounded-full text-sm font-bold shadow-lg hover:bg-blue-700 transition">
                  Get Quote
                </Link>
              </div>
            </div>
          </div>
        </nav>

        {children}
        
        <footer className="bg-gray-900 text-gray-400 py-12 border-t border-gray-800">
            <div className="max-w-7xl mx-auto px-6 text-center">
                <p className="text-sm">© 2024 Elite Clean Group. All rights reserved.</p>
            </div>
        </footer>
      </body>
    </html>
  );
}
""",

    # 2. AIRBNB PAGE (With Dark Hero)
    "src/app/airbnb-turnover/page.js": """
import Link from 'next/link';

export default function AirbnbPage() {
  return (
    <main className="min-h-screen bg-white">
      {/* HERO SECTION */}
      <section className="relative h-[60vh] flex items-center justify-center bg-gray-900 text-white">
        <div className="absolute inset-0 overflow-hidden">
          <img src="https://images.unsplash.com/photo-1556911220-bff31c812dba?auto=format&fit=crop&q=80" className="w-full h-full object-cover opacity-30" alt="Airbnb" />
        </div>
        <div className="relative z-10 text-center max-w-4xl px-4">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">Automated Turnover</h1>
          <p className="text-xl text-gray-300 mb-8">Hotel-quality cleaning for Superhosts.</p>
          <Link href="/quote?service=airbnb" className="bg-blue-600 text-white px-8 py-3 rounded font-bold hover:bg-blue-500">Get Pricing</Link>
        </div>
      </section>

      {/* CONTENT */}
      <section className="py-20 px-6 max-w-4xl mx-auto">
        <h2 className="text-3xl font-bold mb-6 text-gray-900">Protect Your Reviews</h2>
        <p className="text-gray-600 mb-6">We provide linen service, restocking, and damage reporting.</p>
      </section>
    </main>
  );
}
""",

    # 3. CONSTRUCTION PAGE (With Dark Hero)
    "src/app/construction-cleanup/page.js": """
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
""",

    # 4. COMMERCIAL PAGE (With Dark Hero)
    "src/app/commercial-janitorial/page.js": """
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
"""
}

def nuclear_reset():
    print("☢️  INITIATING NUCLEAR RESET...")
    
    # Check if we are in the right folder
    cwd = os.getcwd()
    if "elite-clean-group" not in cwd and "src" not in os.listdir(cwd):
        print(f"⚠️  WARNING: You seem to be in {cwd}. Are you in the project root?")
        confirm = input("Continue anyway? (y/n): ")
        if confirm.lower() != 'y':
            return

    # 1. DELETE CACHE
    if os.path.exists(".next"):
        try:
            shutil.rmtree(".next")
            print("✅ Deleted .next cache folder")
        except:
            print("❌ Could not delete .next (File in use?)")

    # 2. OVERWRITE FILES
    for path, content in files_to_fix.items():
        # Remove if exists
        if os.path.exists(path):
            os.remove(path)
            print(f"🗑️  Deleted old {path}")
        
        # Write new
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"✨ Created new {path}")

    print("\n" + "="*40)
    print("✅ RESET COMPLETE")
    print("="*40)
    print("👇 YOU MUST DO THIS NOW:")
    print("1. Click inside this terminal.")
    print("2. Press 'Ctrl + C' to stop the server.")
    print("3. Run: npm run dev")
    print("4. Go to http://localhost:3002 and REFRESH THE PAGE.")

if __name__ == "__main__":
    nuclear_reset()
