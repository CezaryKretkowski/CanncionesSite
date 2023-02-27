from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label="User Name",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'User name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'E-mail'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'Pass','class':'form-control','placeholder':'Password',
                                ' pattern':'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}'}))
    confirmPassword = forms.CharField(label="Confirm password",widget=forms.PasswordInput(attrs={'id':'confirmPass','class':'form-control','placeholder':'Confirm password'}))
    street = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Street'}))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Post Code','maxlenght':'6'}))
    number =forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'House Number','min':0}))
    flat_number =forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Flat Number','min':0}))
    