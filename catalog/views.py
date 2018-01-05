from django.shortcuts import render , get_object_or_404
from .models import Product , Category


# Create your views here.

def index(request):
    all_category = Category.objects.all()
    context = {'all_category' : all_category}

    return render(request,'catalog/index.html' , context)


def element(request, cat_id, product_id ):
    product = get_object_or_404(Product , id=product_id)
    cat = Category.objects.get(id=cat_id)
    return render(request, 'catalog/element.html',
                  {
                      'product' : product,
                      'cat': cat
                  }
                )


def detail(request, cat_id):
    all_product = Product.objects.filter(category_id=cat_id)
    cat = Category.objects.get(id=cat_id)
    context = {'all_product': all_product, 'cat' : cat}
    return render(request, 'catalog/detail.html', context)