from django.shortcuts import render

from store.models import Product


# Create your views here.
def index(request):
    """View function for home page of site."""

    num_products = Product.objects.all().count()

    num_instances_available = Product.objects.filter(stock__gt=0).count()

    context = {
        "num_products": num_products,
        "num_instances_available": num_instances_available,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)
