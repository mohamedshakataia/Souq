from django.shortcuts import render
from .models import jumia, Category
from django.core.paginator import Paginator



# Create your views here.sss

def is_valid_queryparam(param):
    return param != '' and param is not None



def Product(request):
    qs = jumia.objects.all()
    Categories =Category.objects.all()
    manufacture = request.GET.get('manufacture')
    category = request.GET.get('category')


    # pagination
    paginator = Paginator(qs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    

    if manufacture != '' and manufacture is not None :
        qs = qs.filter(manufacture__icontains=manufacture)



    if is_valid_queryparam (category) and category != 'Choose...':
        qs = qs.filter(category__sweetName=category)


  
    return render(request,'product/jumia_list.html',{
        'queryset' : qs ,
        'Categories' : Categories,
        'movies':page_obj
    })










