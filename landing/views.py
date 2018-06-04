from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SubscriberForm


def landing(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        new_form = form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'turn_the_page/index.html', locals())


def generic(request):
    return render(request, 'turn_the_page/generic.html', locals())


def elements(request):
    return render(request, 'turn_the_page/elements.html', locals())



