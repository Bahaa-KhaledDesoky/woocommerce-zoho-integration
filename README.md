# WooCommerce to Zoho CRM Integration

This project automates the process of syncing WooCommerce orders with Zoho CRM. Orders from WooCommerce are fetched, corresponding Contacts are created or retrieved in Zoho CRM, and Deals are created for each order.

---

## Features

1. **Fetch WooCommerce Orders**
   - Pulls orders from WooCommerce via REST API.

2. **Contact Management**
   - Checks if a contact exists in Zoho CRM by email.
   - Creates a new contact if it doesn't exist.

3. **Deal Creation**
   - Creates a deal in Zoho CRM for each WooCommerce order.
   - Links the deal to the corresponding contact.
   - Adds order details (line items, total, etc.) as the description.

---

## Prerequisites

- Python 3.x
- `requests` library
- WooCommerce API credentials (Consumer Key & Secret)
- Zoho CRM OAuth access token

Install Python dependencies:

```bash
pip install requests
