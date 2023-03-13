from django.shortcuts import render,redirect
from .models import User,Product,Wishlist,Cart,Transaction,Contact
from django.conf import settings
from .paytm import generate_checksum, verify_checksum
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def initiate_payment(request):
        user=User.objects.get(email=request.session['email'])
        amount = int(request.POST['amount'])
        transaction = Transaction.objects.create(made_by=user, amount=amount)
        transaction.save()
        merchant_key = settings.PAYTM_SECRET_KEY
        params = (
        	('MID', settings.PAYTM_MERCHANT_ID),
        	('ORDER_ID', str(transaction.order_id)),
        	('CUST_ID', str(transaction.made_by.email)),
        	('TXN_AMOUNT', str(transaction.amount)),
	        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
	        ('WEBSITE', settings.PAYTM_WEBSITE),
	        # ('EMAIL', request.user.email),
	        # ('MOBILE_N0', '9911223388'),
	        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
	        ('CALLBACK_URL', 'http://localhost:8000/callback/'),
	        # ('PAYMENT_MODE_ONLY', 'NO'),
    )
        paytm_params = dict(params)
        checksum = generate_checksum(paytm_params, merchant_key)
        transaction.checksum = checksum
        transaction.save()
        carts=Cart.objects.filter(user=user,payment_status=False)
        for i in carts:
        	i.payment_status=True
        	i.save()
        carts=Cart.objects.filter(user=user,payment_status=False)
        paytm_params['CHECKSUMHASH'] = checksum
        print('SENT: ', checksum)
        return render(request, 'redirect.html', context=paytm_params)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
        else:
            received_data['message'] = "Checksum Mismatched"
        return render(request, 'callback.html', context=received_data)
       
def index(request):
	try:
		user=User.objects.get(email=request.session['email'])
		if user.usertype=="buyer":
			return render(request,'index.html')
		else:
			return render(request,'seller_index.html')
	except:
		return render(request,'index.html')
def about(request):
	return render(request,'about.html')
def shop_details(request):
	return render(request,'shop-details.html')
def shopping_cart(request):
	return render(request,'shoppi.ng-cart.html')
def checkout(request):
	return render(request,'checkout.html')
def blog_details(request):
	return render(request,'blog-details.html')
def blog (request):
	return render(request,'blog.html')
def contact(request):
	return render(request,'contact.html')
def shop(request):
	product=Product.objects.all()
	return render(request,'shop.html',{'product':product})
def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="Email AlReady Registered "
			return render(request,'signup.html',{'msg' : msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					    email=request.POST['email'],
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						password=request.POST['password'],
						profile_pic=request.FILES['profile_pic'],
						usertype=request.POST['usertype']						
					)
				msg="User Sign Up Succefully"
				return render(request,'signup.html',{'msg' : msg})
			else:
				msg="Password And Confirm password Does Not Match"	
	else:
		return render(request,'signup.html')
									
def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				if user.usertype=="buyer":
					request.session['email']=user.email
					msg="Logiing Succefully"
					return render(request,'index.html',{'msg':msg})
				else:
					request.session['email']=user.email
					msg="Logiing Succefully"
					return render(request,'seller_index.html',{'msg':msg})
			else:
				msg="Your password Is Invalid"
				return render(request,'login.html',{'msg':msg})
		except Exception as e:
			print(e)
			msg="Your Email Is Not Register"
			return render(request,'login.html',{'msg':msg})		
	else:
		return render(request,'login.html')		

def logout(request):
	del request.session['email'] 
	return render(request,'login.html')
def change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		if user.password==request.POST['oldpassword']:
			if request.POST['newpassword']==request.POST['cnewpassword']:
				user.password=request.POST['newpassword']
				user.save()
				return redirect('logout')
			else:
				msg='new password & confirm password Does not match..'
				return render (request,'change-password.html',{'msg':msg})	
		else:
			msg='old password Does Not Match..'
			return render (request,'change-password.html',{'msg':msg})
	else:
		return render(request,'change-password.html')

def edit_profile(request):
	user=User.objects.get(email=request.session['email'])
	if user.usertype=="buyer":
		if request.method=="POST":
			user.fname=request.POST['fname']
			user.lname=request.POST['lname']
			user.mobile=request.POST['mobile']
			user.address=request.POST['address']
			user.email=request.POST['email']
			try:
				user.profile_pic=request.FILES['profile_pic']
			except:
				pass
			user.save()
			msg="Profile Updated Succefully"
			request.session['profile_pic']=user.profile_pic.url
			request.session['fname']=user.fname
			return render(request,'edit-profile.html',{'user':user,'msg':msg})
		else:
			return render(request,'edit-profile.html',{'user':user})
	else:
		if request.method=="POST":
			user.fname=request.POST['fname']
			user.lname=request.POST['lname']
			user.mobile=request.POST['mobile']
			user.address=request.POST['address']
			user.email=request.POST['email']
			try:
				user.profile_pic=request.FILES['profile_pic']
			except:
				pass
			user.save()
			msg="Profile Updated Succefully"
			request.session['profile_pic']=user.profile_pic.url
			request.session['fname']=user.fname
			return render(request,'seller-edit-profile.html',{'user':user,'msg':msg})
		else:
			return render(request,'seller-edit-profile.html',{'user':user})
				
def seller_index(request):
	return render(request,'seller_index.html')

def add_product(request):
	if request.method=="POST":
		product_seller=User.objects.get(email=request.session['email'])
		Product.objects.create(
			
			product_seller=product_seller,
			product_category=request.POST['product_category'],
			product_price=request.POST['product_price'],
			product_name=request.POST['product_name'],
			product_size=request.POST['product_size'],
			product_dese=request.POST['product_desc'],
			product_pic=request.FILES['product_pic'],
            )
		msg="product Added Succefully"
		return render(request,'seller_add_product.html',{'msg':msg})

	else:
		return render(request,'seller_add_product.html')
def my_product(request):
	product_seller=User.objects.get(email=request.session['email'])
	product=Product.objects.filter(product_seller=product_seller)
	return render(request,'seller_my_product.html',{'product':product})	

def seller_product_details(request,pk):
	product=Product.objects.get(pk=pk)
	return render (request,'seller-product-details.html',{'product':product})

def edit_product(request,pk):
	product=Product.objects.get(pk=pk)
	if request.method=="POST":
		product.product_name=request.POST['product_name']
		product.product_price=request.POST['product_price']
		product.product_category=request.POST['product_category']
		product.product_size=request.POST['product_size']
		product.product_dese=request.POST['product_dese']
		try:
			product.product_pic=request.FILES['product_pic']
		except:
			pass
		product.save()
		msg='Edit Product Succefully'
		return render (request,'seller_edit_product.html',{'msg':msg,'product':product})	
	else:
		return render(request,'seller_edit_product.html',{'product':product})
				
def delete_product(request,pk):
	product=Product.objects.get(pk=pk)
	product.delete()
	return redirect('my-product')

def add_to_wishlist (request,pk):
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	Wishlist.objects.create(user=user,product=product)
	msg="Add To Wishlist Succefully."
	wishlist=Wishlist.objects.filter(user=user)	
	return redirect('wishlist')

def remove_to_wishlist(request,pk):
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	wishlist=Wishlist.objects.get(user=user,product=product)
	wishlist.delete()
	return redirect('wishlist')
 
def wishlist(request):
 	user=User.objects.get(email=request.session['email'])
 	wishlist=Wishlist.objects.filter(user=user)
 	return render (request,'add-to-wishlist.html',{'wishlist':wishlist})   

def details(request,pk):
	wishlist_flag=False
	product=Product.objects.get(pk=pk)
	try:	
		user=User.objects.get(email=request.session['email'])
	except:
		pass
	try:
		wishlist=Wishlist.objects.get(user=user,product=product)
		wishlist_flag=True
	except:
		pass
	return render(request,'details.html',{'product':product,'wishlist_flag':wishlist_flag})

def add_to_cart(request,pk):
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	Cart.objects.create(
		              user=user,
		              product=product,
		              product_price=product.product_price,
		              product_qty=1,
		              total_price=product.product_price,
		)
	return redirect('cart')

def remove_to_cart(request,pk):
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.get(user=user,product=product,payment_status=False)
	carts.delete()
	return redirect('cart')
			
def cart(request):
	net_price=0
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user,payment_status=False)
	for i in carts :
 		net_price=net_price + i.total_price + i.delivery_charge
	return render (request,'add-to-cart.html',{'carts':carts,'net_price':net_price})   

def contact(request):
	if request.method =='POST':
		Contact.objects.create(
			contact_name=request.POST['name'],
			contact_email=request.POST['email'],
			contact_message=request.POST['message']
			)
		msg='Send Message Succefully..'
		return render(request,'contact.html',{'msg':msg})
	else:
		return render (request,'contact.html')

def contact_me(request):
	contact=Contact.objects.all().order_by("-id")[:3]
	return render(request,'seller_contact_me.html',{'contact':contact})

def confirm_oder(request):
	product=Product.objects.all()
	user=User.objects.all()
	cart=Cart.objects.filter()
	return render(request,'confirm_oder.html',{'cart':cart,'user':user,'product':product})				
