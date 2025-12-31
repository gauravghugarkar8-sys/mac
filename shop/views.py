from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse
from . models import courses,signup_v,mycours
from math import ceil



# def index(request):
#         products = Product.objects.all()     #add all products
#         n = len(products)
#         nSlides = n // 4 + ceil( (n / 4) + (n // 4))
#         params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
#
#         return render(request, "shop/index.html", params)
def index(request):
    allcours = []
    catprods = courses.objects.values('category', 'id')
    cats = {item["category"] for item in catprods}

    for cat in cats:
        prod = courses.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allcours.append([prod, range(1, nSlides), nSlides])


    params = {'allProds': allcours}
    return render(request, "shop/index.html", params)


def login_p(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = signup_v.objects.filter(name=username, password=password).first()
        if user:
            # print(request.user.username)  he takla tar direct main user disel
            request.session['user_id'] = user.id

            return redirect('/')  # login successful

        else:
            return render(request, 'shop/login_p.html', {'error': 'Invalid Credentials'})

    return render(request, 'shop/login_p.html')



    return render(request,'shop/ak.html')

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        signup_v.objects.create(
            name=name,
            email=email,
            password=password
        )

        return redirect( '/')

    return render(request, 'shop/signup.html')

def about(request):
    catprods = courses.objects.all()
    list={'catprods': catprods}
    return render(request,'shop/about.html',list)

# def mycourse(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         email = request.POST['email']
#         user = mycours.objects.filter(id=id).first()
#         mycours.objects.create(
#
#     )
#
#
#     return render(request,'shop/mycourse.html')


def addcourse(request):
    if request.method == "POST":
        course_id = request.POST.get('id')  # course id POST मधून मिळेल
        user_id = request.session.get('user_id')  # login केलेला user

        if not user_id:
            return redirect('login_p')

        user = signup_v.objects.get(id=user_id)
        course = courses.objects.get(id=course_id)

        # duplicate टाळण्यासाठी
        mycours.objects.get_or_create(user=user, course=course)

        return redirect('about')  # किंवा हवे तिथे
    else:
        return redirect('about')


def mycoursess(request):

    catprods = mycours.objects.filter(user=request.session.get('user_id'))
    list={'catprods': catprods}
    print(list)
    return render(request,'shop/mycours.html',list)

def logout_p(request):
    logout(request)          # Django logout
    return redirect('login_p')

def profile_p(request):
    catprods =signup_v.objects.filter(id=request.session.get('user_id'))
    list = {'catprods': catprods}
    print(list)
    return  render(request,'shop/profil.html',list)
