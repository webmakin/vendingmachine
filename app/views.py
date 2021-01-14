from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ProductForm, AttemptForm
from .models import *
from django.urls import reverse

coins = [1, 5, 10, 25]

def index(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            #product = form.save()
            p = Product(name = form.cleaned_data['name'], price=form.cleaned_data['price'], quantity=form.cleaned_data['quantity'])
            p.save()
    else:        
        form = ProductForm()
    products = Product.objects.all()
    attempts = Attempt.objects.all()
    purchases = Purchase.objects.all()
    attempt_form = AttemptForm()

    return render(request, 'index.html', {'form': form,'title': "vendingmachine", 'products': products, 'coins': coins, 'attempt_form': attempt_form, 'attempts': attempts, 'purchases': purchases})

def purchase(request):
    if request.method == 'POST':
        form = AttemptForm(request.POST)
        if form.is_valid():

            #register attempt
            a = Attempt(coins_inserted = form.cleaned_data['coins_inserted'], product_selected = form.cleaned_data['product_selected'])
            a.save()
            
            coins_inserted = form.cleaned_data['coins_inserted'].split(',')
            coins_inserted_value = 0
            for coin in coins_inserted:
                coins_inserted_value = coins_inserted_value + int(coin) 

            if coins_inserted_value >= form.cleaned_data['product_selected'].price and form.cleaned_data['product_selected'].quantity >= 1:
                #make purchase
                print("make purchase")
                prod = Product.objects.get(id=form.cleaned_data['product_selected'].id)
                prod.quantity = form.cleaned_data['product_selected'].quantity-1
                prod.save()

                p = Purchase(change_returned = str(coins_inserted_value-prod.price))
                p.product_purchased = prod
                p.save()
                

        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponse("not allowed")        
