# config.py

# WooCommerce credentials
WC_URL = "http://localhost:10004/wp-json/wc/v3/orders"
WC_KEY = "ck_fab7c6a47583ccfa34608f95eb796330bed0896d"
WC_SECRET = "cs_601db69f0f80e014631ecf2c4ecaab2d3d89c1a7"

# Zoho credentials
ZOHO_ACCESS_TOKEN = "1000.3c2b2849328e9cbbbdb8cd2c292ef7c5.13d014a6a24d934e40c580eeb14db6c8"
ZOHO_HEADERS = {
    "Authorization": f"Zoho-oauthtoken {ZOHO_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}
