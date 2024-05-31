from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('portfolio/', views.PortfolioView.as_view(), name="portfolio"),
    path('portfolio/<slug:slug>',
         views.PortfolioDetailView.as_view(), name="portfolio_detail"),
    path('testimonial/', views.TestimonialView.as_view(), name="testimonial"),
    path('service/', views.ServiceView.as_view(), name="service"),
    path('skills/', views.SkillView.as_view(), name="skill"),
    path('qualification/', views.QualificationView.as_view(), name="qualification"),
    path('contact/', views.ContactView.as_view(), name="contact"),



]
