from django.core.files.base import endswith_cr
from django.db.models.query import prefetch_related_objects
from django.shortcuts import render, redirect
from .models import Crypto, Store ,Transaction_history
from .forms import CryptoForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decimal import Decimal

crypto_info = ['bitcoin']

def home(request):



	return render(request, 'app/home.html', {'ticker': "Enter a Ticker Symbol Above..."})



@login_required
def transition(request):
  ticker = Crypto.objects.filter(owner=request.user)
  return render(request, 'app/transition.html', {'crypto_info': crypto_info})	

@login_required
def buy_sell(request):
   if request.method=='POST':
	   crypto_info[0] = request.POST['name']
	   return redirect('transition')
   else:
	   return render(request,'app/buy_sell.html',{})

@login_required
def add_get_credit(request):
  credit = Store.objects.filter(moneyowner=request.user)
  return render(request, 'app/add_get_credit.html', {'credit':credit})


	

def about(request):
	return render(request, 'app/about.html', {})

def chart(request):
	return render(request,'app/chart.html',{})
	
@login_required
def add_stock(request):
	if request.method == 'POST':
		if get_user_crypto(request):
			temp = Crypto.objects.get(owner = request.user ,ticker = request.POST['ticker'] )
			temp.quantity = temp.quantity + Decimal(request.POST['quantity'])
			temp.save()
			messages.success(request, ("crypto Has Been Added!"))
			return redirect('portfolio')
		else:
			temp = Crypto.objects.create(ticker = request.POST['ticker'],quantity = request.POST['quantity'],owner = request.user)
			temp.save()
			messages.success(request, ("crypto Has Been Added!"))
			return redirect('portfolio')
	else:
		return redirect('transition')			 
		


	
@login_required
def delete(request, stock_id):
	item = Crypto.objects.filter(owner=request.user).get(pk=stock_id)
	item.delete()
	messages.success(request, ("Crypto Has Been Deleted!"))
	return redirect(delete_stock)


""" @login_required
def delete_stock(request):
	ticker = Stock.objects.filter(owner=request.user)
	return render(request, 'app/delete_stock.html', {'ticker': ticker}) """

@login_required
def delete_stock(request):
	if request.method == 'POST':
		if get_user_crypto(request):
			temp = Crypto.objects.get(owner = request.user,ticker = request.POST['ticker'])
			temp.quantity = temp.quantity - Decimal(request.POST['quantity'])
			if temp.quantity > 0:
			   temp.save()
			   messages.success(request, ("crypto sold seccessfuly!"))
			   return redirect('portfolio')
			else:
				messages.warning(request, ("crypto quantity is more than your owns"))
				return redirect('transition')
		else:
			messages.warning(request, ("you do not have this crypto!"))
			return redirect('transition')
	else:
		return redirect('transition')		


@login_required
def add_credit(request):
	if request.method == 'POST':
		if get_user_store(request) :
			temp = Store.objects.get(moneyowner = request.user)
			temp.credit = temp.credit + Decimal(request.POST['credit'])
			temp.save()
			messages.success(request, ("credit added seccessfuly!"))
			return redirect('credit')
		else:
			temp = Store.objects.create(credit = request.POST['credit'],moneyowner = request.user)
			temp.save()
			return redirect('credit')
	else:
		return redirect('credit')

def get_user_store (request):
    try:
       return Store .objects.get(moneyowner = request.user)
    except Store.DoesNotExist:
        return False

def get_user_crypto(request):
    try:
       return Crypto.objects.get(owner = request.user ,ticker = request.POST['ticker'] )
    except Crypto.DoesNotExist:
        return False

@login_required
def get_credit(request)	:
	if request.method == 'POST':
		if get_user_store(request) :
			temp = Store.objects.get(moneyowner = request.user)
			temp.credit = temp.credit - Decimal(request.POST['credit'])
			if temp.credit > 0:
			   temp.save()
			   messages.success(request, ("credit token seccessfuly!"))
			   return redirect('credit')
			else:
				messages.warning(request, ("token money is more than your credit!"))
				return redirect('credit')
		else:
			messages.warning(request, ("you do not have any credit"))
			return redirect('credit')
	else:
		return redirect('credit')	

@login_required
def show_portfolio(request):
		ticker = Crypto.objects.filter(owner=request.user)
		return render(request, 'app/show_portfolio.html', {'ticker': ticker})


