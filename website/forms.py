from django import forms
from . models import About,Staff

class AboutForm(forms.ModelForm):
    class Meta:
        model=About
        fields=['motto','logo','mission','vision'

        ]

class StaffForm(forms.ModelForm):
    class Meta:
        model=Staff
        fields=['staff_name','id_number','contact','role']