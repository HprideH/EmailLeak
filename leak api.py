import requests
import json
import os
import time
#https://discord.gg/QPuWDHTnDV @hprideh 
email = input("email: ")
url = 'http://23.95.190.29:5001/search_email'
data = {
    'email': email
}

try:
    print("Searching...")
    response = requests.post(url, json=data, timeout=60)
    
    if response.status_code == 200:
        response_data = response.json()
        results = response_data.get('results', [])
        results_count = len(results)
        results.sort()
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print(f"SEARCH RESULTS DASHBOARD - {data['email']}")
        print("=" * 60)
        print(f"Total results found: {results_count}")
        print("-" * 60)
        
        for i, result in enumerate(results[:10], 1):
            clean_result = result.strip()
            print(f"{clean_result}")
        
        if results_count > 10:
            print(f"... and {results_count - 10} more results")
        print("-" * 60)
        
        with open('leak.txt', 'w', encoding='utf-8') as f:
            for result in results:
                clean_result = result.strip()
                f.write(f"{clean_result}\n")
        
        print(f"All results saved to: leak.txt")
        print("=" * 60)
        
    elif response.status_code == 404:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print(f"SEARCH RESULTS DASHBOARD - {data['email']}")
        print("=" * 60)
        print(f"No results found")
        print("=" * 60)
        
        with open('leak.txt', 'w', encoding='utf-8') as f:
            f.write(f"No results found for: {data['email']}\n")
    
    else:
        print(f"Error: {response.status_code}, {response.text}")

except Exception as e:
    print(f"Connection error: {str(e)}")

input("\nPress Enter to exit...")