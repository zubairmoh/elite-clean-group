import './globals.css';
import { Inter } from 'next/font/google';
import Navbar from '../components/Navbar'; // Using the standard @ alias

const inter = Inter({ subsets: ['latin'] });

export const metadata = {
  title: 'Elite Clean Group',
  description: 'Professional Commercial & Residential Cleaning',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        
        {/* TOP BAR - Info Strip */}
        <div className="bg-blue-900 text-white text-xs py-2 px-4 flex justify-between items-center relative z-50">
          <div className="hidden md:flex space-x-4">
             <span>📍 Serving Greater Toronto Area</span>
             <span>🏆 WSIB Insured & Bonded</span>
          </div>
          <div className="flex space-x-4 font-bold">
             <a href="tel:416-555-0199">📞 (416) 555-0199</a>
          </div>
        </div>

        {/* NAVIGATION COMPONENT */}
        <Navbar />

        {/* MAIN CONTENT */}
        {children}
        
        {/* FOOTER */}
        <footer className="bg-gray-900 text-gray-400 py-12 border-t border-gray-800">
            <div className="max-w-7xl mx-auto px-6 text-center">
                <p className="text-sm">© 2026 Elite Clean Group. All rights reserved.</p>
            </div>
        </footer>

      </body>
    </html>
  );
}
