"""Test search endpoint with detailed error"""
import requests
import traceback

try:
    url = "http://localhost:8000/api/search?q=trading"
    print(f"Testing: {url}")
    r = requests.get(url)
    print(f"Status: {r.status_code}")
    print(f"Response: {r.text[:500]}")
except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()

