from django import forms
from django.core import validators
from first_app.models import HotelChain#,Hotel

def check_valid_z(value):
    if value[0] !='Z':
        raise forms.ValidationError("loi rôi nè")

class FormLogin(forms.Form):
    username = forms.CharField(required=False, validators=[check_valid_z])
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    verifyemail = forms.EmailField(label='Please enter email again:')
    note = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)]
                                 )
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verifyemail = all_clean_data['verifyemail']
        if email != verifyemail:
            raise forms.ValidationError("email not match")

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        print('sssssw ewr')
        print(len(botcatcher))
        if len(botcatcher) > 0:
            raise forms.ValidationError("loi rôi nè")
        return botcatcher


class FormNewChain(forms.ModelForm):
    class Meta:
        model = HotelChain
        fields = '__all__'