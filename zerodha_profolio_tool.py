import os
import webbrowser
from typing import Optional, Tuple
from dotenv import load_dotenv
from kiteconnect import KiteConnect
import logging

# Implement a tiny callback HTTP server to capture the `request_token`
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
from urllib.parse import urlparse, parse_qs
import time

def method_to_test():
    logging.info("This is a test method.")
    return "Test successful!"

def generate_session(kite: object, request_token: str) -> Tuple[object, str]:
	api_secret = os.getenv("zerodha_api_secret")
	data = kite.generate_session(request_token, api_secret=api_secret)
	access_token = data["access_token"]
	kite.set_access_token(access_token)
	return kite, access_token

def login(api_key: Optional[str] = None,
		  api_secret: Optional[str] = None,
		  open_in_browser: bool = True) -> Tuple[str, object]:
	"""
	Load `.env` (if available), read API key/secret and redirect URI from environment,
	create a `KiteConnect` instance, build the login URL and optionally open it in the
	default web browser.

	Returns a tuple `(login_url, kite)` where `kite` is the `KiteConnect` instance.

	Notes:
	- After the user completes login, the broker will redirect to `redirect_uri` with
	  a `request_token` parameter. Use `kite.generate_session(request_token, api_secret)`
	  to obtain an access token and then call `kite.set_access_token(access_token)`.
	"""
	# load .env if python-dotenv is available
	if load_dotenv:
		load_dotenv()



	api_key = api_key or os.getenv("zerodha_api_client")
	api_secret = api_secret or os.getenv("zerodha_api_secret")


	if not api_key or not api_secret:
		raise ValueError("KITE_API_KEY and KITE_API_SECRET must be provided either in environment or as arguments.")

	kite = KiteConnect(api_key=api_key)
	
	login_url = kite.login_url()

	if open_in_browser:
		webbrowser.open(login_url)

	return login_url, kite


def get_current_holdings(kite: object) -> list:
    """
    Fetch and return the current holdings from the Zerodha account.
    """
    holdings = kite.holdings()
    holdings=kite.holdings()


    def retain(original_dict:dict):
        retain_keys = ['tradingsymbol','exchnage','isin','price','quantity','average_price','last_price','close_price']
        return_dict ={k: original_dict[k] for k in retain_keys if k in original_dict}
        return return_dict

    minified_holdings=[]
    for holding in holdings:
        minified_holdings.append(retain(holding))

    return minified_holdings