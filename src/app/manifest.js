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