import os

seo_files = {
    # --- 1. SITEMAP (The Map for Google) ---
    "src/app/sitemap.js": """
export default function sitemap() {
  const baseUrl = 'https://elitecleangroup.com'; // Replace with your real domain later

  return [
    {
      url: baseUrl,
      lastModified: new Date(),
      changeFrequency: 'yearly',
      priority: 1,
    },
    {
      url: `${baseUrl}/commercial-janitorial`,
      lastModified: new Date(),
      changeFrequency: 'monthly',
      priority: 0.8,
    },
    {
      url: `${baseUrl}/construction-cleanup`,
      lastModified: new Date(),
      changeFrequency: 'monthly',
      priority: 0.8,
    },
    {
      url: `${baseUrl}/airbnb-turnover`,
      lastModified: new Date(),
      changeFrequency: 'weekly',
      priority: 0.8,
    },
    {
      url: `${baseUrl}/quote`,
      lastModified: new Date(),
      changeFrequency: 'yearly',
      priority: 0.5,
    },
  ];
}
""",

    # --- 2. ROBOTS.TXT (The Rules for Bots) ---
    "src/app/robots.js": """
export default function robots() {
  return {
    rules: {
      userAgent: '*',
      allow: '/',
      disallow: '/admin/', // Don't let Google index your admin panel!
    },
    sitemap: 'https://elitecleangroup.com/sitemap.xml',
  };
}
""",

    # --- 3. MANIFEST (Mobile SEO & Branding) ---
    "src/app/manifest.js": """
export default function manifest() {
  return {
    name: 'Elite Clean Group',
    short_name: 'EliteClean',
    description: 'Professional Commercial & Residential Cleaning Services',
    start_url: '/',
    display: 'standalone',
    background_color: '#fff',
    theme_color: '#1e3a8a', // Your brand blue
    icons: [
      {
        src: '/favicon.ico',
        sizes: 'any',
        type: 'image/x-icon',
      },
    ],
  };
}
"""
}

def make_seo_technical():
    print("🚀 Generating Technical SEO Files (Sitemap, Robots, Manifest)...")
    
    for path, content in seo_files.items():
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"✅ Created: {path}")

    print("\n🎉 Technical SEO Complete!")
    print("👉 When you deploy, Google will now automatically find 'sitemap.xml' and 'robots.txt'.")
    print("👉 IMPORTANT: Before you launch for real, change 'https://elitecleangroup.com' in sitemap.js to your actual domain.")

if __name__ == "__main__":
    make_seo_technical()
