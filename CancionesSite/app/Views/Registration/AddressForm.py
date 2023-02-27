from django import forms

class AddressForm(forms.Form):
    street = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Street'}))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Street'}))
    number =forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'House Number','min':0}))
    flat_number =forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Flat Number','min':0}))
    