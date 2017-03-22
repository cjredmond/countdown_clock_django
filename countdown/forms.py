from countdown.models import Countdown
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
#
# class ContactForm(forms.Form):
#     sender = forms.CharField()
#     message = forms.CharField(widget=forms.Textarea)
#
#     def send_email(self):
#         sender = self.cleaned_data['sender']
#         message = self.cleaned_data['message']
#         subject = "Countdown Info"
#         body = """Thanks for creating a countdown!
#         From: {}
#         Message: {}
#                   """.format(sender, message)
#         recipient_list = ['connor.redmond@gmail.com']
#
#         send_main(subject,body,"connorthrowaway1@gmail.com",recipient_list)
