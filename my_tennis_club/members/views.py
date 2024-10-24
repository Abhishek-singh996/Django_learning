from django.shortcuts import render
from django.template import loader
from .models import Member
from django.http import HttpResponse


# View to display all members
def members(request):
    mymembers = Member.objects.all()  # Fetch all members
    context = {
        'mymembers': mymembers,
    }
    return render(request, 'all_members.html', context)  # Use render shortcut

# View for the main page
def main(request):
    return render(request, 'main.html')  # Use render shortcut

# Updated testing view using render shortcut
def testing(request):
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],   
    }
    return render(request, 'templates.html', context)  # Use render shortcut

