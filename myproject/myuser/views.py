from django.shortcuts import render, redirect,HttpResponse
from .models import *
from django.urls import reverse
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages
from .forms import CreateUserForms
from django.contrib.auth.decorators import login_required

def loginPage(request):
    if request.user.is_authenticated:
      return redirect('home')
    else:  

     if request.method == "POST":
      username =  request.POST.get('username')
      password =  request.POST.get('password')

      user=authenticate(request,   username=username,    password=password)

      if user is not None:
         request.session['username'] = username
         login(request,user)
         url = reverse('home')

         return redirect(url)
      else:
         messages.info(request,'Username Or Password Is Incorrect')
         

     
    return render(request,'user/login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForms()
        if request.method == "POST":
            form = CreateUserForms(request.POST)
            if form.is_valid():
                form.save()
                url = reverse('login') 
                return redirect(url)
        else:
          
            for field, errors in form.errors.items():
                for error in errors:
                   
                    if field == 'password2' and 'password1' in errors:
                        continue
                    messages.error(request, f"{field}: {error}")
        context = {'form': form}
        return render(request, 'user/signup.html', context)




def home_view(request,):
    username = request.session.get('username')
    context={
       'username': username
       
    }
    return render(request, 'user/home.html',context)




def customer(request):

    return render(request, 'user/customer.html',)


def user_balance(request):
    customer = request.user

    balance = 0
    try:
        latest_deposit = Deposit.objects.filter(customer=customer).latest('date_time')
        balance = latest_deposit.balance
    except Deposit.DoesNotExist:
       
        pass
    
    context = {
        'username': customer.username,
        'customer': customer,
        'balance': balance
    }
    return render(request, 'user/user_balance.html',context)





def user_withdrawl(request):
    customer = request.user

    balance = 0
    try:
        latest_deposit = Deposit.objects.filter(customer=customer).latest('date_time')
        balance = latest_deposit.balance
    except Deposit.DoesNotExist:
       
        pass
    
    context = {
        'username': customer.username,
        'customer': customer,
        'balance': balance
    }
    if request.method == 'POST':
        amount = request.POST.get('amount')
        if amount:
            try:
                amount = Decimal(amount)  # Convert to Decimal
                if amount > Decimal('0'):  # Compare with Decimal

                    customer = request.user 
                    if customer:
                       
                        previous_deposits = Deposit.objects.filter(customer=customer)
                        previous_total = sum(deposit.amount for deposit in previous_deposits)
                        if amount <= previous_total:
                            new_balance = previous_total - amount
                            try:
                                Deposit.objects.create(
                                    customer=customer,
                                    amount=-amount,  # Withdrawal amount is negative
                                    balance=new_balance
                                )
                                messages.success(request, f'Withdrawal of {amount} successfully made.')
                                return redirect('user_withdrawl')  
                            except IntegrityError:
                                messages.error(request, 'Failed to create withdrawal record.')
                        else:
                            messages.error(request, 'Insufficient balance.')
                    else:
                        messages.error(request, 'Customer data not found.')
                else:
                    messages.error(request, 'Please enter a valid positive amount.')
            except ValueError:
                messages.error(request, 'Please enter a valid numeric amount.')
        else:
            messages.error(request, 'Please enter an amount.')



    return render(request, 'user/user_withdrawl.html',context)


from decimal import Decimal
from django.db import IntegrityError

@login_required


def user_deposit(request):

    customer = request.user

    balance = 0
    try:
        latest_deposit = Deposit.objects.filter(customer=customer).latest('date_time')
        balance = latest_deposit.balance
    except Deposit.DoesNotExist:
       
        pass
    
    context = {
        'username': customer.username,
        'customer': customer,
        'balance': balance
    }
    if request.method == 'POST':
        amount = request.POST.get('amount')
        if amount:
            try:
                amount = Decimal(amount)  # Convert to Decimal
                if amount > Decimal('0'):  # Compare with Decimal

                    customer = request.user 
                    if customer:
                       
                        previous_deposits = Deposit.objects.filter(customer=customer)
                        previous_total = sum(deposit.amount for deposit in previous_deposits)
                        new_balance = previous_total + amount
                        
                        try:
                            Deposit.objects.create(
                                customer=customer,
                                amount=amount,
                                balance=new_balance
                            )
                            messages.success(request, f'Deposit of {amount} successfully made.')
                            return redirect('user_deposit')  
                        except IntegrityError:
                            messages.error(request, 'Failed to create deposit record.')
                    else:
                        messages.error(request, 'Customer data not found.')
                else:
                    messages.error(request, 'Please enter a valid positive amount.')
            except ValueError:
                messages.error(request, 'Please enter a valid numeric amount.')
        else:
            messages.error(request, 'Please enter an amount.')
    return render(request, 'user/user_deposit.html',context)



def LogoutPage(request):
   logout(request)
   url = reverse('login')  
    
    
   return redirect(url)

