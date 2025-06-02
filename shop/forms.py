from django import forms

class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="First Name")
    last_name = forms.CharField(max_length=50, label="Last Name")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(max_length=20, label="Phone Number", required=False)
    address = forms.CharField(max_length=255, label="Shipping Address")
    city = forms.CharField(max_length=100, label="City")
    postal_code = forms.CharField(max_length=20, label="Postal Code")
    country = forms.CharField(max_length=100, label="Country")