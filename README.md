# Shivam Construction Company Website

A professional Django-based website for Shivam Construction Company showcasing company information, services, projects, equipment, and team.

## Features

- **Home Page**: Introduction and overview of the company
- **About Page**: Company vision, quality policy, and key personnel
- **Services Page**: Comprehensive list of services offered
- **Projects Page**: Completed projects and experience
- **Equipment Page**: Available machinery and equipment
- **Team Page**: Organization structure and human resources
- **Contact Page**: Contact information and inquiry form

## Installation

1. **Activate Virtual Environment**
   ```bash
   source venv/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   pip install django
   ```

3. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

4. **Load Initial Data**
   ```bash
   python manage.py load_initial_data
   ```

5. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Website**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Project Structure

```
shivam_construction_companey/
├── shivam/                    # Main Django app
│   ├── models.py             # Database models
│   ├── views.py              # View functions
│   ├── urls.py               # URL routing
│   ├── admin.py              # Admin configuration
│   └── management/           # Management commands
│       └── commands/
│           └── load_initial_data.py
├── templates/                 # HTML templates
│   └── shivam/
│       ├── base.html
│       ├── home.html
│       ├── about.html
│       ├── services.html
│       ├── projects.html
│       ├── equipment.html
│       ├── team.html
│       └── contact.html
├── static/                    # Static files
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── shivam_construction/       # Project settings
    ├── settings.py
    └── urls.py
```

## Models

- **CompanyInfo**: Company information and details
- **KeyPerson**: Key personnel and their roles
- **Service**: Services offered by the company
- **CompletedProject**: Completed projects and experience
- **Equipment**: Available equipment and machinery
- **Staff**: Staff members and organization structure

## Admin Panel

Access the admin panel at `/admin/` to:
- Manage company information
- Add/edit key persons
- Manage services
- Add completed projects
- Update equipment list
- Manage staff information

## Customization

### Adding Content

1. **Via Admin Panel**: Login to admin and add content through the interface
2. **Via Management Command**: Run `python manage.py load_initial_data` to reload default data

### Styling

- Main stylesheet: `static/css/style.css`
- Color scheme matches company branding (Yellow, Red, Blue)
- Responsive design for mobile and desktop

### Adding New Pages

1. Create view in `shivam/views.py`
2. Add URL pattern in `shivam/urls.py`
3. Create template in `templates/shivam/`
4. Add navigation link in `templates/shivam/base.html`

## Contact Information

- **Phone**: 6350092193
- **Email**: scccompany91@gmail.com
- **Address**: BUILDING NO./FLAT NO.: MEEL COLONY KE SAMANE, ROAD/STREET: WARD NO. 03 NEW, CITY/TOWN/VILLAGE: SURATGARH, DISTRICT: SRI GANGANAGAR, STATE: RAJASTHAN, PIN CODE: 335804

## Technologies Used

- Django 6.0.1
- Python 3.12
- HTML5/CSS3
- JavaScript
- SQLite (default database)

## License

This project is proprietary software for Shivam Construction Company.

# shivam-solar-companey
