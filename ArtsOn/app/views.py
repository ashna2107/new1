from django.shortcuts import render,redirect,HttpResponse
from.models import *
from django.contrib import messages
import razorpay
import datetime

# Create your views here.
def index(re):
    return render(re,'index.html')

def contact(re):
    if re.method=='POST':
        name=re.POST['name']
        email=re.POST['email']
        phone=re.POST['phone']
        message=re.POST['message']
        data = contactus.objects.create(name=name, email=email, phone=phone, message=message)
        data.save()
        messages.success(re, 'successfully added')
        return redirect(contact)
    else:
        return render(re,'contact.html')

def conhome(re):
    data =contactus.objects.all()
    return render(re, 'conhome.html',{'data':data})

def about1(re):
    return render(re,'about.html')

def gallery(re):
    return render(re,'gallery.html')

def admindance(re):
    data = compdance.objects.all()
    return render(re,'adminpage/admindance.html',{'data': data})

def adminuser(re):
        data = reguser.objects.all()
        return render(re,'adminpage/adminuser.html',{'data': data})


def adminmusic(re):
    data = compmusic.objects.all()
    return render(re, 'adminpage/adminmusic.html', {'data': data})

def ser(re):
    if 'user' in re.session:
        u=reguser.objects.get(username=re.session['user'])
        m=compmusic.objects.filter(status="active")
        d=compdance.objects.filter(status="active")
        data = Reviews.objects.all()
        return render(re,'ser.html',{'user':u,'music':m,'dance':d,'data':data})
    return HttpResponse("not have vale")



def pending(re):
    data=compmusic.objects.filter(status="pending")
    return render(re, "pending.html",{'data':data})

def pending1(re,id1):
    compmusic.objects.filter(pk=id1).update(status='active')
    return redirect(pending)

def pending01(re):
    data=compdance.objects.filter(status="pending")
    return render(re, "pending01.html",{'data':data})

def pending02(re,id2):
    compdance.objects.filter(pk=id2).update(status='active')
    return redirect(pending01)
def profile1(request):
    if 'music' in request.session:
        user=compmusic.objects.get(username=request.session['music'])
        data = about.objects.filter(mname=user)
        data1=project.objects.filter(mname=user)
        return render(request, "profile.html",{'user':user,'data':data,'data1':data1})
    else:
        return HttpResponse("not have vale")

def delete(re,id1):
    data=project.objects.get(pk=id1)
    data.delete()
    messages.success(re,"successfully deleted")
    return redirect(profile1)

def delete1(re,id1):
   data=project.objects.get(pk=id1)
   data.delete()
   messages.success(re,"successfully deleted")
   return redirect(profile1)

def profile2(request):
    if 'dance' in request.session:
        user=compdance.objects.get(username=request.session['dance'])
        data7=about.objects.filter(dname=user)
        data2=project.objects.filter(dname=user)
        return render(request, "pro.html",{'user':user,'data7':data7,'data2':data2})

def viewdetails(re,dp):
    user=compmusic.objects.get(pk=dp)
    data3 = about.objects.filter(mname=user)
    data4 = project.objects.filter(mname=user)
    return render(re,"viewdetails.html",{'user':user,'data3':data3,'data4':data4})

def cprofile(re,dp):
    user=compdance.objects.get(pk=dp)
    data8= about.objects.filter(dname=user)
    data9 = project.objects.filter(dname=user)
    return render(re,"viewdetails1.html",{'user':user,'data8':data8,'data9':data9})



def dancepage(re):
    return render(re, "dancepage.html")

def services(re):
    return render(re, "services.html")



def edititem(req,id3):
    if req.method == 'POST':
        name = req.POST['name']
        username = req.POST['username']
        phone = req.POST['phone']
        email = req.POST['email']
        try:
          profile=req.FILES['profile']
          compmusic.objects.filter(pk=id3).update(name=name, username=username, phone=phone, email=email,
                                                  profile=profile)
        except:
          compmusic.objects.filter(pk=id3).update(name=name,username=username,phone=phone,email=email)
        messages.success(req, "successfully updated")
        return redirect(profile1)

def edititem1(req,id5):
    if req.method == 'POST':
        name1 = req.POST['name']
        username1 = req.POST['username']
        phone1 = req.POST['phone']
        email1 = req.POST['email']
        try:
          profile1=req.FILES['profile']
          compdance.objects.filter(pk=id5).update(name=name1, username=username1, phone=phone1, email=email1,
                                                  profile=profile1)
        except:
          compdance.objects.filter(pk=id5).update(name=name1,username=username1,phone=phone1,email=email1)
        messages.success(req, "successfully updated")
        return redirect(profile2)





def adminhome(re):
    data = compdance.objects.filter(status="pending")
    data1 = compmusic.objects.filter(status="pending")
    return render(re, "adminpage/adminhome.html", {'a': data.count, 'b': data1.count})



def login(request):
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['password']
        try:
            data=reguser.objects.get(username=username)
            if data.password==password:
                request.session['user']=username
                messages.success(request, "login success")

                return redirect(ser)
            else:
                messages.error(request, "password incorrect")
                return redirect(login)
                # return HttpResponse("password incorrect")
        except Exception:
            try:
                data = compdance.objects.get(username=username)
                if data.password==password :
                    if data.status=="active":

                        request.session['dance'] = username
                        messages.success(request, "login success")

                        return redirect(profile2)
                    else:
                        messages.error(request, "waiting for approval")
                        return redirect(login)

                else:
                    messages.error(request, "password incorrect")
                    return redirect(login)
            except Exception:
                try:
                    data = compmusic.objects.get(username=username)
                    if data.password == password:
                        if data.status=="active":
                            request.session['music'] = username
                            messages.success(request, "login success")

                            return redirect(profile1)
                        else:
                            messages.error(request, "waiting for approval")
                            return redirect(login)
                    else:
                        messages.error(request, "password incorrect")
                        return redirect(login)
                except Exception:
                    if username=='admin' and password=='admin':
                        request.session['admin']=username
                        messages.success(request, "login success")
                        return redirect(adminhome)
                    else:
                        messages.info(request, "username incorrect")
                        return redirect(login)
    else:

        return render(request,"login.html")


def logout(re):
    if 'music' in re.session:
        re.session.flush()
    return redirect(login)


def mabout(re):
    if re.method=='POST':
        a=re.POST['price']
        b=re.POST['location']
        c=re.POST['achievements']
        d=re.POST['disc']
        e=re.POST['special']
        f=re.POST['experience']
        data=about.objects.create(fprice=a,native=b,achievements=c,disc=d,special=e,experience=f,
                                    mname=compmusic.objects.get(username=re.session['music']))
        data.save()
        messages.success(re,'successfully added')
        return redirect(profile1)


def dabout(re):
    if re.method=='POST':
        a1=re.POST['price']
        b1=re.POST['location']
        c1=re.POST['achievements']
        d1=re.POST['disc']
        e1=re.POST['special']
        f1=re.POST['experience']
        data=about.objects.create(fprice=a1,native=b1,achievements=c1,disc=d1,special=e1,experience=f1,
                                    dname=compdance.objects.get(username=re.session['dance']))
        data.save()
        messages.success(re,'successfully added')
        return redirect(profile2)


def editdm(re,dd):
    if re.method == 'POST':
        a = re.POST['price']
        b = re.POST['location']
        c = re.POST['achievements']
        d = re.POST['disc']
        e = re.POST['special']
        f = re.POST['exp']
        about.objects.filter(pk=dd).update(fprice=a, native=b, achievements=c, disc=d, special=e,experience=f,mname=compmusic.objects.
                                                                   get(username=re.session['music']))
        messages.success(re, "successfully updated")
        return redirect(profile1)

def editdd(re,dk):
    if re.method == 'POST':
        a = re.POST['price']
        b = re.POST['location']
        c = re.POST['achievements']
        d = re.POST['disc']
        e = re.POST['special']
        f = re.POST['exp']
        about.objects.filter(pk=dk).update(fprice=a, native=b, achievements=c, disc=d, special=e,experience=f,dname=compdance.objects.
                                                                   get(username=re.session['dance']))
        messages.success(re, "successfully updated")
        return redirect(profile2)




def addprojects(request):
        if request.method == 'POST':
            f = compmusic.objects.get(username=request.session['music'])
            a = request.POST['category']
            b = request.POST['client']
            c = request.POST['date']
            d = request.POST['projectdetail']
            e = request.FILES['projectimg']

            data = project.objects.create(category=a, client=b, date=c, projectdetail=d,
                                          projectimage=e, mname=f)
            data.save()
            messages.success(request, "successfully added")

        return render(request,'addprojects.html')



def caddprojects(request):
    if request.method == 'POST':
        f2 = compdance.objects.get(username=request.session['dance'])
        a2 = request.POST['category']
        b2 = request.POST['client']
        c2 = request.POST['date']
        d2 = request.POST['projectdetail']
        e2 = request.FILES['projectimg']

        data = project.objects.create(category=a2, client=b2, date=c2, projectdetail=d2, projectimage=e2, dname=f2)
        data.save()
        messages.success(request, "successfully added")

    return render(request, 'caddprojects.html')



def display(re):
    return render(re,'display.html')


l = []
def user(request):
    if request.method == 'POST':
            a = request.POST['name']
            b = request.POST['username']
            c = request.POST['phone']
            d = request.POST['email']
            e = request.POST['password']
            f = request.POST['address']

            try:

                data = reguser.objects.create(name=a, username=b, phone=c, email=d, password=e
                                              ,address=f)
                data.save()

                messages.success(request, "registration sucess")
            except:
                messages.success(request, "username already exists")
                return redirect(user)

            return redirect(login)
    else:


        return render(request, 'registration/user.html')

def danceteam(re):
    if re.method == 'POST':
            a = re.POST['name']
            b = re.POST['username']
            c = re.POST['phone']
            d = re.POST['email']
            e = re.POST['password']
            f=re.FILES['licence']
            try:

                data = compdance.objects.create(name=a, username=b, phone=c, email=d, password=e, license=f,status='pending')
                data.save()
                messages.success(re, "registration success")
            except:
                messages.success(re, "username already exists")
                return redirect(danceteam)

            return redirect(login)
    else:

         return render(re, 'registration/danceteam.html')

def music(re):
    if re.method == 'POST':
            a = re.POST['name']
            b = re.POST['username']
            c = re.POST['phone']
            d = re.POST['email']
            e = re.POST['password']
            f=re.FILES['licence']
            try:

                data = compmusic.objects.create(name=a, username=b, phone=c, email=d, password=e, license=f,status='pending')
                data.save()

                messages.success(re, "registration success")
            except:
                messages.success(re, "username already exists")
                return redirect(music)

            return redirect(login)
    else:

         return render(re, 'registration/music.html')

def uprofile(request):
    if 'user' in request.session:
        user=reguser.objects.get(username=request.session['user'])
        return render(request, "uprofile.html",{'user':user})

def edituser(req,id2):
    if req.method == 'POST':
        username = req.POST['username']
        user_email = req.POST['email']
        password = req.POST['password']
        mobile = req.POST['mobile']
        user_address = req.POST['address']

        try:
            profimg = req.FILES['profile']
            reguser.objects.filter(pk=id2).update(username=username,email=user_email,password=password,
                                                  address=user_address,phone=mobile,profile=profimg)
        except:
            reguser.objects.filter(pk=id2).update(username=username,email=user_email,password=password,
                                                  phone=mobile,address=user_address)

        messages.success(req, "successfully updated")
        return redirect(uprofile)
    else:
        data =reguser.objects.get(pk=id2)
        return render(req, 'edituser.html', {'data':data})

def boooking(re,bok):
    data=compmusic.objects.get(pk=bok)
    data2=about.objects.filter(mname=data)
    return render(re,'buy.html',{'data':data,'data2':data2})

def boooking1(re,bok):
    data=compdance.objects.get(pk=bok)
    data2=about.objects.filter(dname=data)
    return render(re,'buy.html',{'data':data,'data2':data2})
def bookings(re,bk):
    if re.method=='POST':
        user=reguser.objects.get(username=re.session['user'])
        price=re.POST['price']
        bdate=re.POST['setTodaysDate']
        date = datetime.datetime.now()
        address=re.POST['address']
        dis=re.POST['des']
        try:
            mname=compmusic.objects.get(pk=bk)
            data=booking.objects.create(user=user,mname=mname,price=price,date=date,bdate=bdate,
                                        address=address,dis=dis,status="pending")
            data.save()
            messages.success(re,"successfully booked")

            return redirect(ser)
        except:
            dname=compdance.objects.get(pk=bk)
            data=booking.objects.create(user=user,dname=dname,price=price,date=date,bdate=bdate,
                                        address=address,dis=dis,status="pending")
            data.save()
            messages.success(re, "successfully booked")

            return redirect(ser)




def book(re):
        user=reguser.objects.get(username=re.session['user'])
        music=booking.objects.filter(status='active',user=user,mname__isnull=False)
        dance=booking.objects.filter(status='active',user=user,dname__isnull=False)
        return render(re,'book.html',{'music':music,'dance':dance})

def book1(re):
        user=reguser.objects.get(username=re.session['user'])
        da=booking.objects.filter(status='active',user=user)
        return render(re,'book1.html',{'da':da})



def mbook(re):
    f=compmusic.objects.get(username=re.session['music'])
    data=booking.objects.filter(mname=f,status='pending')
    da=booking.objects.filter(mname=f,status='active')
    d=booking.objects.filter(mname=f,status='reject')
    return render(re,'mbook.html',{'data':data,'da':da,'d':d})

def mbook1(re):
    c=compdance.objects.get(username=re.session['dance'])
    data=booking.objects.filter(dname=c,status='pending')
    da=booking.objects.filter(dname=c,status='active')
    d=booking.objects.filter(dname=c,status='reject')
    return render(re,'mbook1.html',{'data':data,'da':da,'d':d})

def accept(req,k):
    booking.objects.filter(pk=k).update(status='active')
    return redirect(mbook)

def daccept(req,k):
    booking.objects.filter(pk=k).update(status='active')
    return redirect(mbook1)

def reject(req,bk):
    booking.objects.filter(pk=bk).update(status='reject')
    return redirect(mbook)

def dreject(req,bk):
    booking.objects.filter(pk=bk).update(status='reject')
    return redirect(mbook1)

def payment(request, a,bid):
        amount = 5000
        a1=int(a)*100
        order_currency = 'INR'
        client = razorpay.Client(
        auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        booking.objects.filter(pk=bid).update(paid='Paid')
        return render(request, "payment.html",{'total':a1})

def success(request):
    user = reguser.objects.get(username=request.session['user'])
    data=booking.objects.filter(user=user,paid='Paid',mname__isnull=False)
    data1=booking.objects.filter(user=user,paid='Paid',dname__isnull=False)
    return render(request,'success.html',{'data':data,'data1':data1})

def paid(re):
    user = compmusic.objects.get(username=re.session['music'])
    data = booking.objects.filter(mname=user, paid='Paid')
    return render(re, 'paid.html', {'data': data})

def paid1(re):
    user = compdance.objects.get(username=re.session['dance'])
    data = booking.objects.filter(dname=user, paid='Paid')
    return render(re, 'paid1.html', {'data': data})

def addreviews(re):
    if 'user' in re.session:
        if re.method=='POST':
            review = re.POST['feedback']
            user = reguser.objects.get(username=re.session['user'])
            feedback=Reviews.objects.create(user=user,review=review)
            feedback.save()
            return render(re,'index.html')
        else:
            return render(index)
    else:
        return render(login)






