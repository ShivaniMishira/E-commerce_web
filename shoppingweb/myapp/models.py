from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator


STATE_CHOICES = {
    ('Andhra Pradesh','Andhra Pradesh'),
('Arunachal Pradesh','Arunachal Pradesh'), 
('Assam','Assam'),
('Bihar','Bihar'),
('Chhattisgarh','Chhattisgarh'),
('Goa','Goa'),
('Gujarat','Gujarat'),
('Haryana','Haryana'),
('Himachal Pradesh','Himachal Pradesh'),
('Jammu and Kashmir','Jammu and Kashmir'), 
('Jharkhand','Jharkhand'),
('Karnataka','Karnataka'),
('Kerala','Kerala'),
('Madhya Pradesh','Madhya Pradesh'),
('Maharashtra','Maharashtra'),
('Manipur','Manipur'),
('Meghalaya','Meghalaya'),
('Mizoram','Mizoram'),
('Nagaland','Nagaland'),
('Odisha','Odisha'),
('Punjab','Punjab'),
('Rajasthan','Rajasthan'),
('Sikkim','Sikkim'),
('Tamil Nadu','Tamil Nadu'),
('Telangana','Telangana'),
('Tripura','Tripura'),
('Uttar Pradesh','Uttar Pradesh'),
('Uttarakhand','Uttarakhand'),
('West Bengal','West Bengal'),
('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
('Chandigarh','Chandigarh'),
('Dadra and Nagar Haveli','Dadra and Nagar Haveli'),
('Daman and Diu','Daman and Diu'),
('Lakshadweep','Lakshadweep'),
('Delhi','Delhi'),
('Puducherry','Puducherry')

}
class Customer(models.Model):
 User = models.ForeignKey(User, on_delete=models.CASCADE)
 name = models.CharField(max_length=200)
 locality =models.CharField(max_length=400)
 city = models.CharField(max_length=50)
 zipcode = models.IntegerField()
 state = models.CharField(choices=STATE_CHOICES, max_length=50)
 class Meta:
  db_table = 'costomer'

CATEGORY_CHOISES = {
    ('Shirt','Shirt'),
    ('Jeans','Jeans'),
    ('Ethnic','Ethnic'),
    ('Mobile','Mobile'),
    ('Laptop','Laptop'),
    ('Pant','Pant'),
    ('Jewellery','Jewellery'),
    ('Watch','Watch'),
    ('Books','Books'),
}

class Product(models.Model):
 title = models.CharField(max_length=400)
 selling_price = models.FloatField()
 discount_price = models.FloatField()
 description = models.TextField(max_length=4000)
 brand = models.CharField(max_length=400)
 category = models.CharField(choices=CATEGORY_CHOISES,max_length=50)
 stock = models.PositiveIntegerField()
 product_image = models.ImageField(upload_to='productimg')
 class Meta:
  db_table = 'product'

STATUS_CHOISES = {
    ('pending','pending'),
    ('Accepted','Accepted'),
    ('On Way','On Way'),
    ('Out For Delivery','Out For Delivery'),
    ('Deliverd','Deliverd'),
 }

class Orders(models.Model):
 User = models.ForeignKey(User, on_delete=models.CASCADE)
 customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
 product = models.ForeignKey(Product,on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField(default=0)
 order_date = models.DateTimeField(auto_now_add=True)
 status = models.CharField(choices=STATUS_CHOISES,max_length=50,default='pending')
 class Meta:
  db_table = 'orders'

class Cart(models.Model):
 User = models.ForeignKey(User,on_delete=models.CASCADE)
 product = models.ForeignKey(Product,on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField()
 class Meta:
  db_table = 'cart'

