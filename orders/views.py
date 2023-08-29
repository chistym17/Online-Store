from django.shortcuts import render

def completedOrder(request):
    return render(request,'orders/order_complete.html')



