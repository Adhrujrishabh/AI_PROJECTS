import requests

url = "https://randomuser.me/api/"

try:
    print("Connecting to the internet to fetch live data...")
    response = requests.get(url, timeout=5)
    
    if response.status_code == 200:
        data = response.json()
        
        user = data['results'][0]
        first_name = user['name']['first']
        last_name = user['name']['last']
        country = user['location']['country']
        
        full_profile = f"Name: {first_name} {last_name} | Country: {country}"
        
        print("\n--- LIVE WEB DATA CAPTURED ---")
        print(full_profile)
        
        # --- NEW AUTOMATION LAYER: SAVE TO HARD DRIVE ---
        # "a" means "append" mode, which adds new text to the end of the file safely
        with open("captured_users.txt", "a") as file:
            file.write(full_profile + "\n")
            
        print("Successfully saved this profile to 'captured_users.txt'!")
        
    else:
        print(f"Server responded with an error code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Network Connection Failed! Error details: {e}")

