import Link from 'next/link';

export const metadata = { title: 'Airbnb Turnover | Elite Clean Group' };

export default function AirbnbPage() {
  return (
    <main className="min-h-screen bg-white">
      <section className="relative h-[60vh] flex items-center justify-center bg-gray-900 text-white">
        <div className="absolute inset-0 overflow-hidden">
          <img src="https://images.unsplash.com/photo-1556911220-bff31c812dba?auto=format&fit=crop&q=80" className="w-full h-full object-cover opacity-30" alt="Airbnb" />
        </div>
        <div className="relative z-10 text-center max-w-4xl px-4">
          <span className="text-blue-400 font-bold tracking-widest uppercase text-sm mb-4 block">For Superhosts</span>
          <h1 className="text-5xl md:text-6xl font-bold mb-6">Automated Turnover</h1>
          <p className="text-xl text-gray-300 mb-8">Hotel-quality cleaning, linen service, and damage reporting.</p>
          <Link href="/quote?service=airbnb" className="bg-blue-600 text-white px-8 py-3 rounded font-bold hover:bg-blue-500">Get Pricing</Link>
        </div>
      </section>

      <section className="py-20 px-6 max-w-7xl mx-auto grid md:grid-cols-2 gap-12 items-center">
        <div>
           <h2 className="text-3xl font-bold text-gray-900 mb-6">Don't lose your Superhost status.</h2>
           <p className="text-gray-600 text-lg mb-6">Managing multiple properties is stressful. We integrate with your booking calendar (Airbnb, VRBO, Guesty) to ensure your unit is ready 100% of the time.</p>
           
           <div className="space-y-6">
                <div className="flex gap-4">
                    <div className="text-2xl">📸</div>
                    <div><h4 className="font-bold text-gray-900">Photo Evidence</h4><p className="text-sm text-gray-600">We send photos after every clean so you know it's ready.</p></div>
                </div>
                <div className="flex gap-4">
                    <div className="text-2xl">🧺</div>
                    <div><h4 className="font-bold text-gray-900">Linen Service</h4><p className="text-sm text-gray-600">We wash linens on-site or off-site depending on your unit.</p></div>
                </div>
                <div className="flex gap-4">
                    <div className="text-2xl">🧴</div>
                    <div><h4 className="font-bold text-gray-900">Restocking</h4><p className="text-sm text-gray-600">We replenish coffee, toilet paper, and soap.</p></div>
                </div>
           </div>
        </div>
        <div className="bg-gray-100 p-8 rounded-2xl border">
            <h3 className="font-bold text-xl mb-4">Our Standard Checklist</h3>
            <div className="space-y-3 text-sm text-gray-600">
                <div className="flex justify-between border-b border-gray-300 pb-2"><span>Change Linens & Towels</span> <span>✅</span></div>
                <div className="flex justify-between border-b border-gray-300 pb-2"><span>Sanitize Kitchen & Bath</span> <span>✅</span></div>
                <div className="flex justify-between border-b border-gray-300 pb-2"><span>Check Under Beds/Sofas</span> <span>✅</span></div>
                <div className="flex justify-between border-b border-gray-300 pb-2"><span>Empty Fridge & Trash</span> <span>✅</span></div>
                <div className="flex justify-between border-b border-gray-300 pb-2"><span>Report Damages</span> <span>✅</span></div>
                <div className="flex justify-between border-b border-gray-300 pb-2"><span>Arrange Welcome Gift</span> <span>Optional</span></div>
            </div>
        </div>
      </section>
    </main>
  );
}