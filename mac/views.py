



from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from math import ceil

# def index(request):
#         products = Product.objects.all()     #add all products
#         n = len(products)
#         nSlides = n // 4 + ceil( (n / 4) + (n // 4))
#         params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
#
#         return render(request, "shop/index.html", params)
def index(request):

    return render(request, "index.html")

