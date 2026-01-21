# Elite Clean Group

A modern, professional website for Elite Clean Group - a commercial cleaning company serving the Greater Toronto Area.

## Tech Stack

- **Framework**: Next.js 16 (App Router)
- **Styling**: Tailwind CSS
- **Database**: Neon PostgreSQL (serverless)
- **Deployment**: Render.com

## Features

- Responsive design optimized for all devices
- Service pages for Commercial Janitorial, Post-Construction Cleanup, and Airbnb Turnover
- Quote request form with email notifications
- Admin dashboard for lead management
- SEO optimized with sitemap and robots.txt

## Getting Started

### Prerequisites

- Node.js 18+
- npm or yarn

### Installation

```bash
# Clone the repository
git clone https://github.com/zubairmoh/elite-clean-group.git
cd elite-clean-group

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env.local
# Edit .env.local with your database and email credentials

# Run the development server
npm run dev
```

### Environment Variables

Create a `.env.local` file with the following variables:

```
DATABASE_URL=your_neon_database_url
ADMIN_PASSWORD=your_secure_admin_password
SMTP_HOST=your_smtp_host
SMTP_PORT=587
SMTP_USER=your_email
SMTP_PASS=your_email_password
NOTIFICATION_EMAIL=where_to_send_notifications
```

## Project Structure

```
src/
├── app/
│   ├── api/           # API routes
│   ├── about/         # About page
│   ├── admin/         # Admin dashboard
│   ├── airbnb-turnover/
│   ├── commercial-janitorial/
│   ├── construction-cleanup/
│   ├── contact/       # Contact page
│   ├── login/         # Admin login
│   └── quote/         # Quote request form
├── components/        # Reusable components
├── hooks/             # Custom React hooks
└── lib/               # Utilities (db, email)
```

## Deployment

The site is configured for deployment on Render.com. See `render.yaml` for configuration.

## License

Private - All rights reserved.
