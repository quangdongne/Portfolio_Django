from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Skill(models.Model):
    class Meta:
        verbose_name_plural = "Skills"
        verbose_name = "Skill"
    sort_id = models.CharField(max_length=5, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = "User Profiles"
        verbose_name = "User Profile"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    name = models.CharField(max_length=100, blank=True, null=True)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    about_bio = models.TextField(blank=True, null=True)
    about_image = models.ImageField(blank=True, null=True, upload_to="about")
    experience = models.IntegerField(default=1, blank=True, null=True)
    projects = models.IntegerField(default=5, blank=True, null=True)
    companies = models.IntegerField(default=1, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'


class ContactProfile(models.Model):
    class Meta:
        verbose_name_plural = "Contact Profiles"
        verbose_name = "Contact Profile"
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    project = models.CharField(verbose_name="Project", max_length=200)
    message = models.TextField(verbose_name="Message")

    def __str__(self) -> str:
        return self.name


class Testimonial(models.Model):
    class Meta:
        verbose_name_plural = "Testimonials"
        verbose_name = "Testimonial"
        ordering = ["name"]

    thumbnail = models.ImageField(
        blank=True, null=True, upload_to="testimonial")
    name = models.CharField(max_length=200, blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Media(models.Model):
    class Meta:
        verbose_name_plural = "Media Files"
        verbose_name = "Media File"
        ordering = ["name"]

    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = "Portfolios"
        verbose_name = "Portfolio"
        ordering = ["name"]

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    demo = models.FileField(blank=True, null=True, upload_to="portfolio_demo")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


class Qualification(models.Model):
    class Meta:
        verbose_name_plural = "Qualifications"
        verbose_name = "Qualification"
        ordering = ["year_from"]

    sort_id = models.CharField(max_length=3, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    sub_title = models.CharField(max_length=200, blank=True, null=True)
    year_from = models.IntegerField(blank=True, null=True)
    year_to = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class Service(models.Model):
    class Meta:
        verbose_name_plural = "Services"
        verbose_name = "Service"

    title = models.CharField(max_length=50, blank=True, null=True)
    title2 = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class Service_Detail(models.Model):
    class Meta:
        verbose_name_plural = "Service Details"
        verbose_name = "Service Detail"

    title = models.CharField(max_length=50, blank=True, null=True)
    desciption = models.CharField(max_length=200, blank=True, null=True)
    services = models.ForeignKey(
        Service, related_name="service_details", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

# Create your models here.
