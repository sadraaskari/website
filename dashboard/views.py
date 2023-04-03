from django.shortcuts import render, redirect
from .forms import StudentTicketForm
from users.models import UserProfile
from .models import Option, Ticket, SliderImage
from courses.models import Tutorial


def home(request):
    slider_images = SliderImage.objects.all()
    tutorials = Tutorial.objects.all()

    context = {
        'slider_images': slider_images,
        'tutorials': tutorials,
    }
    return render(request, 'dashboard/dashboard.html', context)


def card_slider(request):
    users = UserProfile.objects.all()

    context = {
        'users': users,
    }
    return render(request, 'dashboard/cardslider.html', context)


def about(request):
    return render(request, 'dashboard/podcast.html', {'title': 'About'})


def ticket(request):
    if request.method == 'POST':
        form = StudentTicketForm(request.POST)
        form.instance.sender = UserProfile.objects.get(user=request.user)
        form.instance.receiver = UserProfile.objects.get(user__id=Option.objects.get(option_key='ticket_receiver').option_value)
        if form.is_valid():
            form.save()
            return redirect('dashboard-home')
    else:
        form = StudentTicketForm()
    return render(request, 'dashboard/ticket.html', {'form': form})


def all_tickets(request):
    tickets_sent = Ticket.objects.filter(sender=request.user.userprofile)
    tickets_received = Ticket.objects.filter(receiver=request.user.userprofile)

    return render(request, 'dashboard/all_tickets.html', {'tickets_sent': tickets_sent, 'tickets_received': tickets_received})

