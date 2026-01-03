import os

debug_layout = """
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
        {/* TOP BAR */}
        <div className="bg-blue-900 text-white text-xs py-2 px-4 flex justify-between items-center relative z-40">
          <div className="hidden md:flex space-x-4">
             <span>📍 Serving Greater Toronto Area</span>
             <span>🏆 WSIB Insured & Bonded</span>
          </div>
          <div className="flex space-x-4 font-bold">
             <a href="tel:416-555-0199">📞 (416) 555-0199</a>
          </div>
        </div>

        {/* NAV - Added z-[9999] to force it to the very top */}
        <nav className="border-b sticky top-0 bg-white z-[9999]">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16 items-center">
              
              {/* --- DEBUGGING LOGO --- 
                  1. Using standard <a> tag
                  2. RED BORDER to verify hit-box
                  3. cursor-pointer explicitly set
              */}
              <a href="/" className="cursor-pointer border-4 border-red-600 relative z-[9999] block p-2">
                <span className="text-2xl font-extrabold text-blue-900 tracking-tight">
                  ELITE<span className="text-blue-600">CLEAN</span>
                </span>
              </a>
              {/* ---------------------- */}

              <div className="hidden md:flex space-x-8 text-sm font-medium text-gray-700">
                <a href="/commercial-janitorial" className="hover:text-blue-600 py-2">Commercial</a>
                <a href="/construction-cleanup" className="hover:text-blue-600 py-2">Construction</a>
                <a href="/airbnb-turnover" className="hover:text-blue-600 py-2">Airbnb</a>
              </div>
              <div>
                <a href="/quote" className="bg-blue-600 text-white px-5 py-2.5 rounded-full text-sm font-bold shadow-lg hover:bg-blue-700 transition">
                  Get Quote
                </a>
              </div>
            </div>
          </div>
        </nav>

        {children}
        
      </body>
    </html>
  );
}
"""

def apply_debug():
    print("🐞 Applying RED BORDER DEBUG Mode...")
    
    # Force overwrite
    path = "src/app/layout.js"
    with open(path, "w", encoding="utf-8") as f:
        f.write(debug_layout.strip())
    
    print(f"✅ Updated {path}")
    print("👉 RESTART SERVER (npm run dev) and look for the RED BOX around the logo.")

if __name__ == "__main__":
    apply_debug()
