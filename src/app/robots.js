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