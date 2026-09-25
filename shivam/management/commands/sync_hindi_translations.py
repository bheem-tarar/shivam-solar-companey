from django.core.management.base import BaseCommand

from shivam.models import (
    CompanyInfo, KeyPerson, Service, CompletedProject,
    Equipment, Staff, HomeBanner, Document,
)
from shivam.road_content import COMPANY_CONTENT, KEY_PERSONS, ROAD_SERVICES


class Command(BaseCommand):
    help = 'Populate Hindi (_hi) fields for bilingual website content'

    def handle(self, *args, **options):
        company = CompanyInfo.objects.first()
        if company:
            company.tagline_hi = COMPANY_CONTENT['tagline_hi']
            company.introduction_hi = COMPANY_CONTENT['introduction_hi']
            company.vision_hi = COMPANY_CONTENT['vision_hi']
            company.quality_policy_hi = COMPANY_CONTENT['quality_policy_hi']
            company.address_hi = (
                'दुकान नं. ०५, इंडेन गैस ऑफिस के पास, बसंत विहार कॉलोनी, सूरतगढ़, '
                'श्री गंगानगर, राजस्थान, ३३५८०४'
            )
            company.save()
            self.stdout.write('Updated CompanyInfo Hindi fields')

        for person_data in KEY_PERSONS:
            person = KeyPerson.objects.filter(name=person_data['name']).first()
            if person:
                person.role_hi = person_data['role_hi']
                person.description_hi = person_data['description_hi']
                person.save()

        services_hi = {
            item['title']: (item['title_hi'], item['description_hi'])
            for item in ROAD_SERVICES
        }
        for service in Service.objects.all():
            if service.title in services_hi:
                service.title_hi, service.description_hi = services_hi[service.title]
                service.save()

        projects_hi = {
            'Cont. of Earth Work Under Road Work': 'सड़क कार्य के अंतर्गत मिट्टी का कार्य (निरंतर)',
            'Earth Work Under Road Work': 'सड़क कार्य के अंतर्गत मिट्टी का कार्य',
        }
        for project in CompletedProject.objects.all():
            if project.type_of_work in projects_hi:
                project.type_of_work_hi = projects_hi[project.type_of_work]
                project.save()

        equipment_hi = {
            'Excavators': ('एक्सकेवेटर', 'भारी पृथ्वी-खनन उपकरण'),
            'Dump Trucks': ('डंप ट्रक', 'भारी पृथ्वी-खनन उपकरण'),
            'Motor Graders': ('मोटर ग्रेडर', 'भारी पृथ्वी-खनन उपकरण'),
            'Bulldozers': ('बुलडोज़र', 'भारी पृथ्वी-खनन उपकरण'),
            'Road Rollers': ('रोड रोलर', 'भारी पृथ्वी-खनन उपकरण'),
            'Loaders': ('लोडर', 'भारी पृथ्वी-खनन उपकरण'),
        }
        for item in Equipment.objects.all():
            if item.name in equipment_hi:
                item.name_hi, item.category_hi = equipment_hi[item.name]
                item.save()

        staff_hi = {
            'Project Manager': 'परियोजना प्रबंधक',
            'Senior Engineer': 'वरिष्ठ अभियंता',
            'Junior Engineer': 'कनिष्ठ अभियंता',
            'Surveyor': 'सर्वेक्षक',
            'Supervisor': 'सुपरवाइज़र',
            'Safety Supervisors': 'सुरक्षा सुपरवाइज़र',
            'Electrician': 'इलेक्ट्रीशियन',
            'Mechanic': 'मैकेनिक',
            'Store Keeper': 'स्टोर कीपर',
            'Cook': 'रसोइया',
            'Skilled Labor': 'कुशल श्रमिक',
            'Proprietor': 'मालिक',
            'Manager': 'प्रबंधक',
            'Senior Accountant': 'वरिष्ठ लेखाकार',
            'Account Assistant': 'लेखा सहायक',
            'Financer': 'वित्त अधिकारी',
            'HR Officer': 'मानव संसाधन अधिकारी',
            'Safety Officer': 'सुरक्षा अधिकारी',
            'Drawing & Designing Section': 'ड्राइंग और डिज़ाइन विभाग',
            'Billing Section': 'बिलिंग विभाग',
            'Q&C': 'गुणवत्ता नियंत्रण',
            'Purchaser': 'खरीद अधिकारी',
        }
        for staff in Staff.objects.all():
            if staff.designation in staff_hi:
                staff.designation_hi = staff_hi[staff.designation]
                staff.save()

        for banner in HomeBanner.objects.all():
            banner.title_hi = banner.title_hi or 'शिवम कंस्ट्रक्शन कंपनी'
            banner.subtitle_hi = COMPANY_CONTENT['tagline_hi']
            banner.tagline_hi = banner.tagline_hi or COMPANY_CONTENT['tagline_hi']
            banner.button_text_hi = banner.button_text_hi or 'और जानें'
            banner.secondary_button_text_hi = banner.secondary_button_text_hi or 'संपर्क करें'
            banner.save()

        self.stdout.write(self.style.SUCCESS('Hindi translations synced successfully.'))
