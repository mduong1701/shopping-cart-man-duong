from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def searchResult(request):
	products = None
	query = None
	if 'q' in request.GET:
		query = request.GET.get('q')
    # https://riptutorial.com/django/example/4565/advanced-queries-with-q-objects
    # We can use Q objects to create AND, OR conditions in the lookup query.
		products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    # If the description contains the string, return the result
	return render(request, 'search.html', {'query':query, 'products':products})