from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse, Http404, JsonResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_http_methods
import os
from .models import CompanyInfo, KeyPerson, Service, CompletedProject, Equipment, Staff, CompanyImage, Document, EquipmentImage, ContactMessage, HomeBanner

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
    
    context = {
        'company': company,
        'video_banner': video_banner,
        'banners': banners,
        'intro_images': intro_images,
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
    
    context = {
        'services_by_category': services_by_category,
        'company': company,
        'service_images': service_images,
    }
    return render(request, 'shivam/services.html', context)

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
    
    # Group equipment by category
    equipment_by_category = {}
    for item in equipment_list:
        category = item.category or 'Other'
        if category not in equipment_by_category:
            equipment_by_category[category] = []
        equipment_by_category[category].append(item)
    
    context = {
        'equipment_by_category': equipment_by_category,
        'company': company,
        'equipment_images': equipment_images,
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
    """Team and organization structure page"""
    staff = Staff.objects.all()
    company = CompanyInfo.objects.first()
    
    # Group staff by type
    site_staff = staff.filter(staff_type='site')
    central_staff = staff.filter(staff_type='central')
    
    # Calculate totals
    site_staff_total = sum(item.quantity for item in site_staff)
    central_staff_total = sum(item.quantity for item in central_staff)
    grand_total = site_staff_total + central_staff_total
    
    # Group site staff by designation for summary
    site_staff_summary = {}
    for item in site_staff:
        designation = item.designation
        if designation not in site_staff_summary:
            site_staff_summary[designation] = 0
        site_staff_summary[designation] += item.quantity
    
    # Group central staff by designation for summary
    central_staff_summary = {}
    for item in central_staff:
        designation = item.designation
        if designation not in central_staff_summary:
            central_staff_summary[designation] = 0
        central_staff_summary[designation] += item.quantity
    
    context = {
        'site_staff': site_staff,
        'central_staff': central_staff,
        'site_staff_summary': site_staff_summary,
        'central_staff_summary': central_staff_summary,
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

        if not name or not email or not message_text:
            messages.error(request, "Please fill in Name, Email and Message.")
        else:
            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message_text,
            )
            messages.success(request, "Thank you! Your message has been sent. We will contact you soon.")
            return redirect('contact')

    return render(request, 'shivam/contact.html', {'company': company})

def documents(request):
    """Documents page - list all uploaded documents and handle uploads"""
    company = CompanyInfo.objects.first()
    
    # Handle file upload
    if request.method == 'POST':
        try:
            title = request.POST.get('title', '')
            document_type = request.POST.get('document_type', 'other')
            description = request.POST.get('description', '')
            file = request.FILES.get('file')
            
            if not file:
                messages.error(request, 'Please select a file to upload.')
            elif not title:
                messages.error(request, 'Please enter a document title.')
            else:
                # Create document
                document = Document.objects.create(
                    title=title,
                    document_type=document_type,
                    file=file,
                    description=description
                )
                messages.success(request, f'Document "{title}" uploaded successfully!')
                return redirect('documents')
        except Exception as e:
            messages.error(request, f'Error uploading document: {str(e)}')
    
    # Get all documents
    documents_list = Document.objects.all()
    
    # Group documents by type
    documents_by_type = {}
    for doc in documents_list:
        doc_type = doc.get_document_type_display()
        if doc_type not in documents_by_type:
            documents_by_type[doc_type] = []
        documents_by_type[doc_type].append(doc)
    
    context = {
        'company': company,
        'documents_by_type': documents_by_type,
        'total_documents': documents_list.count(),
    }
    return render(request, 'shivam/documents.html', context)

def download_document(request, document_id):
    """Download a document"""
    document = get_object_or_404(Document, id=document_id)
    
    try:
        file_path = document.file.path
        if os.path.exists(file_path):
            response = FileResponse(open(file_path, 'rb'), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
        else:
            raise Http404("File not found")
    except Exception as e:
        raise Http404("Error downloading file")
