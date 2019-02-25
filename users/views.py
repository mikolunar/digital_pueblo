from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'User created!')

        else:
            messages.error(request, f'Error while creating user!')
            render(request, 'registration/register.html', {'form': form})

    else:
        form = UserCreationForm()
    context = {
        'form': form

    }

    return render(request, 'registration/register.html', context)
