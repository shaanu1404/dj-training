from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Product, Category
from .forms import ProductForm, ContactForm


def all_products_view(request):
    """Get all products"""

    all_products = Product.objects.order_by('-id')

    q = request.GET.get('q', None)
    if q:
        all_products = all_products.filter(title__icontains=q)

    context = {"all_products": all_products}
    return render(request, 'products/list.html', context)


def single_product_view(request, id):
    """Get single product using id"""

    # product = None
    # try:
    #     product = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     print("Product does not exist")

    product = get_object_or_404(Product, id=id)

    context = {
        "product": product
    }
    return render(request, 'products/detail.html', context)


def create_new_product(request):
    """Create new product"""

    form = ProductForm(request.POST or None)

    if request.method == "POST":
        # title = request.POST['title']
        # description = request.POST['description']
        # price = request.POST['price']
        # category_id = request.POST['category']

        # if title and description and price and category_id:
        #     category = Category.objects.get(id=category_id)

        #     new_product = Product(
        #         title=title, description=description, price=price, category=category)
        #     new_product.save()
        #     return redirect(reverse('all_products'))

        if form.is_valid():
            form.save()

    context = {
        "categories": Category.objects.all(),
        "form": form
    }
    return render(request, 'products/create.html', context)


def edit_product(request, id):
    """Edit product using id"""

    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        category_id = request.POST['category']

        if title and description and price and category_id:
            category = Category.objects.get(id=category_id)

            product.title = title
            product.description = description
            product.price = price
            product.category = category
            product.save()
            return redirect(reverse('all_products'))

    context = {
        "product": product,
        "categories": Category.objects.all()
    }
    return render(request, 'products/edit.html', context)


def delete_product(request, id):
    """Delete product using id"""

    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.delete()
        return redirect(reverse('all_products'))

    context = {
        "product": product
    }
    return render(request, 'products/delete.html', context)


def contact_form_view(request):
    form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['message'])

    context = {
        "form" : form
    }
    return render(request, 'contact.html', context)