from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Paytm import Checksum
from .models import PaymentData
from django.http import HttpResponse
import uuid

MKEY = 'KfnO&U9D9bJ_4_J3'





def t_int_reg(request):
   
    
        
    order_id = 'Ordesdfsfdsfk'
    param_dict = {
        'MID': 'plORHR51347886962392',
        'ORDER_ID': order_id,
        'TXN_AMOUNT': '7500.00',
        'CUST_ID': 'acfff@paytm.com',
        'INDUSTRY_TYPE_ID': 'Retail',
        'WEBSITE': 'WEBSTAGING',
        'CHANNEL_ID': 'WEB',
        'CALLBACK_URL': 'http://127.0.0.1:8000/r/handvrequest/',
    }
    param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(
        param_dict, MKEY)
    return render(request, 'teamregistrations/paytm.html', {'param_dict': param_dict})

    





@csrf_exempt
def handel_verification_request(request):
    form = request.POST
    responce_dict = {}
    for i in form.keys():
        responce_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(responce_dict, MKEY, checksum)
    if verify:
        if responce_dict['RESPCODE'] == '01':
            print('ORDER SUCCESSFUL')
        else:
            print('CANCLED ORDER ' + responce_dict['RESPMSG'])
    print(responce_dict)
    return render(request, 'teamregistrations/finalstatus.html', {'response': responce_dict})



