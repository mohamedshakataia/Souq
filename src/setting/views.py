from django.shortcuts import render
from product.models import jumia , Category
from django.views.generic import ListView 

# Create your views here.
def Home(request):
    var=Category.objects.all()
    return render(request,'setting/home.html',{'pro':var})

def filter_by_category(request,name_category):
    pro = jumia.objects.filter(category__sweetName=name_category)
    return render(request,'setting/home.html',{'pro':pro})
