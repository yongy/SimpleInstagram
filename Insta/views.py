from django.views.generic import TemplateView

# Create your views here.

class HellowWorld(TemplateView):
    template_name = 'home.html'