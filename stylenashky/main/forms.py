from django import forms

from .models import Customer


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['user_tel']
        widgets = {'user_tel': forms.TextInput(attrs={'type': 'tel',
                                                      'placeholder': '+375 (_ _) _ _ _-_ _-_ _',
                                                      'value': '+375'})
                   }
