from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse, Http404, JsonResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_http_methods
import os
from .models import CompanyInfo, KeyPerson, Service, CompletedProject, Equipment, Staff, CompanyImage, Document, EquipmentImage, ContactMessage, HomeBanner
from .translations import get_translator


def _lang(request):
    lang = request.session.get('language', 'en')
    return lang if lang in ('en', 'hi') else 'en'


def set_language(request, lang):
    """Switch UI language (en / hi) and return to the previous page."""
    if lang in ('en', 'hi'):
        request.session['language'] = lang
    next_url = request.GET.get('next', '/')
    if not next_url.startswith('/'):
        next_url = '/'
    return redirect(next_url)

def home(request):
    """Home page with introduction and overview"""
    company = CompanyInfo.objects.first()
    if not company:
        company = CompanyInfo.objects.create()

    # Show full-screen hero video when active uploaded video banner exists.
    video_banner = (
        HomeBanner.objects.filter(
            is_active=True,
            video__isnull=False
        )
        .exclude(video='')
        .order_by('order', '-created_at')
        .first()
    )

    # Admin-managed homepage banners.
    banners = HomeBanner.objects.filter(is_active=True)

    # Intro section images (separate from carousel banners)
    intro_images = CompanyImage.objects.filter(image_type='intro')[:6]

    # If no intro images, get any available images for intro section cards
    if not intro_images:
        intro_images = CompanyImage.objects.all()[:6]

    key_persons = KeyPerson.objects.all()[:4]
    ceo = KeyPerson.objects.filter(role__icontains='ceo').first()
    if not ceo:
        ceo = KeyPerson.objects.filter(role__icontains='proprietor').first()
    if not ceo:
        ceo = KeyPerson.objects.order_by('order').first()
    
    context = {
        'company': company,
        'video_banner': video_banner,
        'banners': banners,
        'intro_images': intro_images,
        'key_persons': key_persons,
        'ceo': ceo,
    }
    return render(request, 'shivam/home.html', context)

def about(request):
    """About page with company introduction, vision, quality policy, and key persons"""
    company = CompanyInfo.objects.first()
    if not company:
        company = CompanyInfo.objects.create()
    
    key_persons = KeyPerson.objects.all()
    vision_images = CompanyImage.objects.filter(image_type='vision')[:2]
    quality_images = CompanyImage.objects.filter(image_type='quality')[:2]
    
    context = {
        'company': company,
        'key_persons': key_persons,
        'vision_images': vision_images,
        'quality_images': quality_images,
    }
    return render(request, 'shivam/about.html', context)

def _road_service_fallbacks():
    """Build bilingual service stubs from road_content when DB is empty."""
    from shivam.road_content import ROAD_SERVICES, SERVICE_CATEGORY_LABELS

    class _Stub:
        def __init__(self, item):
            self._item = item
            self.category = item['category']
            self.title = item['title']
            self.title_hi = item['title_hi']
            self.description = item['description']
            self.description_hi = item['description_hi']

        def get_category_display(self):
            return SERVICE_CATEGORY_LABELS[self.category][0]

    services_by_category = {}
    for item in ROAD_SERVICES:
        stub = _Stub(item)
        category = stub.get_category_display()
        services_by_category.setdefault(category, []).append(stub)
    return services_by_category


def services(request):
    """Services page"""
    services = Service.objects.all()
    company = CompanyInfo.objects.first()
    service_images = CompanyImage.objects.filter(image_type='service')
    
    # Group services by category
    services_by_category = {}
    for service in services:
        category = service.get_category_display()
        if category not in services_by_category:
            services_by_category[category] = []
        services_by_category[category].append(service)

    if not services_by_category:
        services_by_category = _road_service_fallbacks()
    
    context = {
        'services_by_category': services_by_category,
        'company': company,
        'service_images': service_images,
    }
    return render(request, 'shivam/services.html', context)


def solar_energy(request):
    """Sister firm page — Shivam Solar Energy (Rajasthan projects & branches)."""
    company = CompanyInfo.objects.first()
    t = get_translator(_lang(request))

    solar_services = [
        {'title': t.solar_svc_home_title, 'text': t.solar_svc_home_text, 'image': 'images/solar/solar-rooftop.png', 'featured': True},
        {'title': t.solar_svc_1_title, 'text': t.solar_svc_1_text, 'image': 'images/solar/solar-rooftop.png'},
        {'title': t.solar_svc_2_title, 'text': t.solar_svc_2_text, 'image': 'images/solar/solar-ground.png'},
        {'title': t.solar_svc_3_title, 'text': t.solar_svc_3_text, 'image': 'images/solar/solar-inverter.png'},
    ]
    solar_projects = [
        {'title': t.solar_proj_1_title, 'place': t.solar_proj_1_place, 'status': t.solar_status_ongoing},
        {'title': t.solar_proj_2_title, 'place': t.solar_proj_2_place, 'status': t.solar_status_ongoing},
        {'title': t.solar_proj_3_title, 'place': t.solar_proj_3_place, 'status': t.solar_status_completed},
        {'title': t.solar_proj_4_title, 'place': t.solar_proj_4_place, 'status': t.solar_status_completed},
    ]
    solar_branches = [
        {'city': t.solar_br_1_city, 'area': t.solar_br_1_area},
        {'city': t.solar_br_2_city, 'area': t.solar_br_2_area},
        {'city': t.solar_br_3_city, 'area': t.solar_br_3_area},
        {'city': t.solar_br_4_city, 'area': t.solar_br_4_area},
    ]

    context = {
        'company': company,
        'solar_services': solar_services,
        'solar_projects': solar_projects,
        'solar_branches': solar_branches,
    }
    return render(request, 'shivam/solar.html', context)

def projects(request):
    """Projects page with filtering"""
    company = CompanyInfo.objects.first()
    
    # Get filter from request
    status_filter = request.GET.get('status', 'all').strip().lower().replace('-', '_').replace(' ', '_')
    valid_filters = {'all', 'completed', 'on_hand', 'ongoing'}
    if status_filter not in valid_filters:
        status_filter = 'all'
    
    # Get all projects
    all_projects = CompletedProject.objects.all()
    
    # Filter by status if specified
    if status_filter == 'completed':
        projects = all_projects.filter(status='completed')
    elif status_filter == 'on_hand':
        projects = all_projects.filter(status='on_hand')
    elif status_filter == 'ongoing':
        projects = all_projects.filter(status='ongoing')
    else:
        projects = all_projects
    
    # Count projects by status
    completed_count = all_projects.filter(status='completed').count()
    on_hand_count = all_projects.filter(status='on_hand').count()
    ongoing_count = all_projects.filter(status='ongoing').count()
    
    context = {
        'projects': projects,
        'company': company,
        'current_filter': status_filter,
        'completed_count': completed_count,
        'on_hand_count': on_hand_count,
        'ongoing_count': ongoing_count,
        'total_count': all_projects.count(),
    }
    return render(request, 'shivam/projects.html', context)


def project_detail(request, project_id):
    """Single project detail page with richer presentation"""
    company = CompanyInfo.objects.first()
    project = get_object_or_404(CompletedProject, id=project_id)

    context = {
        'company': company,
        'project': project,
    }
    return render(request, 'shivam/project_detail.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    """Front-end shortcuts to Django admin pages (staff only)."""
    company = CompanyInfo.objects.first()
    if not company:
        company = CompanyInfo.objects.create()

    return render(request, 'shivam/admin_dashboard.html', {'company': company})

def equipment(request):
    """Equipment and machinery page"""
    equipment_list = Equipment.objects.all()
    company = CompanyInfo.objects.first()
    equipment_images = CompanyImage.objects.filter(image_type='equipment')

    equipment_by_category = {}
    for item in equipment_list:
        category = item.category or 'Other'
        equipment_by_category.setdefault(category, []).append(item)

    fleet_total = sum(item.quantity for item in equipment_list)

    context = {
        'equipment_by_category': equipment_by_category,
        'company': company,
        'equipment_images': equipment_images,
        'fleet_total': fleet_total,
    }
    return render(request, 'shivam/equipment.html', context)

def equipment_detail(request, equipment_id):
    """Equipment detail page with images"""
    equipment = get_object_or_404(Equipment, id=equipment_id)
    company = CompanyInfo.objects.first()
    equipment_images = EquipmentImage.objects.filter(equipment=equipment).order_by('order', '-uploaded_at')
    
    context = {
        'equipment': equipment,
        'equipment_images': equipment_images,
        'company': company,
    }
    return render(request, 'shivam/equipment_detail.html', context)

def team(request):
    """Team page — strength cards + site/central structure (no CEO gallery)."""
    staff = Staff.objects.all()
    company = CompanyInfo.objects.first()

    site_staff = staff.filter(staff_type='site')
    central_staff = staff.filter(staff_type='central')

    site_staff_total = sum(item.quantity for item in site_staff)
    central_staff_total = sum(item.quantity for item in central_staff)
    grand_total = site_staff_total + central_staff_total

    teams_map = {}
    for item in site_staff:
        team_name = (item.team or '').strip() or 'General'
        teams_map.setdefault(team_name, [])
        teams_map[team_name].append(item)

    site_team_panels = [
        {
            'name': name,
            'members': members,
            'total': sum(m.quantity for m in members),
        }
        for name, members in sorted(teams_map.items())
    ]

    context = {
        'site_team_panels': site_team_panels,
        'central_roles': list(central_staff),
        'site_staff_total': site_staff_total,
        'central_staff_total': central_staff_total,
        'grand_total': grand_total,
        'company': company,
    }
    return render(request, 'shivam/team.html', context)

def contact(request):
    """Contact page"""
    company = CompanyInfo.objects.first()
    if not company:
        company = CompanyInfo.objects.create()

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message_text = request.POST.get('message', '').strip()

        t = get_translator(_lang(request))
        if not name or not email or not message_text:
            messages.error(request, t.msg_error)
        else:
            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message_text,
            )
            messages.success(request, t.msg_success)
            return redirect('contact')

    return render(request, 'shivam/contact.html', {'company': company})

def documents(request):
    """Public document library. Upload is staff-only."""
    company = CompanyInfo.objects.first()
    t = get_translator(_lang(request))

    if request.method == 'POST':
        if not request.user.is_authenticated or not request.user.is_staff:
            messages.error(request, t.doc_upload_forbidden)
            return redirect('documents')
        try:
            title = request.POST.get('title', '').strip()
            document_type = request.POST.get('document_type', 'other')
            description = request.POST.get('description', '').strip()
            file = request.FILES.get('file')

            if not file:
                messages.error(request, t.doc_upload_no_file)
            elif not title:
                messages.error(request, t.doc_upload_no_title)
            else:
                Document.objects.create(
                    title=title,
                    document_type=document_type,
                    file=file,
                    description=description,
                )
                messages.success(request, t.doc_upload_success)
                return redirect('documents')
        except Exception:
            messages.error(request, t.doc_upload_error)

    documents_list = Document.objects.all()
    documents_by_type = {}
    for doc in documents_list:
        doc_type = doc.get_document_type_display()
        documents_by_type.setdefault(doc_type, []).append(doc)

    context = {
        'company': company,
        'documents_by_type': documents_by_type,
        'total_documents': documents_list.count(),
        'can_upload': request.user.is_authenticated and request.user.is_staff,
    }
    return render(request, 'shivam/documents.html', context)


def document_detail(request, document_id):
    """Document detail page for company records."""
    document = get_object_or_404(Document, id=document_id)
    company = CompanyInfo.objects.first()
    related = Document.objects.filter(document_type=document.document_type).exclude(id=document.id)[:4]
    context = {
        'document': document,
        'company': company,
        'related_documents': related,
        'can_download': True,
    }
    return render(request, 'shivam/document_detail.html', context)


def download_document(request, document_id):
    """Download a document (public company files)."""
    document = get_object_or_404(Document, id=document_id)

    try:
        file_path = document.file.path
        if os.path.exists(file_path):
            response = FileResponse(open(file_path, 'rb'), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
        raise Http404("File not found")
    except Http404:
        raise
    except Exception:
        raise Http404("Error downloading file")
