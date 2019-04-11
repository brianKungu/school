from django import forms
from . models import About,Staff,Department,Club

class AboutForm(forms.ModelForm):
    class Meta:
        model=About
        fields=['motto','logo','mission','vision'

        ]

class StaffForm(forms.ModelForm):
    class Meta:
        model=Staff
        fields=['staff_name','id_number','contact','role']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields = ['department_name', 'department_head', 'sub_head']

class ClubForm(forms.ModelForm):
    class Meta:
        model=Club
        fields = ['club_name', 'description', 'patron']