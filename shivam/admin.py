from django.contrib import admin
from .models import CompanyInfo, KeyPerson, Service, CompletedProject, Equipment, Staff, CompanyImage, Document, EquipmentImage, ContactMessage, HomeBanner

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'tagline', 'phone', 'email', 'address')
        }),
        ('Company Details', {
            'fields': ('introduction', 'vision', 'quality_policy')
        }),
        ('Images', {
            'fields': ('logo', 'hero_image')
        }),
        ('Page Background Images', {
            'fields': ('services_bg', 'projects_bg', 'equipment_bg', 'vision_bg', 'quality_bg', 'team_bg', 'contact_bg'),
            'description': 'Upload background images for different pages. Recommended size: 1920x1080px'
        }),
        ('Social Media', {
            'fields': ('instagram_url',)
        }),
    )

@admin.register(CompanyImage)
class CompanyImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_type', 'order']
    list_filter = ['image_type']
    list_editable = ['order']
    search_fields = ['title', 'description']

@admin.register(KeyPerson)
class KeyPersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'order']
    list_editable = ['order']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order']
    list_filter = ['category']
    list_editable = ['order']

@admin.register(CompletedProject)
class CompletedProjectAdmin(admin.ModelAdmin):
    list_display = ['work_awarded_by', 'type_of_work', 'status', 'date']
    list_filter = ['status', 'date']
    date_hierarchy = 'date'
    fields = ['work_awarded_by', 'wo_reference', 'type_of_work', 'status', 'date', 'image', 'order']

class EquipmentImageInline(admin.TabularInline):
    model = EquipmentImage
    extra = 1
    fields = ['image', 'title', 'description', 'order']

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'category']
    list_filter = ['category']
    fields = ['name', 'quantity', 'category', 'image', 'description', 'specifications', 'order']
    inlines = [EquipmentImageInline]

@admin.register(EquipmentImage)
class EquipmentImageAdmin(admin.ModelAdmin):
    list_display = ['equipment', 'title', 'order', 'uploaded_at']
    list_filter = ['equipment', 'uploaded_at']
    list_editable = ['order']
    search_fields = ['equipment__name', 'title', 'description']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['designation', 'staff_type', 'team', 'quantity']
    list_filter = ['staff_type', 'team']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'document_type', 'get_file_size', 'uploaded_at', 'order']
    list_filter = ['document_type', 'uploaded_at']
    list_editable = ['order']
    search_fields = ['title', 'description']
    readonly_fields = ['uploaded_at', 'get_file_size']
    fields = ['title', 'document_type', 'file', 'description', 'order', 'uploaded_at', 'get_file_size']
    
    def get_file_size(self, obj):
        return obj.get_file_size()
    get_file_size.short_description = 'File Size'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    search_fields = ['name', 'email', 'phone', 'message']
    readonly_fields = ['name', 'email', 'phone', 'message', 'created_at']


@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'order', 'created_at']
    list_filter = ['is_active']
    list_editable = ['is_active', 'order']
    search_fields = ['title', 'subtitle', 'tagline']
    readonly_fields = ['media_type']
    fields = [
        'title', 'subtitle', 'tagline',
        'media_type', 'video',
        'button_text', 'button_url',
        'secondary_button_text', 'secondary_button_url',
        'is_active', 'order'
    ]
