from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from countdown.models import Image
import random

class IndexView(TemplateView):
    template_name = 'index_view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num'] = random.randint(4,6)
        return context

class ImageCreateView(CreateView):
    model = Image
    success_url = "/"
    fields = ('picture',)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)
