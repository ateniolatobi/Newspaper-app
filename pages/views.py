# users/views.py
from django.urls import reverse_lazy
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"

# class (TemplateView):
#     template_name = "TEMPLATE_NAME"
# CLASS_NAME
