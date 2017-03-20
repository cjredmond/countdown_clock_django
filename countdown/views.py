from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View
from django.views.generic.edit import CreateView
from countdown.models import Image, Countdown
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse, reverse_lazy
import random
import uuid

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
        subject = countdown.objects.get(management_slug=self.request['pk'])
        instance = form.save(commit=False)
        instance.countdown = subject
        return super().form_valid(form)

class PassThroughView(View):
    def post(self, request):
        code = request.POST['code']
        try:
            target = Countdown.objects.get(management_slug=code)
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse('index_view'))
        # return HttpResponseRedirect(reverse('image_create_view', args=target.management_slug))
        return HttpResponseRedirect('http://localhost:8000/add_image/{}/'.format(code))
class CountdownCreateView(CreateView):
    model = Countdown
    success_url = "/"
    fields = []

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.base_slug = uuid.uuid4()
        instance.management_slug = uuid.uuid4()
        return super().form_valid(form)

class CountdownView(TemplateView):
    template_name = 'countdown_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Countdown.objects.filter(base_slug=self.kwargs['pk']):
            context['countdown'] = Countdown.objects.get(base_slug=self.kwargs['pk'])
        return context
