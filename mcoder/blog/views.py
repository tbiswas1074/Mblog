from django.shortcuts import render, HttpResponse,redirect
from blog.models import Post, BlogComment, Like, View
from django.contrib import messages
from blog.templatetags import extras
from django.db.models import Max
from django.contrib.auth.models import User 


# Create your views here.
def blogHome(request): 
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "blog/bloghome.html", context)

def blogcreate(request): 
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        slug = request.POST['title']
        post = Post(title=title, content=content, author=author, slug=slug)
        post.save()
        messages.success(request, "Your article has been posted successfully")
        return redirect('/blog/blogcreate/')
    return render(request, "blog/blogcreate.html")

def blogPost(request, slug): 
    a, b = [], []
    c, d = 0, 0
    post = Post.objects.filter(slug=slug).first()
    post.totalviews = post.totalviews + 1
    post.save()

    user = request.user
    for ite in Like.objects.filter(post=post):
        if ite.user not in a:
            a.append(ite.user)
            c += 1
    post.likes = c
    post.save()

    for item in View.objects.filter(post=post):
        if item.user not in b:
            b.append(item.user)
            d += 1
    post.views = d
    post.save()

    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict, }
    return render(request, "blog/blogpost.html", context)

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno== None:
            comment=BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")
    
def postLike(request):
    if request.method == "POST":
        user = request.user
        lSno = request.POST.get('lSno')
        post = Post.objects.get(sno=lSno)
        like = Like(user=user, post=post)
        like.save()

        
    return redirect(f"/blog/{post.slug}")

def postView(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            user = request.user
            pSno = request.POST.get('pSno')
            post = Post.objects.get(sno=pSno)
            view = View(user=user, post=post)
            view.save()

        
    return redirect(f"/blog/{post.slug}")

