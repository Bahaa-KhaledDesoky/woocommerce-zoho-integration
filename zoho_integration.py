# zoho_integration.py
import requests
import json
from config import ZOHO_HEADERS

ZOHO_CONTACTS_URL = "https://www.zohoapis.com/crm/v2/Contacts"
ZOHO_DEALS_URL = "https://www.zohoapis.com/crm/v2/Deals"

def get_or_create_contact(order):
    email = order['billing']['email']
    search_url = f"{ZOHO_CONTACTS_URL}/search?email={email}"
    
    try:
        search_resp = requests.get(search_url, headers=ZOHO_HEADERS)
        if search_resp.status_code == 200 and 'data' in search_resp.json():
            contact_id = search_resp.json()['data'][0]['id']
            return contact_id
    except Exception as e:
        print(f"Error searching contact: {e}")

    # Create contact if not found
    contact_data = {
        "data": [
            {
                "First_Name": order['billing']['first_name'],
                "Last_Name": order['billing']['last_name'],
                "Email": email,
                "Phone": order['billing']['phone']
            }
        ]
    }

    try:
        contact_resp = requests.post(ZOHO_CONTACTS_URL, headers=ZOHO_HEADERS, data=json.dumps(contact_data))
        contact_resp.raise_for_status()
        contact_id = contact_resp.json()['data'][0]['details']['id']
        print(f"Created contact: {email}")
        return contact_id
    except Exception as e:
        print(f"Error creating contact: {e}")
        return None

def deal_exists(order_number):
    search_url = f"{ZOHO_DEALS_URL}/search?criteria=(Deal_Name:equals:{order_number})"
    try:
        search_resp = requests.get(search_url, headers=ZOHO_HEADERS)
        data = search_resp.json()
        if 'data' in data and len(data['data']) > 0:
            return True
        return False
    except:
        return False

def create_deal(order, contact_id):
    if deal_exists(f"Order #{order['number']}"):
        print(f"Deal for Order #{order['number']} already exists. Skipping.")
        return

    products_description = ", ".join([f"{item['name']} x {item['quantity']}" for item in order['line_items']])
    deal_data = {
        "data": [
            {
                "Deal_Name": f"Order #{order['number']}",
                "Amount": float(order['total']),
                "Stage": "Qualification",
                "Contact_Name": {"id": contact_id},
                "Description": f"Products Ordered: {products_description}"
            }
        ]
    }

    try:
        deal_resp = requests.post(ZOHO_DEALS_URL, headers=ZOHO_HEADERS, data=json.dumps(deal_data))
        print(f"Order #{order['number']} -> Deal status: {deal_resp.status_code}")
    except Exception as e:
        print(f"Error creating deal for Order #{order['number']}: {e}")
