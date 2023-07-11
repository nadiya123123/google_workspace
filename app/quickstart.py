from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import requests



JSON_PRIVATE_KEY_FILE = 'credentials.json'
RESELLER_ADMIN_USER = 'admin@goog-test.febno.in'
CUSTOMER_DOMAIN = 'goog-test.nadiya.febno.in'
CUSTOMER_SITE = 'https://www.goog-test.nadiya.febno.in'


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/apps.order',
          'https://www.googleapis.com/auth/siteverification',
          'https://www.googleapis.com/auth/admin.directory.user',
          ]


# CREDENTIALS #############################################
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    JSON_PRIVATE_KEY_FILE, SCOPES).create_delegated(RESELLER_ADMIN_USER)


access_token = credentials.get_access_token().access_token
# print("access_token",access_token)


reseller_service = build(
    serviceName='reseller', version='v1', credentials=credentials)
# print(reseller_service)

directory_service = build(
    serviceName='admin', version='directory_v1', credentials=credentials)
# print(directory_service)

verification_service = build(
    serviceName='siteVerification', version='v1', credentials=credentials)
# print(verification_service)

# #
# # # ....................to retrieve customer information.............................
# url = "https://www.googleapis.com/apps/reseller/v1/customers"
# headers = {
#     "Authorization": f"Bearer {access_token}",
#     "Content-Type": "application/json"
# }
# body = {
#     'customerDomain': CUSTOMER_DOMAIN,
#     'alternateEmail': 'nadi@gmail.com',
#     'postalAddress': {
#         'contactName': 'nadi',
#         'organizationName': 'Acme Corp',
#         'postalCode': '10009',
#         'countryCode': 'US'
#     }
# }
#
# response = requests.post(url, headers=headers, json=body)
#
# if response.status_code == 200:
#     customer_id = response.json().get("customerId")
#     print("Customer created successfully. Customer ID:", customer_id)
# else:
#     print("An error occurred:")
#     print(response.json())
# #
# #
# #
# # # ............................Create first admin user...............................
# #
# url = "https://www.googleapis.com/admin/directory/v1/users"
# headers = {
#     "Authorization": f"Bearer {access_token}",
#     "Content-Type": "application/json"
# }
# user_body = {
#     'primaryEmail': 'marty.mcfly@' + CUSTOMER_DOMAIN,
#     'name': {
#         'givenName': 'Marty',
#         'familyName': 'McFly',
#     },
#     'password': 'Timecircuit88'
# }
# response = requests.post(url, headers=headers, json=user_body)
# if response.status_code == 200:
#     print(response.json())
# else:
#     print("Error:",response.json())
#
# # #
# # # ..................... request to retrieve user list ........................
#
# customer_id = "C01ld0dos"
# url = f"https://www.googleapis.com/admin/directory/v1/users"
# headers = {
#     "Authorization": f"Bearer {access_token}",
#     "Content-Type": "application/json"
# }
# params = {
#     "customer": customer_id,
# }
#
# response = requests.get(url, headers=headers, params=params)
# if response.status_code == 200:
#     users = response.json().get("users", [])
#     user_ids = [user.get("id") for user in users]
#     print("User IDs:", user_ids)
# else:
#     print("An error occurred:",response.json())
# #
#
#
# # # ........................Promote user to admin status..................
# #
# user_key = '107637345770882900763'
# headers = {
#     "Authorization": f"Bearer {access_token}",
#     "Content-Type": "application/json"
# }
# user_body = {"status": True}
#
# response = requests.post(f"https://www.googleapis.com/admin/directory/v1/users/{user_key}/makeAdmin", headers=headers, json=user_body)
#
# if response.status_code == 200:
#     print("User promoted to admin successfully")
# else:
#     print("An error occurred:",response.status_code)
# #
# #
# # # ....................to check user is admin or not................................
#
# user_key = '107637345770882900763'
# url = f"https://www.googleapis.com/admin/directory/v1/users/{user_key}"
# headers = {
#     "Authorization": f"Bearer {access_token}",
#     "Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers)
#
# if response.status_code == 200:
#     user_data = response.json()
#     is_admin = user_data.get("isAdmin", False)
#
#     if is_admin:
#         print("User is an admin")
#     else:
#         print("User is not an admin")
# else:
#     print("An error occurred:",response.json())
# #
# # #
# # # ............................ Create subscription resource.......................
#
#
# id_customer = "C01ld0dos"
# url =f'https://www.googleapis.com/apps/reseller/v1/customers/{id_customer}/subscriptions'
# headers = {
#     "Authorization": f"Bearer {access_token}",
#     "Content-Type": "application/json"
# }
# data = {
#     "customerId": CUSTOMER_DOMAIN,
#     "skuId": "1010020027",
#     "plan": {
#         "planName": 'ANNUAL_MONTHLY_PAY',
#     },
#     "seats": {
#         "numberOfSeats": 5
#     },
#     "renewalSettings": {
#         "renewalType": 'RENEW_CURRENT_USERS_MONTHLY_PAY'
#     }
# }
# response = requests.post(url, headers=headers, json=data)
# if response.status_code == 200:
#     subscription_data = response.json()
#     print("Subscription created successfully:",subscription_data)
# else:
#     print("An error occurred:",response.status_code)
#
# # #
# # # ...................................next user creation..................................
#
# url = "https://www.googleapis.com/admin/directory/v1/users"
# headers = {
#     "Authorization": f"Bearer {access_token}",
#     "Content-Type": "application/json"
# }
#
# user_body = {
#     'primaryEmail': 'mimi.mani@' + CUSTOMER_DOMAIN,
#     'name': {
#         'givenName': 'mim',
#         'familyName': 'mani',
#     },
#     'password': '1234567890'
# }
# response = requests.post(url, headers=headers, json=user_body)
# if response.status_code == 200:
#     user_data = response.json()
#     print("User created successfully:",user_data)
# else:
#     print("An error occurred:",response.json())
#
#
#
# #
# # #...............get all user details.........................
# #
# url = f"https://www.googleapis.com/admin/directory/v1/users"
# headers = {
#     "Authorization": f"Bearer {access_token}"
# }
# params = {
#     "domain": CUSTOMER_DOMAIN
# }
#
# response = requests.get(url, headers=headers, params=params)
#
# if response.status_code == 200:
#     users_data = response.json().get("users", [])
#     print("Users:")
#     for user in users_data:
#         print(user)
# else:
#     print("An error occurred:", response.status_code)
#
#
# #
# # #
# # # ................................get subscription id.......................................
# #
# url = f"https://www.googleapis.com/apps/reseller/v1/subscriptions?customerAuthToken={access_token}&customerDomain={CUSTOMER_DOMAIN}"
# headers = {
#     "Authorization": f"Bearer {access_token}",
#     "Content-Type": "application/json"
# }
# response = requests.get(url, headers=headers)
# if response.status_code == 200:
#     subscriptions = response.json().get("subscriptions", [])
#     subscription_ids = [subscription.get("subscriptionId") for subscription in subscriptions]
#     print("Subscription IDs:", subscription_ids)
# else:
#     print("An error occurred:",response.json())
#

#
# # # ..................user updation.........................
# # #
# user_id = "107637345770882900763"
# url = f"https://www.googleapis.com/admin/directory/v1/users/{user_id}"
# headers = {
#     "Authorization": f"Bearer {access_token}",
#     "Content-Type": "application/json"
# }
# user_data = {
#     "name": {
#         "givenName": "nike",
#         "familyName": "th"
#     },
#     "password": "nik1401999"
# }
# response = requests.put(url, headers=headers, json=user_data)
# if response.status_code == 200:
#     updated_user = response.json()
#     print("Updated User:",updated_user)
# else:
#     print("An error occurred:",response.json())
#
#
# #
# # # ..........................customer details...............................
#
# url = f"https://www.googleapis.com/apps/reseller/v1/customers/{CUSTOMER_DOMAIN}"
# headers = {
#     "Authorization": f"Bearer {access_token}"
# }
# response = requests.get(url, headers=headers)
# if response.status_code == 200:
#     customer_data = response.json()
#     print("Customer Details:",customer_data)
# else:
#     print("An error occurred:",response.json())
#
#
# #
# #
# # # .........................suspend.......................................
#
# id_customer = "C01ld0dos"
# subscription_id='5570815540'
# url =f"https://www.googleapis.com/apps/reseller/v1/customers/{id_customer}/subscriptions/{subscription_id}/suspend"
# headers = {
#     "Authorization": f"Bearer {access_token}"
# }
# response = requests.post(url, headers=headers)
# if response.status_code == 200:
#     print("Subscription suspended successfully.")
# else:
#     print("An error occurred:",response.status_code)
#
# #
# # #..............................activate...................................

# id_customer = "C01ld0dos"
# subscription_id='5570815540'
# url = f"https://www.googleapis.com/apps/reseller/v1/customers/{id_customer}/subscriptions/{subscription_id}/activate"
# headers = {
#     "Authorization": f"Bearer {access_token}",
#     "Content-Type": "application/json"
# }
# response = requests.post(url, headers=headers)
# if response.status_code == 200:
#     activation_data = response.json()
#     print("Subscription activated successfully:",activation_data)
# else:
#     print("An error occurred:",response.status_code)
#
# # # #
# # #........................user delete.........................................
# #
#
# user_key = "113803129205846834209"
# url = f"https://www.googleapis.com/admin/directory/v1/users/{user_key}"
# headers = {
#     "Authorization": f"Bearer {access_token}"
# }
# response = requests.delete(url, headers=headers)
# if response.status_code == 204:
#     print("User deleted successfully.")
# else:
#     print("An error occurred:", response.status_code)
#
#
# # #...................undelete......................
#
# user_key = "113803129205846834209"
# url = f"https://www.googleapis.com/admin/directory/v1/users/{user_key}/undelete"
# headers = {
#     "Authorization": f"Bearer {access_token}"
# }
#
# response = requests.post(url, headers=headers)
# if response.status_code == 200:
#     print("User undeleted successfully.")
# else:
#     print("An error occurred:", response.status_code)

#................seat updation...................

id_customer='C01ld0dos'
subscription_id='5570815540'
url = f'https://www.googleapis.com/apps/reseller/v1/customers/{id_customer}/subscriptions/{subscription_id}/changeSeats'
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}
data = {
        "numberOfSeats": 7,
        "maximumNumberOfSeats": 10,
        "kind": 'subscriptions#seats'
    }
response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    print(" seat updated.")
else:
    print("An error occurred:", response.status_code)
