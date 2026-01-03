/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        elite: {
          50: '#f0fdf4',
          100: '#dcfce7',
          500: '#22c55e',
          800: '#064e3b',
          900: '#003B2B', // Brand Deep Green
        },
        safety: {
          500: '#ff5e00', // Construction Orange
          600: '#cc4b00',
        }
      },
    },
  },
  plugins: [],
}