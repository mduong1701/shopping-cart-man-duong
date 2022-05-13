from django.db import models
from django.urls import reverse

class Category(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
  # https://learndjango.com/tutorials/django-slug-tutorial
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='category', blank=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_url(self):
		return reverse('shop:products_by_category', args=[self.slug])
		# https://www.educba.com/django-reverse/
    # We could instead "return HttpResponseRedirect('/something/')""
		# But what if you want to change the URL in the future? 
  	# You'd have to update your urls.py and all references to it in your code.

	def __str__(self):
		return '{}'.format(self.name)

class Product(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='product', blank=True)
	stock = models.IntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'product'
		verbose_name_plural = 'products'

	def get_url(self):
		return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])
		# https://www.educba.com/django-reverse/
    # We could instead "return HttpResponseRedirect('/something/')""
		# But what if you want to change the URL in the future? 
  	# You'd have to update your urls.py and all references to it in your code.

	def __str__(self):
		return '{}'.format(self.name)