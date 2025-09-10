# wc_orders.py
import requests
from config import WC_URL, WC_KEY, WC_SECRET

def fetch_orders():
    try:
        response = requests.get(WC_URL, auth=(WC_KEY, WC_SECRET))
        response.raise_for_status()
        orders = response.json()
        print(f"Fetched {len(orders)} orders from WooCommerce.")
        return orders
    except requests.exceptions.RequestException as e:
        print(f"Error fetching WooCommerce orders: {e}")
        return []
