from django.contrib import admin
from .models import User,Product,Wishlist,Cart,Transaction,Contact

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Transaction)
admin.site.register(Contact)
