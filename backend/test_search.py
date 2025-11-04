"""
Test search endpoint
"""
import sys
from pathlib import Path
import requests

backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

try:
    # Test search endpoint
    url = "http://localhost:8000/api/search?q=trading"
    response = requests.get(url)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:500]}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"\nResults count: {len(data.get('results', []))}")
        print(f"Total: {data.get('total', 0)}")
        if data.get('results'):
            print(f"First result: {data['results'][0]}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

