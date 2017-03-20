from django.shortcuts import render
from django.views.generic import TemplateView
import random

class IndexView(TemplateView):
    template_name = 'index_view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num'] = random.randint(4,6)
        return context
