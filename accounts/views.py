from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils.http import is_safe_url
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method == 'POST':
        #user has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']: #  در صورتی که دوتا پسورد باهم همخوانی داشته باشه
            try: # سعی میکنه نام کاربری رو از بین کاربران موجود پیدا کنه
 
                # در خط زیر سعی میکنه کاربر با نام کاربری ورودی رو از دیتابیس پیدا کنه
                # اگر همچین کاربری پیدا نشه، ارور زیر پرت میشه
                # User.DoesNotExist
                # که این ارور رو چند خط پایین تر در اکسپت گرفتیم
                # و این ارور به معنی اینه که کاربر جدیده و باید ساخته بشه
                user = User.objects.get(username=request.POST['username']) # means this username already Exist!
 
                # در صورتی که در خط قبل کاربر موجود بود، کد به این خط میرسه و این یک پیام رو به صفحه مبدا بر می گردونه
                #  و میگه که نام کاربری قبلا انتخاب شده
                messages.success(request, ("user name has already exist!"))
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken!'})
            except User.DoesNotExist: # اگر نام کاربری از قبل موجود نبود، کاربر جدید رو میسازه
                # ترتیب یوزرنیم و ایمیل و پسورد در متدزیر مهمه. مثلا اگر کلا ایمیل رو ننویسیم، و پسورد رو بعنوان دومی بنویسیم، پسورد میره بعنوان آدرس ایمیل کاربر ذخیره میشه
                user = User.objects.create_user(request.POST['username'], request.POST['email'] , request.POST['password1'])
                # در خط زیر با کاربری که در خط بالا ایجاد کرده در سایت لاگین می کنه
                auth.login(request,user)
                # و کاربر لاگین کرده رو زارت میفرسته به صفحه اصلی. البته میشد اینجا با یک پیام به کاربر اعلام کنیم که ثبت نام با موفقیت انجام شد.
                return redirect('home')
 
        else: # در صورتی که دوتا پسورد باهم همخوانی نداشته باشه
            messages.success(request, ("paswords did not match!"))
            return render(request,'accounts/signup.html', {'error':'paswords did not match!'})
    else:
        # در این حالت متد پست فراخوانی نشده. یعنی کاربر فرم را سابمیت نکرده. بلکه فقط آدرس صفحه را زده که صفحه را ببیند.
        # بنابراین صفحه حاوی فرم به کاربر نمایش داده میشود و پردازشی انجام نمی شود.
        return render(request, 'accounts/signup.html')

def login(request):
    # اگر رکوئست با متد POST ارسال شده بود یعنی کاربر فرم لاگین را سابمیت کرده است
    if request.method == 'POST':
        # از متد user.authemticate برای یافتن کاربر استفاده میشود. این متد یه متغیر از نوع آبجکت user بر می گرداند
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        # چک می کند که اگر متغیر یوزر خالی نبود، لاگین را با اطلاعات یوزر انجام دهد
        if user is not None:
            auth.login(request, user)
            # در اینجا کاربر را به صفحه ای که میخواهیم پس از لاگین به وی نمایش دهیم ریدایرکت می کنیم
            return redirect(request.POST['next'])

        # در صورتی که متغیر یوزر خالی بود
        # یعنی کاربر با مشخصاتی که در فرم وارد شده است وجود ندارد
        else:
            # کاربر را به همراه یک پیام خطا به صفحه لاگین باز می گرداند
            # این پیغام خطا در قسمت تعبیه شده در بالای صفحه لاگین به نمایش در می آید
            messages.success(request, ("Invalid Username Or Password"))
            return render(request, 'app/home.html', {'error':'Invalid Username Or Password'})
    # اگر رکوئست با متد GET ارسال شده بود یعنی کاربر لینک صفحه لاگین را زده و میخواهد صفحه لاگین را ببیند
    else:
        return render(request, 'accounts/login.html')        

def logout(request):
    auth.logout(request)
    return redirect('home')        