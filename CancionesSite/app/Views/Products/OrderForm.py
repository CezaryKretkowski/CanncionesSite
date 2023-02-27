from django import forms

class OrderForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'E-mail'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}))
    street = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Street'}))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Post Code','maxlenght':'6'}))
    number =forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'House Number','min':0}))
    flat_number =forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Flat Number','min':0}))