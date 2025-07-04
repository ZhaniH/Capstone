from django import forms

class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label='Your Message')