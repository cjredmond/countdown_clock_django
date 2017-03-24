from countdown.models import Countdown, Image
from django import forms
from datetimewidget.widgets import DateTimeWidget
from django.core.mail import send_mail

class testForm(forms.ModelForm):
    class Meta:
        model = Countdown
        fields = ['end_time', 'email']
        widgets = {
        'end_time': DateTimeWidget(attrs={'id': 'yourdatetimeid'}, usel10n = True, bootstrap_version=3),
        }

class testImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['picture']
