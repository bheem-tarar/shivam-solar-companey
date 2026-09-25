from django.core.management.base import BaseCommand

from shivam.models import CompanyInfo, KeyPerson, Service, CompletedProject, Equipment, Staff
from shivam.road_content import COMPANY_CONTENT, KEY_PERSONS, ROAD_SERVICES

class Command(BaseCommand):
    help = 'Load initial data for Shivam Construction Company'

    def handle(self, *args, **options):
        # Company Info
        company, created = CompanyInfo.objects.get_or_create(
            name="Shivam Construction Company",
            defaults={
                'tagline': COMPANY_CONTENT['tagline'],
                'tagline_hi': COMPANY_CONTENT['tagline_hi'],
                'phone': '6350092193',
                'email': 'scccompany91@gmail.com',
                'address': 'BUILDING NO./FLAT NO.: MEEL COLONY KE SAMANE, ROAD/STREET: WARD NO. 03 NEW, CITY/TOWN/VILLAGE: SURATGARH, DISTRICT: SRI GANGANAGAR, STATE: RAJASTHAN, PIN CODE: 335804',
                'introduction': COMPANY_CONTENT['introduction'],
                'introduction_hi': COMPANY_CONTENT['introduction_hi'],
                'vision': COMPANY_CONTENT['vision'],
                'vision_hi': COMPANY_CONTENT['vision_hi'],
                'quality_policy': COMPANY_CONTENT['quality_policy'],
                'quality_policy_hi': COMPANY_CONTENT['quality_policy_hi'],
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Company info created'))
        else:
            self.stdout.write(self.style.SUCCESS('Company info already exists'))

        for person_data in KEY_PERSONS:
            person, created = KeyPerson.objects.get_or_create(
                name=person_data['name'],
                defaults={
                    'role': person_data['role'],
                    'role_hi': person_data['role_hi'],
                    'description': person_data['description'],
                    'description_hi': person_data['description_hi'],
                    'order': person_data['order'],
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created key person: {person_data["name"]}'))

        for service_data in ROAD_SERVICES:
            service, created = Service.objects.get_or_create(
                category=service_data['category'],
                title=service_data['title'],
                defaults={
                    'title_hi': service_data['title_hi'],
                    'description': service_data['description'],
                    'description_hi': service_data['description_hi'],
                    'order': service_data['order'],
                },
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
            {'name': 'Excavators', 'quantity': 5, 'category': 'Heavy Earth-Moving Equipment', 'order': 1},
            {'name': 'Dump Trucks', 'quantity': 8, 'category': 'Heavy Earth-Moving Equipment', 'order': 2},
            {'name': 'Motor Graders', 'quantity': 3, 'category': 'Heavy Earth-Moving Equipment', 'order': 3},
            {'name': 'Bulldozers', 'quantity': 4, 'category': 'Heavy Earth-Moving Equipment', 'order': 4},
            {'name': 'Road Rollers', 'quantity': 3, 'category': 'Heavy Earth-Moving Equipment', 'order': 5},
            {'name': 'Loaders', 'quantity': 6, 'category': 'Heavy Earth-Moving Equipment', 'order': 6},
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

