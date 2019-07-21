from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_item = List.objects.all
            messages.success(request, ('item has been added To List'))
            return render(request, 'home.html', {'all_items': all_item})
    else:
        all_item = List.objects.all
        return render(request, 'home.html', {'all_items': all_item})


def about(request):
    my_name = "Bijoy Digital"
    return render(request, 'about.html', {'name': my_name})


def delete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('item has been Deleted'))
    return redirect('home')


def cross_off(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')


def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')


def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None,instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been edited!'))
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})

