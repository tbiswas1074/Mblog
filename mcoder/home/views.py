from django.shortcuts import render, HttpResponse
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect




def home(request):
    sv = Post.objects.filter(views__gte=Post.objects.order_by('-views')[2].views)
    contex = {'sv':sv}
    return render(request, "home/home.html", contex)

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/login/")
    return render(request, "home/login.html")



def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')
    # return render(request, "home/login.html")


def about(request):
    return render(request, "home/about.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "please fill the form correctely")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been droped")
            return redirect('home')
    return render(request, "home/contact.html")


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count() == 0:
        messages.warning(request, "No search results found. Please refine your query.")
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)

def signup(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            rpassword = request.POST['rpassword']
            # check = request.POST['check']

            if len(username) < 6:
                messages.error(request, "Your user name must be under 6 characters")
                return render(request, "home/signup.html")

            if not username.isalnum():
                messages.error(request, "User name should only contain letters and numbers")
                return render(request, "home/signup.html")

            if (password != rpassword):
                messages.error(request, "Passwords do not match")
                return render(request, "home/signup.html")

            if len(password) < 8 and password != str(password).isalnum():
                messages.error(request, "password must be greater than 8 and contain letters and numeric values")
                return render(request, "home/signup.html")
        
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Your account has been created successfully")
            return redirect('/login')
        return render(request, "home/signup.html")
    except Exception:
        messages.error(request, "No account created")
        return render(request, "home/signup.html")

    

