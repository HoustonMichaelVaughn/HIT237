HIT237
A HIT237 django website. Here is how the directory is setup!

```
mango_pests_project/                    # Django Project Root
│   db.sqlite3
│   manage.py
│   README.md
│
├───mango_pests/                        # Django App
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   urls.py
│   │   views.py
│   │   data.py                         # The custom Python class for pests/diseases
│   │   tests.py
│   │   __init__.py
│   │
│   ├───migrations/
│   │   └───__pycache__/
│   │
│   ├───templates/
│   │   └───mango_pests/
│   │       │   base.html               # Base template for navigation
│   │       │   home.html               # Introduction
│   │       │   project_list.html       # List of pests/diseases
│   │       │   project_detail.html     # Pest/disease details
│   │       │   about.html              # Team details
│   │
│   ├───static/
│   │   ├───css/
│   │   │   └───style.css               # Temporary CSS (I don't know if we need any)
│   │   ├───images/                     # Images for pests/diseases
│   │   └───js/
│   │       └───script.js               # JavaScript (Possibly needed)
│   │
│   └───__pycache__/
│
└───mango_pests_project/                 # Django Project Settings
    │   asgi.py
    │   settings.py
    │   urls.py
    │   wsgi.py
    │   __init__.py
    │
    └───__pycache__/
```

