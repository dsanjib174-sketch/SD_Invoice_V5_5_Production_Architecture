# SD Invoice V5.5 Production Architecture

This is a production architecture package for rebuilding SD Invoice in a stable, modular way.

This package is not a full final ERP product. It is the proper project foundation and architecture to build the production version module by module.

## Main Goals

- Stable PostgreSQL database
- Professional login and branding
- Superadmin SaaS control
- Client/company profile
- Branch/user limits by plan
- Invoice, quotation, proforma and credit note workflow
- Professional GST invoice format
- Client analytics dashboard
- Superadmin analytics dashboard
- Demo client data isolation
- GST, Tally and SAP export-ready reports
- WhatsApp and email communication module
- Audit logging

## Recommended Tech Stack

- Backend: Python Flask
- Database: PostgreSQL
- ORM: SQLAlchemy
- Migrations: Alembic
- Frontend: Jinja templates + Bootstrap/Tailwind style CSS
- PDF: WeasyPrint or Playwright PDF
- Deployment: Render/Railway/AWS/DigitalOcean
- Static Files: local for testing, S3/Cloudinary for production
- Email: SMTP
- WhatsApp: Meta Cloud API / approved provider

## Default Login Flow

Client:
- Login page: `/`
- Client enters email
- Branch dropdown loads automatically
- Then user ID and password

Superadmin:
- Login page: `/admin`
- Superadmin controls clients, plans, updates and analytics

## Important Rule

Demo client data must not appear in Superadmin ledger, GST, Tally, SAP or production analytics.
Demo client data should remain only inside demo account. Audit logs remain global.
