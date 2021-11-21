from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('about.html', views.about, name="about"),
	path('chart.html', views.chart, name="chart"),
	path('add_stock.html', views.add_stock, name="add_stock"),
	path('delete/<stock_id>', views.delete, name="delete"),
	path('delete_stock.html', views.delete_stock, name="delete_stock"),
	path('add_credit.html', views.add_credit, name="add_credit"),
	path('get_credit.html', views.get_credit, name="get_credit"),
	path('show_portfolio.html', views.show_portfolio, name="portfolio"),
    path('transition.html', views.transition, name="transition"),
	path('buy_sell.html', views.buy_sell, name="buy_sell"),
	path('add_get_credit.html', views.add_get_credit, name="credit"), 
]