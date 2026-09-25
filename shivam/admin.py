from django.contrib import admin
from .models import CompanyInfo, KeyPerson, Service, CompletedProject, Equipment, Staff, CompanyImage, Document, EquipmentImage, ContactMessage, HomeBanner

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'tagline', 'tagline_hi', 'phone', 'email', 'address', 'address_hi')
        }),
        ('Company Details', {
            'fields': (
                'introduction', 'introduction_hi',
                'vision', 'vision_hi',
                'quality_policy', 'quality_policy_hi',
            )
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
    fields = ['name', 'role', 'role_hi', 'description', 'description_hi', 'photo', 'order']
    readonly_fields = []

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order']
    list_filter = ['category']
    list_editable = ['order']
    fields = ['category', 'title', 'title_hi', 'description', 'description_hi', 'order']

@admin.register(CompletedProject)
class CompletedProjectAdmin(admin.ModelAdmin):
    list_display = ['work_awarded_by', 'type_of_work', 'status', 'date']
    list_filter = ['status', 'date']
    date_hierarchy = 'date'
    fields = [
        'work_awarded_by', 'work_awarded_by_hi',
        'wo_reference', 'type_of_work', 'type_of_work_hi',
        'status', 'date', 'image', 'order',
    ]

class EquipmentImageInline(admin.TabularInline):
    model = EquipmentImage
    extra = 1
    fields = ['image', 'title', 'title_hi', 'description', 'description_hi', 'order']

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'category']
    list_filter = ['category']
    fields = [
        'name', 'name_hi', 'quantity',
        'category', 'category_hi',
        'image', 'description', 'description_hi',
        'specifications', 'specifications_hi', 'order',
    ]
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
    fields = ['name', 'designation', 'designation_hi', 'staff_type', 'team', 'quantity', 'order']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'document_type', 'get_file_size', 'uploaded_at', 'order']
    list_filter = ['document_type', 'uploaded_at']
    list_editable = ['order']
    search_fields = ['title', 'description']
    readonly_fields = ['uploaded_at', 'get_file_size']
    fields = ['title', 'title_hi', 'document_type', 'file', 'description', 'description_hi', 'order', 'uploaded_at', 'get_file_size']
    
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
        'title', 'title_hi',
        'subtitle', 'subtitle_hi',
        'tagline', 'tagline_hi',
        'media_type', 'video',
        'button_text', 'button_text_hi', 'button_url',
        'secondary_button_text', 'secondary_button_text_hi', 'secondary_button_url',
        'is_active', 'order',
    ]
