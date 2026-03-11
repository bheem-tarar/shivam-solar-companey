from django.core.management.base import BaseCommand
from shivam.models import CompanyInfo, KeyPerson, Service, CompletedProject, Equipment, Staff

class Command(BaseCommand):
    help = 'Load initial data for Shivam Construction Company'

    def handle(self, *args, **options):
        # Company Info
        company, created = CompanyInfo.objects.get_or_create(
            name="Shivam Construction Company",
            defaults={
                'tagline': 'Civil Contractor & General Order Suppliers',
                'phone': '6350092193',
                'email': 'scccompany91@gmail.com',
                'address': 'SHOP NO. 05, NEAR INDANE GAS OFFICE, BASANT VIHAR COLONY, SURATGARH, SRI GANGANAGAR, RAJASTHAN, 335804',
                'introduction': 'Shivam Construction Company is engaged in large format earthworks, cross-country piping, irrigation works, industrial plant buildings, commercial and IT spaces, plant fabrication and erection (especially in power, petrochemical, and pharmaceutical areas).',
                'vision': 'To become a leading professional one solution engineering consultancy, Construction organization and asset builder in large format earth works, Industrial plant construction and commercial building construction with best national & international quality standards.',
                'quality_policy': 'Our policy at SCC is to exceed the customer expectations by understanding their needs and delivering them with specified quality, within agreed time by becoming their trusted partners through constant interaction and continuous improvement by enabling a positive and creative environment.'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Company info created'))
        else:
            self.stdout.write(self.style.SUCCESS('Company info already exists'))

        # Key Persons
        key_persons_data = [
            {
                'name': 'Mr. V. K. Choudhary',
                'role': 'Managing Director',
                'description': 'A natural entrepreneur with excellent experience in large format Earth works, Cross country Pipe lines, road works, etc. He hails from a business family with enormous experience in project implementation.',
                'order': 1
            },
            {
                'name': 'Mr. Praveen Acharya',
                'role': 'Director',
                'description': 'A Post graduate in Arts. After acquiring working experience in reputed organizations, he has been inducted into the board of Directors and took over the responsibility for Finance and accounting.',
                'order': 2
            },
            {
                'name': 'Mr. Rakesh Kumar',
                'role': 'Director',
                'description': 'A Post graduate in Arts. After acquiring working experience in reputed organizations, he has been inducted into the board of Directors and took over the responsibility of HR and Admn.',
                'order': 3
            },
            {
                'name': 'Mr. Chanderkant',
                'role': 'Technical Advisor',
                'description': 'A highly knowledgeable and successful project professional who proved himself by independently executing large power plant projects. His background with KC Group, BHEL, is mentioned as taking the company to new heights.',
                'order': 4
            }
        ]

        for person_data in key_persons_data:
            person, created = KeyPerson.objects.get_or_create(
                name=person_data['name'],
                defaults=person_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created key person: {person_data["name"]}'))

        # Services
        services_data = [
            # Industrial and Commercial Buildings
            {'category': 'industrial', 'title': 'Construction of Industrial Warehouses', 'description': 'Expert construction of large-scale industrial warehouses with modern facilities and infrastructure.', 'order': 1},
            {'category': 'industrial', 'title': 'Construction of Commercial Buildings and Towers', 'description': 'Design and construction of commercial buildings and high-rise towers with state-of-the-art facilities.', 'order': 2},
            {'category': 'industrial', 'title': 'Equipment Erection', 'description': 'Professional equipment erection services for industrial and commercial facilities.', 'order': 3},
            # Civil
            {'category': 'civil', 'title': 'Large Format Earth Works and Road Works', 'description': 'Comprehensive earthworks and road construction services for large-scale projects.', 'order': 1},
            {'category': 'civil', 'title': 'Contour Survey, Grading and Leveling', 'description': 'Professional surveying, grading, leveling, and setting out services for construction projects.', 'order': 2},
            {'category': 'civil', 'title': 'Construction of Foundations', 'description': 'Expert foundation construction for industrial buildings and heavy equipment.', 'order': 3},
            {'category': 'civil', 'title': 'Canal Excavation and Lining', 'description': 'Canal excavation, lining, strengthening of banks, and associated head works.', 'order': 4},
            {'category': 'civil', 'title': 'Water Storage Solutions', 'description': 'Construction of Ash ponds, water storage tanks, and reservoirs.', 'order': 5},
            {'category': 'civil', 'title': 'Control Blasting / Rock Blasting Works', 'description': 'Professional and controlled blasting services for rock excavation projects.', 'order': 6},
            # Cross Country Piping
            {'category': 'piping', 'title': 'Survey, Marking, and ROU Formation', 'description': 'Complete survey, marking, and Right of Way (ROU) formation services for pipeline projects.', 'order': 1},
            {'category': 'piping', 'title': 'Stringing, Trench Work, Welding, Laying and Testing', 'description': 'End-to-end pipeline services including stringing, trench work, welding, laying, and testing.', 'order': 2},
            {'category': 'piping', 'title': 'Valve Stations and Pump Houses', 'description': 'Construction of valve stations and pump houses for pipeline infrastructure.', 'order': 3},
            {'category': 'piping', 'title': 'Intake Wells and Access Bridges', 'description': 'Construction of intake wells and fabrication and erection of access bridges.', 'order': 4},
        ]

        for service_data in services_data:
            service, created = Service.objects.get_or_create(
                category=service_data['category'],
                title=service_data['title'],
                defaults=service_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created service: {service_data["title"]}'))

        # Completed Projects
        projects_data = [
            {
                'work_awarded_by': 'NKC Project Pvt. Ltd.',
                'wo_reference': 'NKCPPL/ Raj. Pkg No-3/2019 28/067/10-12-19',
                'type_of_work': 'Cont. of Earth Work Under Road Work',
                'date': '2019-12-10',
                'status': 'completed',
                'order': 1
            },
            {
                'work_awarded_by': 'VRC',
                'wo_reference': 'VRC/Raj. Pkg-08/2020 35/075/04-06-2020',
                'type_of_work': 'Cont. of Earth Work Under Road Work',
                'date': '2020-06-04',
                'status': 'completed',
                'order': 2
            },
            {
                'work_awarded_by': 'BARBRIK LOGISTIC PVT. LTD.',
                'wo_reference': 'BLPL/RAJ. WO. NO.-113504 18-8-2020',
                'type_of_work': 'Earth Work Under Road Work',
                'date': '2020-06-04',
                'status': 'completed',
                'order': 3
            },
            {
                'work_awarded_by': 'M/s Krishna Construction',
                'wo_reference': 'KCPL/Raj Pkg-04/2020 201058-08103/2020',
                'type_of_work': 'Cont. of Earth Work Under Road Work',
                'date': '2020-03-08',
                'status': 'completed',
                'order': 4
            },
            {
                'work_awarded_by': 'M/s Krishna Construction',
                'wo_reference': 'WO/KC/BMP/AJ-SR/ PKG-1/2021/01',
                'type_of_work': 'Cont. of Earth Work Under Road Work',
                'date': '2021-07-01',
                'status': 'completed',
                'order': 5
            }
        ]

        for project_data in projects_data:
            project, created = CompletedProject.objects.get_or_create(
                wo_reference=project_data['wo_reference'],
                defaults=project_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created project: {project_data["work_awarded_by"]}'))

        # Equipment (sample data)
        equipment_data = [
            {'name': 'Excavators', 'quantity': 5, 'category': 'Heavy Equipment', 'order': 1},
            {'name': 'Dump Trucks', 'quantity': 8, 'category': 'Heavy Equipment', 'order': 2},
            {'name': 'Motor Graders', 'quantity': 3, 'category': 'Heavy Equipment', 'order': 3},
            {'name': 'Bulldozers', 'quantity': 4, 'category': 'Heavy Equipment', 'order': 4},
            {'name': 'Road Rollers', 'quantity': 3, 'category': 'Heavy Equipment', 'order': 5},
            {'name': 'Loaders', 'quantity': 6, 'category': 'Heavy Equipment', 'order': 6},
        ]

        for eq_data in equipment_data:
            equipment, created = Equipment.objects.get_or_create(
                name=eq_data['name'],
                defaults=eq_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created equipment: {eq_data["name"]}'))

        # Staff (sample data)
        staff_data = [
            # Site Staff
            {'designation': 'Project Manager', 'staff_type': 'site', 'team': 'TEAM-A', 'quantity': 1, 'order': 1},
            {'designation': 'Project Manager', 'staff_type': 'site', 'team': 'TEAM-B', 'quantity': 1, 'order': 2},
            {'designation': 'Senior Engineer', 'staff_type': 'site', 'team': 'TEAM-A', 'quantity': 1, 'order': 3},
            {'designation': 'Senior Engineer', 'staff_type': 'site', 'team': 'TEAM-B', 'quantity': 1, 'order': 4},
            {'designation': 'Junior Engineer', 'staff_type': 'site', 'team': 'TEAM-A', 'quantity': 2, 'order': 5},
            {'designation': 'Junior Engineer', 'staff_type': 'site', 'team': 'TEAM-B', 'quantity': 2, 'order': 6},
            {'designation': 'Surveyor', 'staff_type': 'site', 'team': 'TEAM-A', 'quantity': 1, 'order': 7},
            {'designation': 'Surveyor', 'staff_type': 'site', 'team': 'TEAM-B', 'quantity': 1, 'order': 8},
            {'designation': 'Supervisor', 'staff_type': 'site', 'team': 'TEAM-A', 'quantity': 2, 'order': 9},
            {'designation': 'Supervisor', 'staff_type': 'site', 'team': 'TEAM-B', 'quantity': 1, 'order': 10},
            {'designation': 'Safety Supervisors', 'staff_type': 'site', 'team': 'TEAM-B', 'quantity': 1, 'order': 11},
            {'designation': 'Electrician', 'staff_type': 'site', 'team': 'TEAM-B', 'quantity': 1, 'order': 12},
            {'designation': 'Mechanic', 'staff_type': 'site', 'team': 'TEAM-A', 'quantity': 2, 'order': 13},
            {'designation': 'Mechanic', 'staff_type': 'site', 'team': 'TEAM-B', 'quantity': 1, 'order': 14},
            {'designation': 'Store Keeper', 'staff_type': 'site', 'team': 'TEAM-A', 'quantity': 1, 'order': 15},
            {'designation': 'Store Keeper', 'staff_type': 'site', 'team': 'TEAM-B', 'quantity': 2, 'order': 16},
            {'designation': 'Cook', 'staff_type': 'site', 'team': 'TEAM-A', 'quantity': 2, 'order': 17},
            {'designation': 'Cook', 'staff_type': 'site', 'team': 'TEAM-B', 'quantity': 2, 'order': 18},
            {'designation': 'Skilled Labor', 'staff_type': 'site', 'team': 'TEAM-A', 'quantity': 8, 'order': 19},
            {'designation': 'Skilled Labor', 'staff_type': 'site', 'team': 'TEAM-B', 'quantity': 8, 'order': 20},
            # Central Planner
            {'designation': 'Proprietor', 'staff_type': 'central', 'team': '', 'quantity': 1, 'order': 1},
            {'designation': 'Manager', 'staff_type': 'central', 'team': '', 'quantity': 2, 'order': 2},
            {'designation': 'Senior Accountant', 'staff_type': 'central', 'team': '', 'quantity': 1, 'order': 3},
            {'designation': 'Account Assistant', 'staff_type': 'central', 'team': '', 'quantity': 2, 'order': 4},
            {'designation': 'Financer', 'staff_type': 'central', 'team': '', 'quantity': 1, 'order': 5},
            {'designation': 'HR Officer', 'staff_type': 'central', 'team': '', 'quantity': 2, 'order': 6},
            {'designation': 'Safety Officer', 'staff_type': 'central', 'team': '', 'quantity': 1, 'order': 7},
            {'designation': 'Drawing & Designing Section', 'staff_type': 'central', 'team': '', 'quantity': 1, 'order': 8},
            {'designation': 'Billing Section', 'staff_type': 'central', 'team': '', 'quantity': 2, 'order': 9},
            {'designation': 'Q&C', 'staff_type': 'central', 'team': '', 'quantity': 1, 'order': 10},
            {'designation': 'Purchaser', 'staff_type': 'central', 'team': '', 'quantity': 2, 'order': 11},
        ]

        for staff_item in staff_data:
            staff, created = Staff.objects.get_or_create(
                designation=staff_item['designation'],
                staff_type=staff_item['staff_type'],
                team=staff_item['team'],
                defaults=staff_item
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created staff: {staff_item["designation"]}'))

        self.stdout.write(self.style.SUCCESS('\nInitial data loaded successfully!'))

