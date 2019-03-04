from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, IntegerField, CharField, NumberInput
from allauth.account.forms import SignupForm

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):

    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )
    
    # zip_code = IntegerField(max_value=5)

    class Meta(forms.UserCreationForm.Meta):
        model = User
        zip_code = IntegerField(max_value=5)


    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])


class CustomSignupForm(SignupForm):
    zip_code = CharField(label="Zip Code",
                               max_length=5,
                               widget=NumberInput(
                                   attrs={'size': '5'}))

    def signup(self, request, user):
        user.zip_code = self.cleaned_data['zip_code']
        
        user.save()
        return user