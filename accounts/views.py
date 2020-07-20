from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.utils import timezone

from .forms import CreateUserForm
from .forms import ReportForm
from .models import Report
from .decorators import unauthenticated_user, allowed_users, admin_only, customer_only
from .filters import reportFilter
from .filters import userFilter
from .models import Customer

# Create your views here.


@login_required(login_url='login')
def homePage(request):
    return render(request, 'accounts/index.html')
 
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            user.save()

            messages.success(request,'Account was created for '+ username)

            return redirect('login')
        
    context = {'form':form}
    return render(request, 'accounts/register.html',context)
    
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'User name or password isnt correct')

    context = {}
    return render(request, 'accounts/login.html', context)
    
def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def reprtPage(request):
    reports = Report.objects.all()

    context = {'reports':reports}
    return render(request, 'accounts/requestForm.html' , context)

@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
@admin_only
def manage_users(request):
    
    users = User.objects.all()
    myFilter = userFilter(request.GET, queryset=users)
    users = myFilter.qs

    context = {'users':users, 'MyFilter':myFilter}

    return render(request, 'accounts/manager_users.html', context)

@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
@admin_only
def manage_reports(request):
    reports = Report.objects.all()
    
    myFilter = reportFilter(request.GET, queryset=reports)
    reports = myFilter.qs

    Waiting = reports.filter(status='Waiting').count()
    onTretamant = reports.filter(status='onTretamant').count()
    Done = reports.filter(status='Done').count()

    context = {'reports':reports, 'Waiting':Waiting, 
    'onTretamant':onTretamant, 'Done':Done, 'MyFilter':myFilter}

    return render(request, 'accounts/manager_reports.html', context)


@login_required(login_url='login')
def formPage(request,id=0):
    if request.method == 'GET':
        if id==0:
            form = ReportForm()
        else:
            report = Report.objects.get(pk=id)
            form = ReportForm(instance=report)
        return render(request, 'accounts/requestForm.html',{'form':form})
    else:
        if id==0:
            form = ReportForm(request.POST)
        else:
            report = Report.objects.get(pk=id)
            form = ReportForm(request.POST,instance=report)
        if form.is_valid():
            form.save()
        return redirect('private')

@login_required(login_url='login')
def privatePage(request):
    reports = Report.objects.all()
    count_reports = reports.count()
    context = {'reports':reports,'count_reports':count_reports}

    return render(request,'accounts/private.html', context)


@login_required(login_url='login')
def progressPage(request,pk_report):
    report = get_object_or_404(Report,pk=pk_report)
    context = {'report':report}

    return render(request,'accounts/progress.html',context)

@login_required(login_url='login')
def updateReport(request, pk):
    form = ReportForm(request,pk)
    context = {'form':form}
    return render(request,'accounts/form.html',context)

@login_required(login_url='login')
def deleteReport(request,id):
    report = Report.objects.get(pk=id)
    report.delete()
    return redirect('manage_reports')

