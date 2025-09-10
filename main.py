# main.py
from wc_orders import fetch_orders
from zoho_integration import get_or_create_contact, create_deal

def main():
    orders = fetch_orders()
    for order in orders:
        contact_id = get_or_create_contact(order)
        if contact_id:
            create_deal(order, contact_id)

if __name__ == "__main__":
    main()
