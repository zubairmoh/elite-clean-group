"use client"; // This allows the hamburger button to work

import { useState } from 'react';
import Link from 'next/link';

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="border-b sticky top-0 bg-white/95 backdrop-blur z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16 items-center">
          
          {/* LOGO */}
          <Link href="/" className="cursor-pointer relative z-50 block group">
            <span className="text-2xl font-extrabold text-blue-900 tracking-tight group-hover:opacity-75 transition">
              ELITE<span className="text-blue-600">CLEAN</span>
            </span>
          </Link>

          {/* DESKTOP MENU (Hidden on Mobile) */}
          <div className="hidden md:flex space-x-8 text-sm font-medium text-gray-700">
            <Link href="/commercial-janitorial" className="hover:text-blue-600 py-2 transition">Commercial</Link>
            <Link href="/construction-cleanup" className="hover:text-blue-600 py-2 transition">Construction</Link>
            <Link href="/airbnb-turnover" className="hover:text-blue-600 py-2 transition">Airbnb</Link>
          </div>

          {/* GET QUOTE BUTTON (Desktop) */}
          <div className="hidden md:block">
            <Link href="/quote" className="bg-blue-600 text-white px-5 py-2.5 rounded-full text-sm font-bold shadow-lg hover:bg-blue-700 transition transform hover:-translate-y-0.5">
              Get Quote
            </Link>
          </div>

          {/* MOBILE MENU BUTTON (Hamburger) */}
          <div className="-mr-2 flex items-center md:hidden">
            <button
              onClick={() => setIsOpen(!isOpen)}
              type="button"
              className="inline-flex items-center justify-center p-2 rounded-md text-gray-700 hover:text-blue-600 focus:outline-none"
            >
              <span className="sr-only">Open main menu</span>
              {!isOpen ? (
                // Hamburger Icon
                <svg className="block h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16" />
                </svg>
              ) : (
                // X Icon
                <svg className="block h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              )}
            </button>
          </div>
        </div>
      </div>

      {/* MOBILE MENU DROPDOWN (Only shows when clicked) */}
      {isOpen && (
        <div className="md:hidden bg-white border-t">
          <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
            <Link href="/commercial-janitorial" className="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-50">Commercial</Link>
            <Link href="/construction-cleanup" className="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-50">Construction</Link>
            <Link href="/airbnb-turnover" className="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-50">Airbnb</Link>
            <Link href="/quote" className="block px-3 py-2 mt-4 text-center rounded-md text-base font-bold bg-blue-600 text-white hover:bg-blue-700">Get Quote</Link>
          </div>
        </div>
      )}
    </nav>
  );
}
