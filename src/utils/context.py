from product.models import Category



def get_nav(request):
    pro = Category.objects.all()
    return {'pro':pro}