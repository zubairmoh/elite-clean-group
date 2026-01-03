'use client';
import { useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);
  const pathname = usePathname();

  const navLinks = [
    { name: 'Commercial', href: '/commercial-janitorial' },
    { name: 'Construction', href: '/construction-cleanup' },
    { name: 'Airbnb', href: '/airbnb-turnover' },
  ];

  return (
    <nav className="bg-white shadow-md sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-20">
          <div className="flex-shrink-0 flex items-center">
            <Link href="/" className="flex items-center gap-2">
              <div className="relative h-12 w-48">
                 {/* Ensure logo.webp is in public folder */}
                 <span className="text-2xl font-bold text-elite-900">Elite<span className="text-elite-500">Clean</span></span>
              </div>
            </Link>
          </div>
          <div className="hidden md:flex items-center space-x-8">
            {navLinks.map((link) => (
              <Link key={link.name} href={link.href} className={`text-sm font-bold uppercase tracking-wide hover:text-elite-500 transition ${pathname === link.href ? 'text-elite-900' : 'text-gray-600'}`}>
                {link.name}
              </Link>
            ))}
          </div>
          <div className="hidden md:flex items-center gap-4">
             <a href="tel:+14165550123" className="flex flex-col items-end group">
              <span className="text-xs text-gray-500 font-medium">24/7 Service</span>
              <span className="text-lg font-bold text-elite-900 group-hover:text-elite-500 transition">(416) 555-0123</span>
            </a>
            <Link href="/quote" className="bg-elite-900 text-white px-6 py-3 rounded-md font-bold hover:bg-elite-800 transition shadow-lg">Get a Bid</Link>
          </div>
          <div className="flex items-center md:hidden">
            <button onClick={() => setIsOpen(!isOpen)} className="text-gray-700 hover:text-elite-900 focus:outline-none">
              Menu
            </button>
          </div>
        </div>
      </div>
      {isOpen && (
        <div className="md:hidden bg-white border-t border-gray-100">
          <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
            {navLinks.map((link) => (
              <Link key={link.name} href={link.href} onClick={() => setIsOpen(false)} className="block px-3 py-4 rounded-md text-base font-medium text-gray-700 hover:bg-gray-50">
                {link.name}
              </Link>
            ))}
            <Link href="/quote" onClick={() => setIsOpen(false)} className="block px-3 py-4 mt-4 text-center rounded-md text-base font-bold bg-elite-900 text-white">Get a Free Quote</Link>
          </div>
        </div>
      )}
    </nav>
  );
}