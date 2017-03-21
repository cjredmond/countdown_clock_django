from countdown.models import Countdown
from django import forms
from datetimewidget.widgets import DateTimeWidget

class testForm(forms.ModelForm):
    class Meta:
        model = Countdown
        fields = ['end_time']
        widgets = {
        'end_time': DateTimeWidget(attrs={'id': 'yourdatetimeid'}, usel10n = True, bootstrap_version=3)
        }
