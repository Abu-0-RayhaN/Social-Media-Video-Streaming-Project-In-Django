from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Posts,Like,Comment
from .forms import CommentForm,PostForm
def post(request):
    post=Posts.objects.all()
    liked_post=Like.objects.filter(user=request.user)
    liked_post_list=liked_post.values_list('post',flat=True)
    form=PostForm()
    if request.method == 'POST':
        post_form = PostForm(request.POST,request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post')
    return render(request,'whatsApp/post.html',context={'posts':post,'like_post':liked_post_list,
                                                        'form':form})


def liked(request,pk):
    post= Posts.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post,user=request.user)
    if not already_liked:
        liked_post=Like(post=post,user=request.user)
        liked_post.save()
        return HttpResponseRedirect(reverse('post'))


def Unilked(request,pk):
    post= Posts.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post,user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('post'))

def detail(request,pk):
    post=Posts.objects.filter(pk=pk)
    Postss=Posts.objects.get(pk=pk)
    comments=Comment.objects.filter(post=Postss)
    print(comments)
    form=CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = Postss
            comment.save()
            return HttpResponseRedirect(reverse('detail', kwargs={'pk':pk}))
    return render(request,'whatsApp/details.html',context={'form':form,'comment':comments,'post':post})

def editpost(request,pk):
    current = Posts.objects.get(pk=pk)
    form = PostForm(instance=current)
    if request.method =="POST":
        form=PostForm(request.POST,request.FILES,instance=current)
        if form.is_valid():
            form.save(commit=True)
            form =PostForm(instance=current)
            return redirect('profile')
    return render(request,'whatsApp/editpost.html',context={'form':form})
