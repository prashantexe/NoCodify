from django.shortcuts import render
from Dragster.models import Wallet


def connect_metamask(request):
    return render(request, 'metamask.html')

def save_wallet_address(request):
    if request.method == 'POST':
        wallet_address = request.POST.get('wallet_address')
        request.session['wallet_address'] = wallet_address
        print(wallet_address)
        obj = Wallet(session=wallet_address)
        obj.save()
        return render(request,'common/index.html',{'wallet':wallet_address})
    else:
        return render(request,'common/index.html',{'wallet':"Your wallet address is the key to unlocking the magic of the blockchain. Connect it now and explore the limitless possibilities!"})

def DisConnect(request):
    if request.method == 'POST':
        obj=Wallet.objects.all().delete()
        return render(request,'common/index.html',{'wallet':"Your wallet address is the key to unlocking the magic of the blockchain. Connect it now and explore the limitless possibilities!"})

    return render(request,'common/index.html',{'wallet':"Problem are Occer"})

def home(request):
    obj = Wallet.objects.all()[::-1]
    try:
        return render(request,'common/index.html',{'wallet':obj[0]})
    except:
        return render(request,'common/index.html',{'wallet':"Your wallet address is the key to unlocking the magic of the blockchain. Connect it now and explore the limitless possibilities!"})
    
def blog(request):
    return render(request,'common/blog-single.html')


