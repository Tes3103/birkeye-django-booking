from django.shortcuts import render

# Create your views here.


def get_booking_list(request):
    return render(request, 'booking/index.html')
