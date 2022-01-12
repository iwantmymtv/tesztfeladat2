from .models import Category

def category_list(request):
    ctx= {
        'category_list':Category.objects.all().only("name"),
    }
    return ctx