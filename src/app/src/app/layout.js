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