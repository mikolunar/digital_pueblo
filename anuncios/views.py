from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


from django.contrib import messages


from rest_framework import generics

from django.http import HttpResponse

from . models import Anuncio
from . serializers import AnuncioSerializer

from . forms import AddAnuncioForm, EditAnuncioForm, ContactForm


class AnunciosListAPI(generics.ListAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer


class AnunciosDetailsAPI(generics.RetrieveDestroyAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer


# def anuncioView(request):
#     queryset = Anuncio.objects.all()
#     html = "<HTML> <HEAD></HEAD> <body> Anuncios: %s </body> </HMLT>" % queryset[0].title
#     return HttpResponse(html)

def anuncioView(request, pk):
    item = get_object_or_404(Anuncio, pk=int(pk))

    return render(request, 'anuncios/anuncio.html', {'item': item})


def anunciosView(request):
    queryset = Anuncio.objects.all()
    return render(request, 'anuncios/anuncios.html', {'context': queryset})


def anuncioRem(request, pk):
    item = Anuncio.objects.get(pk=int(pk))
    return render(request, 'anuncios/anuncio_rem.html', {'item': item})


def anuncioEdit(request, pk):

    if request.method == 'POST':

        form = EditAnuncioForm(request.POST)

        if form.is_valid():
            form.save()  # it breaks here
            messages.success(request, f'Anuncio saved!')
            return redirect('anuncios')

        else:
            item = {}
            try:
                item['id'] = pk
                item['pk'] = pk
                item['title'] = request.POST['title']
                item['subtitle'] = request.POST['subtitle']
                item['email'] = request.POST['email']
                item['location'] = request.POST['location']
            except (KeyError):
                instance = Anuncio.objects.get(pk=int(pk))
                return render(request, 'anuncios/anuncio_edit.html', {'item': instance})

            messages.error(request, f'Error in form validation')
            return render(request, 'anuncios/anuncio_edit.html', {'item': item})
    else:

        item = Anuncio.objects.get(pk=int(pk))

        return render(request, 'anuncios/anuncio_edit.html', {'item': item})


def anuncioDel(request, pk):
    instance = Anuncio.objects.get(id=pk).delete()
    messages.warning(request, f'Anuncio deleted!')
    return redirect('anuncios')


def anuncioNew(request):

    if request.method == 'POST':
        form = AddAnuncioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Anuncio created!')
            return redirect('anuncios')
        else:
            messages.error(request, f'Error in form validation!')
            return render(request, 'anuncios/post_edit.html', {'form': form})

    else:
        form = AddAnuncioForm()

    return render(request, 'anuncios/post_edit.html', {'form': form})


def contactView(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['mikolunar@gmail.com']
            if cc_myself:
                recipients.append('mr@marcinros.net')
            # from django.core.mail import send_mail
            # send_mail(subject, message, sender, recipients)
            # send data
            return render(request, 'contact_thanks.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})