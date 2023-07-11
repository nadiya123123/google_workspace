from django.shortcuts import render
import requests
from .quickstart import access_token
from .quickstart import CUSTOMER_DOMAIN


# Create your views here.

def customer_list(request):
    url = f"https://www.googleapis.com/apps/reseller/v1/customers/{CUSTOMER_DOMAIN}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        customers = response.json().get("customers", [])
        return render(request, 'customer_list.html', {'customers': customers})
    else:
        error_message = "An error occurred while retrieving customer details."
        return render(request, 'error.html', {'error_message': error_message})

def user_list(request):
    customer_id = "C01ld0dos"
    url = f"https://www.googleapis.com/admin/directory/v1/users"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    params = {
        "customer": customer_id,
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        users = response.json().get("users", [])
        return render(request, 'user_list.html', {'users': users})
    else:
        error_message = "An error occurred while retrieving user details."
        return render(request, 'error.html', {'error_message': error_message})

def subscription_list(request):

    url = f"https://www.googleapis.com/apps/reseller/v1/subscriptions?customerAuthToken={access_token}&customerDomain={CUSTOMER_DOMAIN}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        subscriptions = response.json().get("subscriptions", [])
        return render(request, 'subscription_list.html', {'subscriptions': subscriptions})
    else:
        error_message = "An error occurred while retrieving subscription details."
        return render(request, 'error.html', {'error_message': error_message})
