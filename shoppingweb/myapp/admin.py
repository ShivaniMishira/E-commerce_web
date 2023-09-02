from django.contrib import admin
from .models import Customer, Product, Cart, Orders

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','User','name','locality','city','zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title','selling_price','discount_price','description','brand','category','stock','product_image']

@admin.register(Orders)
class OrdersModelAdmin(admin.ModelAdmin):
    list_display = ['User','product','order_date','quantity','customer','status']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['User','product','quantity']