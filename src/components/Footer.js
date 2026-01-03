import Link from 'next/link';

export default function Footer() {
  const currentYear = new Date().getFullYear();
  const cities = ['Toronto', 'Mississauga', 'Brampton', 'Vaughan', 'Markham', 'Etobicoke'];

  return (
    <footer className="bg-elite-900 text-white pt-16 pb-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
          <div>
            <h3 className="text-2xl font-bold mb-4">Elite Clean Group</h3>
            <p className="text-gray-300 mb-6">Setting the standard for commercial and post-construction sanitation in the GTA.</p>
            <div className="text-gray-300">
              <p>Email: contracts@elitecleangroup.com</p>
              <p>Phone: (416) 555-0123</p>
            </div>
          </div>
          <div>
            <h4 className="text-lg font-bold mb-4 text-elite-500">Services</h4>
            <ul className="space-y-2">
              <li><Link href="/construction-cleanup" className="hover:text-white text-gray-400">Construction Cleanup</Link></li>
              <li><Link href="/commercial-janitorial" className="hover:text-white text-gray-400">Office Janitorial</Link></li>
              <li><Link href="/airbnb-turnover" className="hover:text-white text-gray-400">Airbnb Management</Link></li>
            </ul>
          </div>
          <div>
            <h4 className="text-lg font-bold mb-4 text-elite-500">Service Area</h4>
            <ul className="grid grid-cols-2 gap-2">
              {cities.map(city => (
                <li key={city}><Link href="#" className="text-sm text-gray-400 hover:text-white">{city}</Link></li>
              ))}
            </ul>
          </div>
          <div>
            <h4 className="text-lg font-bold mb-4 text-elite-500">Business Hours</h4>
            <p className="text-gray-400 mb-2">Mon-Fri: 7am - 8pm</p>
            <Link href="/quote" className="inline-block bg-white text-elite-900 font-bold py-2 px-6 rounded hover:bg-gray-100 transition">Get Quote</Link>
          </div>
        </div>
        <div className="border-t border-gray-800 pt-8 text-center text-gray-500 text-sm">
          <p>&copy; {currentYear} Elite Clean Group. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
}