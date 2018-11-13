from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import re 
from users.models import Passport

# Create your views here.

def register(request):
    return render(request,'users/register.html')


def register_handle(request):
    
    username = request.POST.get('user_name')

    password = request.POST.get('pwd')
    
    email = request.POST.get('email')

    if not all([username,password,email]):
        return render(request,'user/register.html',{'errmsg':'参数不能为空' })

    try:
        passport.object.add_one_passport(username=username, password=password, email=email)
    except:
        return render(request, 'users/register.html', {'errmsg': '用户名已存在！'})

    # 注册完，还是返回注册页。
    return redirect(reverse('user:register'))

def login(request):
    if request.COOKIES.get('username'):
        username = request.COOKIES.get('username')
        checked = 'checked'

    else:
        username = ''

        checked = ''
    context = {
        'username':username,
        'checked':checked,
        }

    return render(request,'users/login.html',context)



def login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    remeber = request.POST.get('remeber')

    if not all([username,password,remeber]):
        return JsonResponse({'res':2})
    
    password = Passport.object.get_one_passport(username = username,password=password)

    if passport:
        next_url = reverse('books:index')
        jres = JsonResponse({'res':1,'next_url':next_url})

        #判断是否需要记住用户名
        if remeber == 'true':
            jres.set_cookie('username',username,max_length=7*24*3600)

        else:
            jres.delete_cookie('username')

        request.session['islogin']=True
        request.session['username']=username
        request.session['passport_id']=passport_id
        return jres
    else:
        return JsonResponse({'res':0})

    
def logout(request):
    request.session.flush()
    return redirect(reverse('books:index'))_
