-- Run this in your Neon SQL Editor to create the table
CREATE TABLE leads (
  id SERIAL PRIMARY KEY,
  company_name TEXT,
  contact_name TEXT NOT NULL,
  email TEXT NOT NULL,
  phone TEXT NOT NULL,
  service_type TEXT NOT NULL, -- 'construction', 'commercial', 'airbnb'
  details JSONB,
  status TEXT DEFAULT 'new', -- 'new', 'contacted', 'contract_signed'
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);