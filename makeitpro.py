import os

project_files = {
    # --- 1. UTILS (City Detection) ---
    "src/hooks/useCity.js": """
'use client';
import { useState, useEffect } from 'react';

export function useCity() {
  const [city, setCity] = useState('Toronto'); // Default

  useEffect(() => {
    // In a real app, you would use an API like ipinfo.io or Vercel Headers
    // For now, we simulate "Toronto" or allow URL override ?city=Mississauga
    const params = new URLSearchParams(window.location.search);
    if (params.get('city')) {
      setCity(params.get('city'));
    }
  }, []);

  return city;
}
""",

    # --- 2. LAYOUT (Adds "Top Bar" with Phone Number) ---
    "src/app/layout.js": """
import './globals.css';
import { Inter } from 'next/font/google';

const inter = Inter({ subsets: ['latin'] });

export const metadata = {
  title: 'Elite Clean Group',
  description: 'Professional Commercial & Residential Cleaning',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        {/* TOP BAR - Trust Signal */}
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
              <div className="text-2xl font-extrabold text-blue-900 tracking-tight">
                ELITE<span className="text-blue-600">CLEAN</span>
              </div>
              <div className="hidden md:flex space-x-8 text-sm font-medium text-gray-700">
                <a href="/commercial-janitorial" className="hover:text-blue-600">Commercial</a>
                <a href="/construction-cleanup" className="hover:text-blue-600">Construction</a>
                <a href="/airbnb-turnover" className="hover:text-blue-600">Airbnb</a>
              </div>
              <div>
                <a href="/quote" className="bg-blue-600 text-white px-5 py-2.5 rounded-full text-sm font-bold shadow-lg hover:bg-blue-700 transition transform hover:-translate-y-0.5">
                  Get Quote
                </a>
              </div>
            </div>
          </div>
        </nav>

        {children}
        
        {/* FOOTER */}
        <footer className="bg-gray-900 text-gray-400 py-12">
            <div className="max-w-7xl mx-auto px-6 grid md:grid-cols-4 gap-8">
                <div>
                    <h3 className="text-white font-bold mb-4">ELITE CLEAN GROUP</h3>
                    <p className="text-sm">Professional cleaning standards for businesses that care about first impressions.</p>
                </div>
                <div>
                    <h4 className="text-white font-bold mb-4">Services</h4>
                    <ul className="space-y-2 text-sm">
                        <li><a href="/commercial-janitorial">Janitorial Services</a></li>
                        <li><a href="/construction-cleanup">Post-Construction</a></li>
                        <li><a href="/airbnb-turnover">Airbnb Turnover</a></li>
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
                    <p className="text-sm">hello@elitecleangroup.com</p>
                    <p className="text-white font-bold mt-2">(416) 555-0199</p>
                </div>
            </div>
        </footer>
      </body>
    </html>
  );
}
""",

    # --- 3. HOME PAGE (Heavy Content + Dynamic City) ---
    "src/app/page.js": """
'use client';
import Link from 'next/link';
import { useCity } from '@/hooks/useCity';

export default function Home() {
  const city = useCity();

  return (
    <main className="flex min-h-screen flex-col">
      
      {/* 1. HERO SECTION - Darker, Professional, Dynamic */}
      <section className="relative bg-gray-900 text-white py-32 px-6">
        {/* Background Image Overlay */}
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

      {/* 2. TRUST SIGNALS (The 'Not Empty' Factor) */}
      <section className="py-10 border-b bg-gray-50">
        <div className="max-w-7xl mx-auto px-6 text-center">
            <p className="text-sm font-bold text-gray-400 uppercase tracking-widest mb-6">Trusted by businesses in {city}</p>
            <div className="flex flex-wrap justify-center gap-8 md:gap-16 opacity-50 grayscale">
                {/* Placeholders for logos - Text for now */}
                <span className="text-2xl font-bold text-gray-600">RE/MAX</span>
                <span className="text-2xl font-bold text-gray-600">Scotiabank</span>
                <span className="text-2xl font-bold text-gray-600">WeWork</span>
                <span className="text-2xl font-bold text-gray-600">EllisDon</span>
            </div>
        </div>
      </section>

      {/* 3. VALUE PROPS (Why Us?) */}
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

      {/* 4. SERVICES GRID (Visuals) */}
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
                {/* Card 1 */}
                <Link href="/airbnb-turnover" className="group block relative h-80 rounded-2xl overflow-hidden hover:ring-4 ring-blue-600 transition">
                    <img src="https://images.unsplash.com/photo-1556911220-bff31c812dba?auto=format&fit=crop&q=80" className="absolute inset-0 w-full h-full object-cover transition duration-500 group-hover:scale-110" />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/90 to-transparent"></div>
                    <div className="absolute bottom-0 p-8">
                        <h3 className="text-2xl font-bold mb-2">Airbnb Turnover</h3>
                        <p className="text-gray-300 text-sm">Automated scheduling for your short-term rentals.</p>
                    </div>
                </Link>

                 {/* Card 2 */}
                <Link href="/commercial-janitorial" className="group block relative h-80 rounded-2xl overflow-hidden hover:ring-4 ring-blue-600 transition">
                    <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80" className="absolute inset-0 w-full h-full object-cover transition duration-500 group-hover:scale-110" />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/90 to-transparent"></div>
                    <div className="absolute bottom-0 p-8">
                        <h3 className="text-2xl font-bold mb-2">Office Janitorial</h3>
                        <p className="text-gray-300 text-sm">Nightly cleaning for professional workspaces.</p>
                    </div>
                </Link>

                 {/* Card 3 */}
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
"""
}

def make_it_pro():
    print("🚀 Injecting 'Pro' Design & Dynamic City Logic...")

    for file_path, content in project_files.items():
        # Ensure directory exists (hooks folder)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Write file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        
        print(f"✅ Updated: {file_path}")

    print("\n🎉 Upgrade Complete!")
    print("1. Restart server: 'npm run dev'")
    print("2. Check the default: http://localhost:3002")
    print("3. Test City Logic: http://localhost:3002/?city=Mississauga")

if __name__ == "__main__":
    make_it_pro()
