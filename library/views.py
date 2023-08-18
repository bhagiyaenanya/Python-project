from django.shortcuts import render,redirect



from library.models import registermodel
def signin(request):
    if request.method == "POST":
        # try:
            resp_obj=registermodel.objects.create(firstname=request.POST.get('uname'),
                                                  lastname=request.POST.get('password'),
                                                  userid=request.POST.get('mnum'),
                                                  password=request.POST.get('pwd'),
                                                  mblenum=request.POST.get('phno'),
                                                  email=request.POST.get('eml'),
                                                  gender=request.POST.get('gen'),
                                                  )
        # except:
        #     pass

    return render(request,'lib.html')



from library.models import book_details
def index(request):
    if request.method == "POST":
        # try:
            resp_obj=book_details.objects.create( bookname=request.POST.get('bname'),
                                                  code=request.POST.get('cd'),
                                                  category=request.POST.get('cat'),
                                                  author=request.POST.get('writer'),
                                                  status=request.POST.get('stat'),
                                                  created_by=request.POST.get('crb'),
                                                  created_date=request.POST.get('crd'),
                                                  updated_by=request.POST.get('upb'),
                                                  updated_date=request.POST.get('upd'),
                                                  )
            id(resp_obj.id)
            print(id)
            return redirect('star')
        # except:
        #     pass

    return render(request,'bookdetails.html')




from library.models import order_detail
def signup(request):
    if request.method == "POST":
        # try:
            resp_obj=order_detail.objects.create( bookid_id=request.POST.get('bid'),
                                                  count=request.POST.get('count'),
                                                  price=request.POST.get('rate'),
                                                  delivery_date=request.POST.get('del'),
                                                  status=request.POST.get('stat'),
                                                  created_by=request.POST.get('crb'),
                                                  created_date=request.POST.get('crd'),
                                                  updated_by=request.POST.get('upb'),
                                                  updated_date=request.POST.get('upd'),
                                                  )
            id(resp_obj.id)
            print(id)
            return redirect('sun')

        # except:
        #     pass

    return render(request,'orderdetails.html')


def sign(request):
    if request.method =="POST":
        a=request.POST.get('name')
        b=request.POST.get('pwd')
        try:
            check = registermodel.objects.get(userid=a,password=b)
            return redirect('star')
        except:
            pass

    return render(request,"book.html")

def sun(request):
    obj = order_detail.objects.all()
    return render(request, "sun.html", {'data': obj})


def star(request):
    obj=book_details.objects.all()
    return render(request,"start.html",{'data':obj})

def login(request):
    obj=registermodel.objects.all()
    return render(request,"login.html",{'data':obj})

def add1(request):
    return redirect('signup')

def order(request):
    return redirect('star')

def book(request):
    return redirect('sun')

def add(request):
    return redirect('index')




def edit1(request,pk):

    obj=order_detail.objects.get(id=pk)
    if request.method == "POST":
        print(request.POST.get('bid'))
        obj_data=order_detail.objects.filter(id=pk).update(count=request.POST.get('count'),price=request.POST.get('rate'),
                                                           status=request.POST.get('stat'))
        return redirect('sun')

    return render(request,'newfile.html',{'obj':obj})



def edit(request,ps):
    obj=book_details.objects.get(id=ps)
    if request.method == "POST":
       print(request.POST.get('cd'))
       obj_data =book_details.objects.filter(id=ps).update(author=request.POST.get('writer'),category=request.POST.get('cat'),)
       return redirect('star')

    return render(request,'newedit.html',{'obj':obj})


def table(request,rr):
    try:
        order_detail.objects.filter(id=rr).delete()
        return redirect('sun')
    except:
        pass
    return render(request, 'newfile.html', {'obj': 'obj'})

def table1(request,rd):
     try:
          book_details.objects.filter(id=rd).delete()
          return redirect('star')
     except:
         pass
     return render(request, 'newedit.html', {'obj': 'obj'})
