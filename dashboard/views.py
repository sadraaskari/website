from django.shortcuts import render, redirect
from .forms import StudentTicketForm
from users.models import UserProfile
from .models import Option, Ticket


def home(request):
    dash = {
        'title': 'Dashboard',
        'heading': 'Dashboard',
        'subheading': 'This is the dashboard page.',
    }
    context = {
        'dash': dash
    }
    return render(request, 'dashboard/home.html', context)


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
