from django.shortcuts import render
from .models import jumia, Category
from django.core.paginator import Paginator
from django.http import JsonResponse




# Create your views here.sss

def is_valid_queryparam(param):
    return param != '' and param is not None

def range_num():
    return range(1,6)

def Product(request):
    qs = jumia.objects.all()
    count = jumia.objects.all().count()
    Categories =Category.objects.all().order_by('sweetName')
    Recently_Viewed =jumia.objects.filter()[:100]
    manufacture = request.GET.get('manufacture')
    category = request.GET.get('category')
    paginator = Paginator(qs, 50) # Show 50 contacts per page.
    brands= jumia.objects.values('manufacture').distinct().order_by('manufacture')
    obj = jumia.objects.values('rate')



    



    if is_valid_queryparam (manufacture) and manufacture != 'Choose...':
        qs = qs.filter(manufacture__icontains=manufacture)
        count = qs.filter(manufacture__icontains=manufacture).count()
        paginator = Paginator(qs, 50) # Show 50 contacts per page.


    if is_valid_queryparam (category) and category != 'Choose...':
        qs = qs.filter(category__sweetName=category)
        count = qs.filter(category__sweetName=category).count()
        paginator = Paginator(qs, 50) # Show 50 contacts per page.


    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request,'product/jumia_list.html',{
        'page_obj' : page_obj ,
        'Categories' : Categories,
        'brands':brands,
        'count':count,
        'Recently_Viewed':Recently_Viewed,
        'object': obj,
        'range_num':range_num

       
        })



# def rate_image(request):
#     if request.method == 'POST':
#         el_id = request.POST.get('el_id')
#         val = request.POST.get('val')
#         print(val)
#         obj = jumia.objects.get(id=el_id)
#         obj.score = val
#         obj.save()
#         return JsonResponse({'success':'true', 'score': val}, safe=False)
#     return JsonResponse({'success':'false'})




