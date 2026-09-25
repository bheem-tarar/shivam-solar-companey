from django.core.management.base import BaseCommand

from shivam.models import CompanyInfo, KeyPerson, Service
from shivam.road_content import COMPANY_CONTENT, KEY_PERSONS, ROAD_SERVICES


class Command(BaseCommand):
    help = 'Update website content for road construction & earthwork specialization'

    def handle(self, *args, **options):
        company = CompanyInfo.objects.first()
        if not company:
            company = CompanyInfo.objects.create()

        company.tagline = COMPANY_CONTENT['tagline']
        company.tagline_hi = COMPANY_CONTENT['tagline_hi']
        company.introduction = COMPANY_CONTENT['introduction']
        company.introduction_hi = COMPANY_CONTENT['introduction_hi']
        company.vision = COMPANY_CONTENT['vision']
        company.vision_hi = COMPANY_CONTENT['vision_hi']
        company.quality_policy = COMPANY_CONTENT['quality_policy']
        company.quality_policy_hi = COMPANY_CONTENT['quality_policy_hi']
        company.save()
        self.stdout.write('Updated company profile for road earthwork focus')

        deleted, _ = Service.objects.all().delete()
        self.stdout.write(f'Removed {deleted} old service record(s)')

        for item in ROAD_SERVICES:
            Service.objects.create(
                category=item['category'],
                title=item['title'],
                title_hi=item['title_hi'],
                description=item['description'],
                description_hi=item['description_hi'],
                order=item['order'],
            )
        self.stdout.write(self.style.SUCCESS(f'Created {len(ROAD_SERVICES)} road-focused services'))

        for person_data in KEY_PERSONS:
            person, _ = KeyPerson.objects.update_or_create(
                name=person_data['name'],
                defaults={
                    'role': person_data['role'],
                    'role_hi': person_data['role_hi'],
                    'description': person_data['description'],
                    'description_hi': person_data['description_hi'],
                    'order': person_data['order'],
                },
            )
        self.stdout.write(self.style.SUCCESS(f'Updated {len(KEY_PERSONS)} key persons for road earthwork focus'))
