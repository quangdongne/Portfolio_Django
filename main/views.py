from django.shortcuts import render
from django.contrib import messages
from .models import (UserProfile, Testimonial, Service,
                     Qualification, Portfolio, Skill, Service_Detail)

from django.views import generic

from . forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        services = Service.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)
        qualifications = Qualification.objects.filter(is_active=True)

        context["testimonials"] = testimonials
        context["services"] = services
        context["qualications"] = qualifications
        context["portfolio"] = portfolio
        return context"""


class ContactView(generic.FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 'Cảm ơn tôi sẽ liên lạc lại bạn sớm nhất có thể!!')
        return super().form_valid(form)


class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "main/portfolio.html"

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class QualificationView(generic.ListView):
    model = Qualification
    template_name = "main/qualification.html"

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class SkillView(generic.ListView):
    model = Skill
    template_name = "main/skills.html"


class TestimonialView(generic.ListView):
    model = Testimonial
    template_name = "main/testimonial.html"

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class ServiceView(generic.ListView):
    model = Service
    template_name = "main/service.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = Service.objects.filter(is_active=True)
        context["services"] = services
        return context


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "main/portfolio_detail.html"


class AboutView(generic.TemplateView):
    model = UserProfile
    template_name = "main/about.html"


# Create your views here.
