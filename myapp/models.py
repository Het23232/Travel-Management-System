# models.py
from django.db import models

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    travel_date = models.DateField()
    location = models.CharField(max_length=100)
    hotel_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name} - {self.hotel_name}"

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    cardholder_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    expiry_month = models.CharField(max_length=2)
    expiry_year = models.CharField(max_length=4)
    cvv = models.CharField(max_length=4)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of ₹{self.amount} by {self.cardholder_name}"
