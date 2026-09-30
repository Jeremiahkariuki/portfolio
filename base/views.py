from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def contacts(request):
    return render(request, 'base/contacts.html')

def projects(request):
    projects_list = [
        {
            "title": "Property Management & Rental Platform",
            "description": "Full SaaS property management platform for landlords, agents, and tenants. "
                           "Tenant records, rental history, maintenance requests, M-Pesa payments, invoice generation, "
                           "payment tracking, tenant ledgers, automated rent reminders, utility meter readings, and public property listings.",
            "built_with": ["Python", "Django", "Django REST Framework", "PostgreSQL", "M-Pesa API"],
            "github": "",
            "live": "https://pyostay.com",
            "status": "Live",
        },
        {
            "title": "Security Solutions & Services Website",
            "description": "Responsive corporate website for a security company offering electric gates, gate automation, "
                           "CCTV systems, and access-control services. Structured service discovery, responsive layouts, "
                           "contact/lead-generation, performance, responsiveness, SEO, and cross-device compatibility.",
            "built_with": ["React.js", "TypeScript", "Node.js", "PostgreSQL", "Git", "Docker", "DigitalOcean"],
            "github": "",
            "live": "https://jksecurityservices.co.ke",
            "status": "Live",
        },
        {
            "title": "Transport & Logistics Management Website",
            "description": "Responsive transport and logistics platform for cargo transportation from Nairobi to all 47 counties. "
                           "Service discovery, shipment booking, cargo tracking, fleet/service presentation, customer inquiries, "
                           "and delivery workflow interfaces. Mobile-first UX for quote requests and shipment scheduling.",
            "built_with": ["React.js", "TypeScript", "Node.js", "PostgreSQL", "Docker", "Git", "DigitalOcean"],
            "github": "",
            "live": "",
            "status": "Live",
        },
        {
            "title": "JK Security ERP (Odoo 17)",
            "description": "Full-stack ERP built on Odoo 17 for security companies in Kenya. 12 custom modules: "
                           "Guards Management, Shift Scheduling, HR Recruitment, Payroll (PAYE & tax), Incident Reports, "
                           "Complaint Management, PDF reports via QWeb, and role-based access with 8 user groups.",
            "built_with": ["Python", "Odoo 17", "XML", "PostgreSQL", "QWeb"],
            "github": "https://github.com/Sikarjb/security-services",
            "live": "",
        },
        {
            "title": "jdiary — Personal Productivity Platform",
            "description": "Personal productivity and reflection platform with diary entries, task management, and event scheduling. "
                           "DRF API endpoints, mood-tracking algorithm with user streaks, automated PDF export (xhtml2pdf), "
                           "glassmorphism UI, deployed on Render with PostgreSQL and full CI/CD via GitHub.",
            "built_with": ["Python", "Django", "DRF", "PostgreSQL", "xhtml2pdf", "Render", "GitHub Actions"],
            "github": "",
            "live": "",
        },
        {
            "title": "Gym Management System",
            "description": "Django system with admin, cashier, and client roles. Membership plans, payments, "
                           "role-based dashboards, and automated notifications.",
            "built_with": ["Python", "Django", "SQLite"],
            "github": "https://github.com/Sikarjb/gym-website",
            "live": "",
        },
        {
            "title": "Future Me — Letter Scheduler",
            "description": "Web application that allows users to write letters to their future selves and schedule delivery via email.",
            "built_with": ["Django", "Email Integration", "SQLite"],
            "github": "https://github.com/Dennismwangi-k/futureme",
            "live": "",
        },
        {
            "title": "Bwada Football Club",
            "description": "Modern recruitment marketplace connecting employers with job seekers. "
                           "Job posting, applicant tracking, and employer management features.",
            "built_with": ["Python", "Django", "HTML", "CSS"],
            "github": "",
            "live": "",
        },
        {
            "title": "Portfolio Website",
            "description": "My personal developer portfolio built with Django and deployed on Render.",
            "built_with": ["Django", "HTML", "CSS", "Render"],
            "github": "https://github.com/Sikarjb/personal-website",
            "live": "https://personal-website-1-p148.onrender.com",
        },
    ]

    return render(request, "base/projects.html", {"projects": projects_list})