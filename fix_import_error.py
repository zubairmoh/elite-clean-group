import os

project_files = {
    # --- 1. Fix the Import in Page.js ---
    # We change '@/hooks/useCity' to '../hooks/useCity'
    "src/app/page.js": """
'use client';
import Link from 'next/link';
import { useCity } from '../hooks/useCity'; // FIXED: Changed @ to ..

export default function Home() {
  const city = useCity();

  return (
    <main className="flex min-h-screen flex-col">
      
      {/* 1. HERO SECTION - Darker, Professional, Dynamic */}
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

      {/* 2. TRUST SIGNALS */}
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

      {/* 3. VALUE PROPS */}
      <section className="py-24 px-6 max-w-7xl mx-auto">
        <div className="grid md:grid-cols-3 gap-12">
            <div className="space-y-4">
                <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center text-2xl">⚡</div>
                <h3 className="text-xl font-bold text-gray-900">Zero-Hassle Reliability</h3>
                <p className="text-gray-600">We show up. It sounds simple, but we know it's your biggest pain point. Our crews are tracked and supervised.</p>
            </div>
            <div className="space-y-4">
                <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center text-2xl">🛡️</div>
                <h3 className="text-xl font-bold text-gray-900">Fully Insured & Bonded</h3>
                <p className="text-gray-600">Peace of mind for your property. We carry $5M liability insurance and WSIB coverage for all staff.</p>
            </div>
            <div className="space-y-4">
                <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center text-2xl">💎</div>
                <h3 className="text-xl font-bold text-gray-900">Hospital-Grade Sanitation</h3>
                <p className="text-gray-600">We don't just dust. We sanitize high-touch points using eco-friendly, hospital-grade disinfectants.</p>
            </div>
        </div>
      </section>

      {/* 4. SERVICES GRID */}
      <section className="bg-gray-900 text-white py-24 px-6">
        <div className="max-w-7xl mx-auto">
            <div className="flex justify-between items-end mb-12">
                <div>
                    <h2 className="text-3xl font-bold mb-2">Our Core Services</h2>
                    <p className="text-gray-400">Specialized teams for specific environments.</p>
                </div>
                <Link href="/services" className="text-blue-400 hover:text-blue-300 hidden md:block">View all services →</Link>
            </div>

            <div className="grid md:grid-cols-3 gap-8">
                <Link href="/airbnb-turnover" className="group block relative h-80 rounded-2xl overflow-hidden hover:ring-4 ring-blue-600 transition">
                    <img src="https://images.unsplash.com/photo-1556911220-bff31c812dba?auto=format&fit=crop&q=80" className="absolute inset-0 w-full h-full object-cover transition duration-500 group-hover:scale-110" />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/90 to-transparent"></div>
                    <div className="absolute bottom-0 p-8">
                        <h3 className="text-2xl font-bold mb-2">Airbnb Turnover</h3>
                        <p className="text-gray-300 text-sm">Automated scheduling for your short-term rentals.</p>
                    </div>
                </Link>

                <Link href="/commercial-janitorial" className="group block relative h-80 rounded-2xl overflow-hidden hover:ring-4 ring-blue-600 transition">
                    <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80" className="absolute inset-0 w-full h-full object-cover transition duration-500 group-hover:scale-110" />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/90 to-transparent"></div>
                    <div className="absolute bottom-0 p-8">
                        <h3 className="text-2xl font-bold mb-2">Office Janitorial</h3>
                        <p className="text-gray-300 text-sm">Nightly cleaning for professional workspaces.</p>
                    </div>
                </Link>

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

      {/* 5. CTA SECTION */}
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

    # --- 2. Re-assert the Hook exists (Just in case) ---
    "src/hooks/useCity.js": """
'use client';
import { useState, useEffect } from 'react';

export function useCity() {
  const [city, setCity] = useState('Toronto'); 

  useEffect(() => {
    // Check URL params for ?city=X
    if (typeof window !== 'undefined') {
        const params = new URLSearchParams(window.location.search);
        if (params.get('city')) {
            setCity(params.get('city'));
        }
    }
  }, []);

  return city;
}
"""
}

def fix_import():
    print("🚀 Fixing Import Path Error...")

    for file_path, content in project_files.items():
        # Ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Write file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        
        print(f"✅ Updated: {file_path}")

    print("\n🎉 Fixed! The '@' alias has been replaced with standard relative paths.")

if __name__ == "__main__":
    fix_import()
