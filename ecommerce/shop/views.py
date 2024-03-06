from django.shortcuts import render
from .models import Product,Order
from django.core.paginator import Paginator

# Create your views here.

# Index View
def index(request):
    # QuerySet
    items = Product.objects.all()    
    
    # Product Search Logic
    item_search = request.GET.get('item_search')
    if item_search != '' and item_search is not None:
        items = items.filter(item_name__icontains=item_search)
    
    # Paginator Logic
    paginator = Paginator(items,3)
    cur_page = request.GET.get('page')
    items = paginator.get_page(cur_page)
    
    return render(request, 'shop/index.html', context={'items':items})

# Detail View
def detail(request, id):
    items = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', context={'items':items})

def checkout(request):
    
    if request.method == 'POST':
        items = request.POST.get('items','')
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone_number = request.POST.get('phonenumber',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        zip = request.POST.get('zip',"")
        total = request.POST.get('total-amount','')
        
        order = Order.objects.create(items=items,name=name,email=email,phone_number=phone_number,address=address,city=city,zip=zip,total=total)
    return render(request, 'shop/checkout.html')