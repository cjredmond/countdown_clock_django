from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View
from django.views.generic.edit import CreateView, FormView, DeleteView, UpdateView
from countdown.models import Image, Countdown
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse, reverse_lazy
from countdown.forms import testForm
from django.core.mail import send_mail
import random
import uuid

class ImageCreateView(CreateView):
    model = Image
    fields = ('picture',)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_images'] = Countdown.objects.get(management_slug=self.kwargs['pk']).list_pictures()
        context['countdown'] = Countdown.objects.get(management_slug=self.kwargs['pk'])
        return context
    def get_success_url(self, **kwargs):
        return reverse('image_create_view', kwargs={'pk': self.kwargs['pk']})
    def form_valid(self, form):
        subject = Countdown.objects.get(management_slug=str(self.kwargs['pk']))
        instance = form.save(commit=False)
        instance.countdown = subject
        return super().form_valid(form)

class ImageDeleteView(DeleteView):
    model = Image
    success_url = "/"

class PassThroughView(View):
    def post(self, request):
        code = request.POST['code']
        try:
            target = Countdown.objects.get(management_slug=code)
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse('countdown_create_view'))
        return HttpResponseRedirect(reverse('image_create_view', kwargs={'pk': target.management_slug}))

class CountdownCreateView(CreateView):
    model = Countdown
    form_class = testForm
    def get_success_url(self):
        target = Countdown.objects.last()
        return reverse('image_create_view', kwargs={'pk': target.management_slug })
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.base_slug = uuid.uuid4()
        instance.management_slug = uuid.uuid4()
        send_mail(
        'URLS',
        'base url: begincount.com/countdown/{}\nmanagement url: begincount.com/manage/{}'.format(instance.base_slug, instance.management_slug),
        'connorthrowaway1@gmail.com',
        'start@begincount.com',
        ['{}'.format(instance.email)],
        fail_silently=False
        )
        return super().form_valid(form)

class CountdownView(TemplateView):
    template_name = 'countdown_view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Countdown.objects.filter(base_slug=self.kwargs['pk']):
            countdown = Countdown.objects.get(base_slug=self.kwargs['pk'])
            context['countdown'] = countdown
            if countdown.list_pictures():
                context['background'] = random.choice(countdown.list_pictures())
            context['end'] = countdown.end_time.strftime("%B %d %Y %H:%M %Z")
        return context
