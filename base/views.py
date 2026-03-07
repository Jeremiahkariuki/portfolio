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
            "title": "Gym management system",
            "description": "A Django system with admin, cashier, client roles, membership plans and payments.",
            "built_with": ["Python", "Django", "SQLite"],
            "github": "https://github.com/Sikarjb/gym-website",
            "status": "Pending",
        },
        {
            "title": "Portfolio website",
            "description": "My personal portfolio built with Django and deployed on Render.",
            "built_with": ["Django", "HTML", "CSS"],
            "github": "https://github.com/Sikarjb/personal-website",
            "live": "https://personal-website-1-p148.onrender.com",
        },
        {
            "title": "Future Me Website",
            "description": "A web application that allows users to write letters to their future selves and schedule via email.",
            "built_with": ["Django", "Email Integration", "SQLite"],
            "github": "https://github.com/Dennismwangi-k/futureme",
            "live": "",
        },
    ]

    return render(request, "base/projects.html", {"projects": projects_list})