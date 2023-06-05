from django.shortcuts import HttpResponse, render, redirect
from datetime import datetime
from products.models import Product, Review
from products.forms import ProductCreateForm, ReviewCreateForm
from products.constants import PAGINATION_LIMIT


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date_view(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now())


def goodby_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')


def main_page(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == "GET":
        products = Product.objects.all()
        page = int(request.GET.get('page', 1))

        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        search_title = request.GET.get('search_title')
        search_description = request.GET.get('search_description')
        if search_title:
            products = products.filter(title__contains=search_title)
        if search_description:
            products = products.filter(title__contains=search_description)

        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context = {
            'products': products,
            'pages': range(1, max_page+1)
        }
        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'reviews': product.review_set.all(),
            'form': ReviewCreateForm,
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        data = request.POST
        form = ReviewCreateForm(data)
        product = Product.objects.get(id=id)

        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('review'),
                product=product
            )
            return redirect(f'/products/{product.id}')

        return render(request, 'products/detail.html', context={
            'form': form
        })


def create_product_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }

        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ProductCreateForm(data, files)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price')
            )
            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })
