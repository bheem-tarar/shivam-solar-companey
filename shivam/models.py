from django.db import models
from django.core.exceptions import ValidationError

# Company Information Model
class CompanyInfo(models.Model):
    name = models.CharField(max_length=200, default="Shivam Construction Company")
    tagline = models.CharField(max_length=300, default="Road Earthwork, Soil Leveling & Canal Lining Contractor")
    tagline_hi = models.CharField(max_length=300, blank=True, verbose_name="Tagline (Hindi)")
    phone = models.CharField(max_length=20, default="6350092193")
    email = models.EmailField(default="scccompany91@gmail.com")
    address = models.TextField(default="BUILDING NO./FLAT NO.: MEEL COLONY KE SAMANE, ROAD/STREET: WARD NO. 03 NEW, CITY/TOWN/VILLAGE: SURATGARH, DISTRICT: SRI GANGANAGAR, STATE: RAJASTHAN, PIN CODE: 335804")
    address_hi = models.TextField(blank=True, verbose_name="Address (Hindi)")
    vision = models.TextField(blank=True)
    vision_hi = models.TextField(blank=True, verbose_name="Vision (Hindi)")
    quality_policy = models.TextField(blank=True)
    quality_policy_hi = models.TextField(blank=True, verbose_name="Quality Policy (Hindi)")
    introduction = models.TextField(blank=True)
    introduction_hi = models.TextField(blank=True, verbose_name="Introduction (Hindi)")
    logo = models.ImageField(upload_to='company/', blank=True, null=True)
    hero_image = models.ImageField(upload_to='company/', blank=True, null=True)
    instagram_url = models.URLField(blank=True, default="https://www.instagram.com/shivamconstruction")
    services_bg = models.ImageField(upload_to='company/backgrounds/', blank=True, null=True, verbose_name="Services Page Background")
    projects_bg = models.ImageField(upload_to='company/backgrounds/', blank=True, null=True, verbose_name="Projects Page Background")
    equipment_bg = models.ImageField(upload_to='company/backgrounds/', blank=True, null=True, verbose_name="Equipment Page Background")
    vision_bg = models.ImageField(upload_to='company/backgrounds/', blank=True, null=True, verbose_name="Vision Section Background")
    quality_bg = models.ImageField(upload_to='company/backgrounds/', blank=True, null=True, verbose_name="Quality Section Background")
    team_bg = models.ImageField(upload_to='company/backgrounds/', blank=True, null=True, verbose_name="Team Page Background")
    contact_bg = models.ImageField(upload_to='company/backgrounds/', blank=True, null=True, verbose_name="Contact Page Background")
    
    class Meta:
        verbose_name_plural = "Company Information"
    
    def __str__(self):
        return self.name

# Image Gallery Model for various images
class CompanyImage(models.Model):
    IMAGE_TYPES = [
        ('intro', 'Introduction Images'),
        ('vision', 'Vision Images'),
        ('quality', 'Quality Policy Images'),
        ('service', 'Service Images'),
        ('project', 'Project Images'),
        ('equipment', 'Equipment Images'),
        ('team', 'Team Images'),
        ('general', 'General Images'),
    ]
    
    title = models.CharField(max_length=200)
    title_hi = models.CharField(max_length=200, blank=True, verbose_name="Title (Hindi)")
    image = models.ImageField(upload_to='gallery/')
    image_type = models.CharField(max_length=20, choices=IMAGE_TYPES, default='general')
    description = models.TextField(blank=True)
    description_hi = models.TextField(blank=True, verbose_name="Description (Hindi)")
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['image_type', 'order', '-created_at']
        verbose_name_plural = "Company Images"
    
    def __str__(self):
        return f"{self.get_image_type_display()} - {self.title}"

# Key Persons Model
class KeyPerson(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    role_hi = models.CharField(max_length=200, blank=True, verbose_name="Role (Hindi)")
    description = models.TextField()
    description_hi = models.TextField(blank=True, verbose_name="Description (Hindi)")
    photo = models.ImageField(upload_to='team/', blank=True, null=True, verbose_name="Photo / CEO image")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Key Persons"
    
    def __str__(self):
        return f"{self.name} - {self.role}"

# Services Model
class Service(models.Model):
    SERVICE_CATEGORIES = [
        ('road', 'Road Earthwork & Soil Leveling'),
        ('bridge', 'Bridge & Flyover Earthwork'),
        ('canal', 'Canal & Nahar Lining (Rajasthan)'),
    ]
    
    category = models.CharField(max_length=50, choices=SERVICE_CATEGORIES)
    title = models.CharField(max_length=200)
    title_hi = models.CharField(max_length=200, blank=True, verbose_name="Title (Hindi)")
    description = models.TextField()
    description_hi = models.TextField(blank=True, verbose_name="Description (Hindi)")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order']
        verbose_name_plural = "Services"
    
    def __str__(self):
        return f"{self.get_category_display()} - {self.title}"

# Project Model (Updated to include all project types)
class CompletedProject(models.Model):
    PROJECT_STATUS = [
        ('completed', 'Project Completed'),
        ('on_hand', 'Project On Hand'),
        ('ongoing', 'Ongoing Projects'),
    ]
    
    work_awarded_by = models.CharField(max_length=200)
    work_awarded_by_hi = models.CharField(max_length=200, blank=True, verbose_name="Work Awarded By (Hindi)")
    wo_reference = models.CharField(max_length=200)
    type_of_work = models.CharField(max_length=300)
    type_of_work_hi = models.CharField(max_length=300, blank=True, verbose_name="Type of Work (Hindi)")
    date = models.DateField()
    status = models.CharField(max_length=20, choices=PROJECT_STATUS, default='completed')
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-date', 'order']
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return f"{self.work_awarded_by} - {self.type_of_work}"

# Equipment Model
class Equipment(models.Model):
    name = models.CharField(max_length=200)
    name_hi = models.CharField(max_length=200, blank=True, verbose_name="Name (Hindi)")
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=100, blank=True)
    category_hi = models.CharField(max_length=100, blank=True, verbose_name="Category (Hindi)")
    image = models.ImageField(upload_to='equipment/', blank=True, null=True)
    description = models.TextField(blank=True)
    description_hi = models.TextField(blank=True, verbose_name="Description (Hindi)")
    specifications = models.TextField(blank=True, help_text="Technical specifications")
    specifications_hi = models.TextField(blank=True, verbose_name="Specifications (Hindi)")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order']
        verbose_name_plural = "Equipment"
    
    def __str__(self):
        return f"{self.name} ({self.quantity})"

# Equipment Images Model
class EquipmentImage(models.Model):
    equipment = models.ForeignKey(Equipment, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='equipment/images/')
    title = models.CharField(max_length=200, blank=True)
    title_hi = models.CharField(max_length=200, blank=True, verbose_name="Title (Hindi)")
    description = models.TextField(blank=True)
    description_hi = models.TextField(blank=True, verbose_name="Description (Hindi)")
    order = models.IntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['equipment', 'order', '-uploaded_at']
        verbose_name_plural = "Equipment Images"
    
    def __str__(self):
        return f"{self.equipment.name} - Image {self.order + 1}"

# Staff Model
class Staff(models.Model):
    STAFF_TYPES = [
        ('site', 'Site Staff'),
        ('central', 'Central Planner'),
    ]
    
    name = models.CharField(max_length=200, blank=True)
    designation = models.CharField(max_length=200)
    designation_hi = models.CharField(max_length=200, blank=True, verbose_name="Designation (Hindi)")
    staff_type = models.CharField(max_length=20, choices=STAFF_TYPES)
    team = models.CharField(max_length=50, blank=True)
    quantity = models.IntegerField(default=1)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['staff_type', 'order']
        verbose_name_plural = "Staff"
    
    def __str__(self):
        return f"{self.designation} - {self.get_staff_type_display()}"

# Documents Model
class Document(models.Model):
    DOCUMENT_TYPES = [
        ('work', 'Complete Work Documents'),
        ('experience', 'Experience Documents'),
        ('payment', 'Payment Documents'),
        ('certificate', 'Certificates'),
        ('other', 'Other Documents'),
    ]
    
    title = models.CharField(max_length=200)
    title_hi = models.CharField(max_length=200, blank=True, verbose_name="Title (Hindi)")
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    file = models.FileField(upload_to='documents/%Y/%m/')
    description = models.TextField(blank=True)
    description_hi = models.TextField(blank=True, verbose_name="Description (Hindi)")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['document_type', 'order', '-uploaded_at']
        verbose_name_plural = "Documents"
    
    def __str__(self):
        return f"{self.get_document_type_display()} - {self.title}"
    
    def get_file_size(self):
        """Return file size in human readable format"""
        try:
            size = self.file.size
            for unit in ['B', 'KB', 'MB', 'GB']:
                if size < 1024.0:
                    return f"{size:.1f} {unit}"
                size /= 1024.0
            return f"{size:.1f} TB"
        except:
            return "Unknown"
    
    def get_file_extension(self):
        """Return file extension"""
        try:
            return self.file.name.split('.')[-1].upper()
        except:
            return "FILE"


class ContactMessage(models.Model):
    """Messages submitted from the Contact Us page."""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.email}"


class HomeBanner(models.Model):
    """Homepage banners (video only)."""
    MEDIA_TYPES = [
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=200)
    title_hi = models.CharField(max_length=200, blank=True, verbose_name="Title (Hindi)")
    subtitle = models.CharField(max_length=300, blank=True)
    subtitle_hi = models.CharField(max_length=300, blank=True, verbose_name="Subtitle (Hindi)")
    tagline = models.CharField(max_length=300, blank=True)
    tagline_hi = models.CharField(max_length=300, blank=True, verbose_name="Tagline (Hindi)")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, default='video')
    image = models.ImageField(upload_to='banners/images/', blank=True, null=True)
    video = models.FileField(upload_to='banners/videos/', blank=True, null=True)
    button_text = models.CharField(max_length=80, blank=True, default='Learn More')
    button_text_hi = models.CharField(max_length=80, blank=True, verbose_name="Button Text (Hindi)")
    button_url = models.CharField(max_length=300, blank=True, default='/projects/')
    secondary_button_text = models.CharField(max_length=80, blank=True, default='Contact Us')
    secondary_button_text_hi = models.CharField(max_length=80, blank=True, verbose_name="Secondary Button (Hindi)")
    secondary_button_url = models.CharField(max_length=300, blank=True, default='/contact/')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name_plural = "Home Banners"

    def __str__(self):
        return self.title

    def clean(self):
        if not self.video:
            raise ValidationError("Please upload a video file for this banner.")

    def save(self, *args, **kwargs):
        # Enforce video-only behavior for all HomeBanner entries.
        self.media_type = 'video'
        super().save(*args, **kwargs)
