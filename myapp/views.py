from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm, PaymentForm
from .models import Booking, Payment

# Price mapping based on destination
DESTINATION_PRICES = {
    'France': '165000',
    'UK': '185000',
    'Dubai': '55000',
    'Italy': '145000',
    'Kashmir': '32500',
    'US': '225000',
    'Seville': '135000',
    'Singapore': '52000',
    'Turkey': '85000',
    'China': '95000',
    'Germany': '155000',
    'Monaco City': '240000',
}

def home(request):
    return render(request, 'Index.html')

def booking(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        travel_date = request.POST.get('date')  # from HTML input name
        location = request.POST.get('location')
        hotel_name = request.POST.get('hotelName')

        booking = Booking.objects.create(
            full_name=full_name,
            email=email,
            travel_date=travel_date,
            location=location,
            hotel_name=hotel_name
        )
        return redirect('payment_view', booking_id=booking.id)

    # GET request: Capture pre-selected location from URL query (e.g. ?location=US)
    selected_location = request.GET.get('location', '')
    default_price = DESTINATION_PRICES.get(selected_location, '')

    return render(request, 'booking.html', {
        'selected_location': selected_location,
        'default_price': default_price
    })

def payment_view(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    
    # Automatically resolve the fixed amount based on the booking's location
    amount = DESTINATION_PRICES.get(booking.location, '0')

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            print("✅ Payment form is valid.")
            payment = form.save(commit=False)
            payment.booking = booking
            payment.amount = amount  # Assign auto-calculated amount
            payment.save()
            return redirect('payment_success')
        else:
            print("❌ Payment form is invalid:", form.errors)
    else:
        form = PaymentForm()

    return render(request, 'payment.html', {
        'form': form, 
        'booking': booking,
        'location': booking.location,
        'hotelName': booking.hotel_name,
        'fullName': booking.full_name,
        'amount': amount
    })

def payment_success(request):
    return render(request, 'payment_success.html')

def index_red(request):
    return render(request, 'Day 2/index-red.html')

def france_view(request):
    return render(request, 'France.html')

def france_details1(request):
    return render(request, 'Images/France/Details1.html')

def france_details2(request):
    return render(request, 'Images/France/Details2.html')

def france_details3(request):
    return render(request, 'Images/France/Details3.html')

def france_details4(request):
    return render(request, 'Images/France/Details4.html')

def germany_view(request):
    return render(request, 'Germany.html')

def germany_details1(request):
    return render(request, 'Images/Germany/Details1.html')

def germany_details2(request):
    return render(request, 'Images/Germany/Details2.html')

def germany_details3(request):
    return render(request, 'Images/Germany/Details3.html')

def germany_details4(request):
    return render(request, 'Images/Germany/Details4.html')

def dubai_view(request):
    return render(request, 'dubai.html')

def US_view(request):
    return render(request, 'US.html')

def italy_view(request):
    return render(request, 'Italy.html')

def Kashmir_view(request):
    return render(request, 'Kashmir.html')

def seville_view(request):
    return render(request, 'Seville.html')

def singapore_view(request):
    return render(request, 'Singapore.html')

def turkey_view(request):
    return render(request, 'Turkey.html')

def china_view(request):
    return render(request, 'China.html')

def Monaco_City_view(request):
    return render(request, 'Monaco City.html')

def UK_view(request):
    return render(request, 'UK.html')

def uk_details1(request):
    return render(request, 'Images/UK/Details1.html')

def uk_details2(request):
    return render(request, 'Images/UK/Details2.html')       

def uk_details3(request):
    return render(request, 'Images/UK/Details3.html')

def uk_details4(request):
    return render(request, 'Images/UK/Details4.html')

def explore(request):
    return render(request, 'index-red.html')  # or 'Day 2/index-red.html' depending on your templates path