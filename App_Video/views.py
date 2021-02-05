from django.shortcuts import redirect, render,HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from . import models
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
class Home(ListView):
    context_object_name='videos'
    model=models.Item
    template_name='App_Video/Home.html'
    
    
@login_required
def detail_view(request,pk):
    videos=models.Item.objects.get(pk=pk)
    commentform=CommentForm()
    if request.method =='POST':
        commentform=CommentForm(data=request.POST)
        if commentform.is_valid():
            comment=commentform.save(commit=False)
            comment.video=videos
            comment.user=request.user
            comment.save()
            messages.success(request,'You Have Commented Successfully')
            return HttpResponseRedirect(reverse('App_Video:details',kwargs={'pk':pk}))
    return render(request,'App_Video/FullVideo.html',context={'video':videos,'form':commentform})
    
    
