from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Confession, Comment


# Create your views here.
def index(request):
    all_confession_items = Confession.objects.all().order_by('-id')
    return render(request, 'freedomApp/index.html', {'all_items': all_confession_items})


# This function saves new confessions made by the user
def add_confession(request):
    # new_alias, new_confession = request.POST['user-alias', 'confession']
    new_alias = request.POST['user-alias']
    new_confession = request.POST['confession']
    new_item = Confession(user_alias=new_alias, confession=new_confession)
    new_item.save()
    return HttpResponseRedirect('/freedom-app/')


def confession(request, item_id):
    confession = get_object_or_404(pk=item_id)
    comments = Comment.objects.get(pk=item_id)
    return render(request, 'freedomApp/confession.html', {'confession': confession}, {'comments': comments})