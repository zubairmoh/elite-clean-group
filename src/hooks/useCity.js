'use client';
import { useState, useEffect } from 'react';

export function useCity() {
  const [city, setCity] = useState('Toronto'); // Default

  useEffect(() => {
    // In a real app, you would use an API like ipinfo.io or Vercel Headers
    // For now, we simulate "Toronto" or allow URL override ?city=Mississauga
    const params = new URLSearchParams(window.location.search);
    if (params.get('city')) {
      setCity(params.get('city'));
    }
  }, []);

  return city;
}