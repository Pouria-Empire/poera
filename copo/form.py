from django import forms
from copo.models import Questions
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['title', 'description', 'test']


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('User is not active')
            return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='username')
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(label='Email Address')
    phone = forms.CharField(label='Phone number')

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'phone',
            'email'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('This email is already being used')
        return email
