from django import forms


from _test42.main.models import Profile
from _test42.main.widgets import CalendarWidget


class ProfileEditForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        widgets = {
            'bio': forms.Textarea(attrs={'cols':40, 'rows': 10}),
            'other': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
            'birth_date': CalendarWidget()
        }
