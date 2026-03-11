from django.db import models

# Company Information Model
class CompanyInfo(models.Model):
    name = models.CharField(max_length=200, default="Shivam Construction Company")
    tagline = models.CharField(max_length=300, default="Civil Contractor & General Order Suppliers")
    phone = models.CharField(max_length=20, default="6350092193")
    email = models.EmailField(default="scccompany91@gmail.com")
    address = models.TextField(default="SHOP NO. 05, NEAR INDANE GAS OFFICE, BASANT VIHAR COLONY, SURATGARH, SRI GANGANAGAR, RAJASTHAN, 335804")
    vision = models.TextField(blank=True)
    quality_policy = models.TextField(blank=True)
    introduction = models.TextField(blank=True)
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
    image = models.ImageField(upload_to='gallery/')
    image_type = models.CharField(max_length=20, choices=IMAGE_TYPES, default='general')
    description = models.TextField(blank=True)
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
    description = models.TextField()
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Key Persons"
    
    def __str__(self):
        return f"{self.name} - {self.role}"

# Services Model
class Service(models.Model):
    SERVICE_CATEGORIES = [
        ('industrial', 'Industrial and Commercial Buildings'),
        ('civil', 'Civil'),
        ('piping', 'Cross Country Piping'),
    ]
    
    category = models.CharField(max_length=50, choices=SERVICE_CATEGORIES)
    title = models.CharField(max_length=200)
    description = models.TextField()
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
    wo_reference = models.CharField(max_length=200)
    type_of_work = models.CharField(max_length=300)
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
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='equipment/', blank=True, null=True)
    description = models.TextField(blank=True)
    specifications = models.TextField(blank=True, help_text="Technical specifications")
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
    description = models.TextField(blank=True)
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
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    file = models.FileField(upload_to='documents/%Y/%m/')
    description = models.TextField(blank=True)
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
