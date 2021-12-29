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
    confession = get_object_or_404(Confession, pk=item_id)
    target = Confession.objects.get(pk=item_id)
    comments = Comment.objects.filter(target=target.id).order_by('-comment_timestamp')
    # comments = Comment.objects.filter(target=Confession.objects.get(pk=item_id))
    return render(request, 'freedomApp/confession.html', {'item': confession, 'comments': comments})


# This function saves a new comment in a specific confession thread
def add_comment(request):
    target_id = request.POST['item-id']
    new_comment_alias = request.POST['commenter-alias']
    new_comment_body = request.POST['comment-body']
    new_comment = Comment(target=Confession.objects.get(pk=target_id), commenter_name=new_comment_alias, comment_body=new_comment_body)
    new_comment.save()
    return HttpResponseRedirect('/freedom-app/confession/' + target_id)