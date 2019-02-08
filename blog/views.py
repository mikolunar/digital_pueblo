
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from . forms import BlogForm
from . models import Blog


# Create your views here.

def blogHome(request):

    queryset = Blog.objects.all()
    print(queryset)
    return render(request, 'blog/blog.html', {'context': queryset})


def blogView(request, pk):
    instance = Blog.objects.get(pk=int(pk))
    fields = instance._meta.get_fields()
    item = {}
    for field in fields:
        item[str(field.name)] = str(getattr(instance, field.name))

    print(item)
    return render(request, 'blog/blog_view.html', {'item': item, 'id': int(pk)})


def blogNew(request):

    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('blog_home')
        else:
            form = BlogForm(request.POST)
            if form.is_valid():
                instance = form.save()
                return redirect('blog_view', instance.pk)

    form = BlogForm(request.POST or None)
    context = {'form': form}

    return render(request, 'blog/blog_new.html', context)


def blogEdit(request, pk):

    if request.method == 'POST':

        if "cancel" in request.POST:
            return redirect('blog_view', pk)
        else:
            form = BlogForm(request.POST)
            if form.is_valid():
                instance = form.save()
                return redirect('blog_view', instance.pk)
            else:
                return redirect('blog_view', pk)
    else:

        instance = Blog.objects.get(pk=int(pk))
        form = BlogForm(request.POST or None, instance=instance)

    return render(request, 'blog/blog_edit.html', {'form': form})
