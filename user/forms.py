from django import forms
from django.contrib.auth.models import User


class UserInfo(forms.Form):
    CHOICES = (('A+', 'A+'),
             ('B+', 'B+'),
             ('A-', 'A-'),
             ('B-', 'B-'),
             ('AB+', 'AB+'),
             ('AB-', 'AB-'),
             ('O+', 'O+'),
             ('O-', 'O-'))

    name = forms.CharField(max_length=50, required=True,
                         widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Full Name'}))
    age = forms.CharField(max_length=2, required=True,
                         widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Age'}))
    email = forms.EmailField(max_length=50, required=True,
                          widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Email'}))
    address = forms.CharField(max_length=50, required=True,
                            widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Address'}))
    contact_number = forms.CharField(max_length=30, required=True,
                      widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Contact Number'}))
    blood_group = forms.ChoiceField(required=True,
               widget=forms.Select(attrs={'class' : 'form-control','placeholder' : 'Blood Group'}), choices=CHOICES)



class RegisterForm(forms.ModelForm):
    '''first_name = forms.CharField(label="", max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter First Name' }))
    last_name = forms.CharField(label="", max_length=20,  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Last Name'}))'''
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Username'}), help_text='<ul class="form-text text-muted small"><li>Must be combination of letters, digits and ./-/_ only.</li></ul>')
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password'}), help_text='<ul class="form-text text-muted small"><li>Must contain at least 8 characters.</li><li>Must be combination of letters, digits and special-characters.</li></ul>')
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}), help_text='<ul class="form-text text-muted small"><li>Enter the same password as above.</li></ul>')

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Password Mismatch")
        return password2 

    def save(self, commit=True):
        user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password1'])
        return user


class EditProfileForm(forms.ModelForm):
  password = forms.CharField(label="", widget=forms.TextInput(attrs={'type':'hidden'}))

  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'username', 'password',)
