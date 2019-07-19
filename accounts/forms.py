from django import forms
from django.contrib.auth import authenticate, get_user_model
from posts.models import Post


User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('User does not exits')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
            if not user.is_active:
                raise forms.ValidationError('User not acive')
            return super(UserLoginForm, self).clean(*args, **kwargs)



class UserRegisterForm(forms.ModelForm):

    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={'class':'form-control'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
        help_texts = {
            'username': None
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('Email already Exists')
        return email


class StatusForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class':'form-control'}))
    desc = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Post
        fields = [
            'title',
            'desc'
        ]
