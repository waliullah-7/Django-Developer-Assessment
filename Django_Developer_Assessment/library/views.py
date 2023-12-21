from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import authorf , bookf
from .models import authorm, bookm
from django.db.models import Avg, Count

# Create your views here.
def authorv(request):
    fa = authorf()
    if request.method == 'POST':
        fa = authorf(request.POST)
        if fa.is_valid():
            fa.save()
            return HttpResponseRedirect('/')
    else:
        fa=authorf()
    return render (request, 'library/author.html', {'form':fa,})

def bookv(request):
    fb = bookf()

    if request.method == 'POST':
        fb = bookf(request.POST)
        if fb.is_valid():
            fb.save()
            return HttpResponseRedirect('/')
    else:
        fb = bookf()
    return render (request, 'library/book.html', {'frm':fb})

# This Function will Delete
def delete_data(request, id):
 if request.method == 'POST':
  pi = authorm.objects.get(pk=id)
  pi.delete()
  return HttpResponseRedirect('/')
 

def delete_databook(request, id):
 if request.method == 'POST':
  pi = bookm.objects.get(pk=id)
  pi.delete()
  return HttpResponseRedirect('/')


# This Function will Update
def update_data(request, id):
    pi = authorm.objects.get(pk=id)

    if request.method == 'POST':
        fa = authorf(request.POST, instance=pi)

        if fa.is_valid():
            fa.save()
            return HttpResponseRedirect('/')
    else:
        fa = authorf(instance=pi)
        # fa = authorf()
    return render(request, 'library/updateauthor.html', {'form': fa,})

def update_databook(request, id):
    pi = bookm.objects.get(pk=id)

    if request.method == 'POST':
        fb = bookf(request.POST, instance=pi)

        if fb.is_valid():
            fb.save()
            return HttpResponseRedirect('/')

    else:
        fb = bookf(instance=pi)
        # fb = bookf()
    return render(request, 'library/updatebook.html', {'form': fb,})




def dashboard (request):
    fa = authorf()
    if request.method == 'POST':
        fa = authorf(request.POST)
        if fa.is_valid():
            fa.save()
    else:
        fa=authorf()
    auth = authorm.objects.all()
    bok = bookm.objects.all()
    print(auth)
    return render (request , 'library/dashboard.html', {'aut':auth, 'book':bok})

def aggregationv (request):
    totl = bookm.objects.count()
    price_average = bookm.objects.aggregate(avg_price=Avg("price"))['avg_price']
    old = bookm.objects.order_by('pb_year').first()
    new = bookm.objects.order_by('-pb_year').first()

    return render (request , 'library/aggregation.html', {'total':totl, 'prav':price_average, 'oold':old, 'neww':new} )