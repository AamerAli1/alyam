from django import forms

from management.models import UserUsed


class PasswordForm(forms.ModelForm):
    class Meta:
        model = UserUsed
        fields = ['name','passcode']
        