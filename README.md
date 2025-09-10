# WooCommerce to Zoho CRM Integration

This project automates syncing WooCommerce orders with Zoho CRM. Orders from WooCommerce are fetched, corresponding Contacts are created or retrieved in Zoho CRM, and Deals are created for each order.

## Features

- **Fetch WooCommerce Orders:** Pull orders from WooCommerce via REST API.
- **Contact Management:**  
  - Checks if a contact exists in Zoho CRM by email.  
  - Creates a new contact if it doesn't exist.
- **Deal Creation:**  
  - Creates a deal in Zoho CRM for each WooCommerce order.  
  - Links the deal to the corresponding contact.  
  - Adds order details (line items, total, etc.) as the description.

## Prerequisites

- Python 3.x  
- `requests` library  
- WooCommerce API credentials (Consumer Key & Secret)  
- Zoho CRM OAuth access token  

Install Python dependencies:

```bash
pip install requests
Files
fetch_orders_create_deals.py: Fetches orders from WooCommerce and creates contacts and deals in Zoho CRM.

create_deal_example.py: Example script to create a single deal in Zoho CRM from a sample order.

Usage
Update WooCommerce credentials in fetch_orders_create_deals.py:

python
Copy code
wc_url = "http://yourstore.com/wp-json/wc/v3/orders"
wc_key = "<your_consumer_key>"
wc_secret = "<your_consumer_secret>"
Update Zoho credentials:

python
Copy code
access_token = "<your_zoho_access_token>"
headers = {
    "Authorization": f"Zoho-oauthtoken {access_token}",
    "Content-Type": "application/json"
}
Run the script:

bash
Copy code
python fetch_orders_create_deals.py
The script prints each order number and the status of deal creation.

Notes
Ensure WooCommerce REST API is enabled.

Zoho CRM access token must be valid and have proper permissions.

The script handles multiple orders by looping through all fetched WooCommerce orders.

Author
Bahaa Khaled Desoky
Project for automating WooCommerce → Zoho CRM workflow.

pgsql
Copy code

---

If you want, I can also **enhance it with a Table of Contents, badges (Python version, license, etc.), and sections like Contributing/License** to make it look more professional on GitHub.  

Do you want me to do that next?






