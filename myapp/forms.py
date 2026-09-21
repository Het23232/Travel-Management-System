from django import forms
from .models import Payment, Booking

class PaymentForm(forms.ModelForm):
    expiry_month = forms.IntegerField(required=True)
    expiry_year = forms.IntegerField(required=True)

    class Meta:
        model = Payment
        fields = ['amount', 'cardholder_name', 'card_number', 'cvv']

    def clean(self):
        cleaned_data = super().clean()
        month = cleaned_data.get('expiry_month')
        year = cleaned_data.get('expiry_year')

        if month and year:
            from datetime import date
            try:
                cleaned_data['expiry_date'] = date(int(year), int(month), 1)
            except ValueError:
                raise forms.ValidationError("Invalid expiry date.")
        return cleaned_data
    
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ['booking']
