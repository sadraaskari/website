from django.shortcuts import render, redirect
import requests
from .models import Transaction
import json


def home(request):
    return render(request, 'accounting/home.html')


def make_payment(request, pk):
    transaction_data = {"merchant_id": Transaction.objects.get(pk=pk).merchant_id,
                        "amount": Transaction.objects.get(pk=pk).amount,
                        "callback_url": Transaction.objects.get(pk=pk).callback_url,
                        "description": Transaction.objects.get(pk=pk).description,
                        }
    data = json.dumps(transaction_data)

    response = requests.post('https://api.zarinpal.com/pg/v4/payment/request.json', headers={'accept': 'application/json', 'content-type': 'application/json'}, data=data)
    response_data = response.json()
    if response_data['errors']:
        return render(request, 'accounting/error.html', {'response_data': response_data})
    elif response_data['data']['code'] == 100:
        authority = response_data['data']['authority']
        payment_url = 'https://www.zarinpal.com/pg/StartPay/' + authority
        return redirect(payment_url)
    else:
        return render(request, 'accounting/home.html')


def payment_status(request, pk):
    status = request.GET.get('Status')
    if status == 'OK':
        transaction_data = {'merchant_id': '1344b5d4-0048-11e8-94db-005056a205be',
                            'amount': Transaction.objects.get(pk=pk).amount}
        serializer = json.dumps(transaction_data)
        serializer_data = serializer.data
        serializer_data['authority'] = request.GET.get('Authority')
        response = requests.post('https://api.zarinpal.com/pg/v4/payment/verify.json', data=serializer_data)
        response_data = response.json()
        if response_data['data']['code'] == 100:
            status = 1
            ref_id = response_data['data']['ref_id']
            transaction = Transaction(
                status=status,
                ref_id=ref_id
            )
            transaction.save()
            return render(request, 'accounting/home.html', {'ref_id': ref_id})
        else:
            return render(request, 'accounting/error.html')
    else:
        return render(request, 'accounting/error.html')

