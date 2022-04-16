
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from.forms import VideoForm,CommentForm
from .models import Uploads,Category,Like,Comment

def Uploader(request):
    form=VideoForm()
    if request.method=="POST":
        form= VideoForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.creator=request.user
            post.save()
            return redirect('show_video')

    return render(request,'video/uploads.html',context={'form':form})
def show_video(request):
    videos=Uploads.objects.all()
    category=Category.objects.all()
    categoryID= request.GET.get('category')
    if categoryID:
        videos = Uploads.get_all_products_by_id(categoryID)
    else:
        videos=Uploads.objects.all()
    prddata={
        'video':videos,
        'category':category,
    }
    return render(request,'video/video_home.html',prddata)

def single_video(request,pk,cpk):
    video=Uploads.objects.filter(pk=pk)
    #like and unlike
    liked_post=Like.objects.filter(user=request.user)
    liked_post_list=liked_post.values_list('post',flat=True)
    category_video=Uploads.get_all_products_by_id(cpk)
    #like and unlike
    video_up = Uploads.objects.get(pk=pk)
    #comment
    comments=Comment.objects.filter(upload=video_up)
    print(comments)
    form=CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.upload = video_up
            comment.save()
            return HttpResponseRedirect(reverse('singlevideo', kwargs={'pk':pk,'cpk':cpk}))
    return render(request,'video/justonevideo.html',context={'form':form,'video':video,
                                                             'category_video':category_video,
                                                             'like_post':liked_post_list,
                                                             'comment':comments})

 
def liked(request,pk,cpk):
    post= Uploads.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post,user=request.user)
    if not already_liked:
        liked_post=Like(post=post,user=request.user)
        liked_post.save()
        return HttpResponseRedirect(reverse('singlevideo', kwargs={'pk':pk,'cpk':cpk}))
        # return HttpResponseRedirect(reverse('show_video'))

def Unilked(request,pk,cpk):
    post= Uploads.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post,user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('singlevideo', kwargs={'pk':pk,'cpk':cpk}))
    # return HttpResponseRedirect(reverse('show_video'))
def Editpost(request,pk):
    current = Uploads.objects.get(pk=pk)
    form = VideoForm(instance=current)
    if request.method =="POST":
        form=VideoForm(request.POST,request.FILES,instance=current)
        if form.is_valid():
            form.save(commit=True)
            form =VideoForm(instance=current)
            return redirect('profile')
    return render(request,'whatsApp/editpost.html',context={'form':form})

    