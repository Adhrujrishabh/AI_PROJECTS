import os
import requests

url = "https://randomuser.me/api/"
csv_file = "users.csv"

try:
    print("Fetching live web profile data...")
    response = requests.get(url, timeout=5)
    
    if response.status_code == 200:
        data = response.json()
        user = data['results'][0]
        
        # Pull clean data pieces
        first_name = user['name']['first']
        last_name = user['name']['last']
        country = user['location']['country']
        
        # Check if the Excel file already exists. If not, create it with a header row!
        file_exists = os.path.exists(csv_file)
        
        with open(csv_file, "a") as file:
            if not file_exists:
                # Write the column title headers first
                file.write("First Name,Last Name,Country\n")
            
            # Write the user data separated by clear commas
            file.write(f"{first_name},{last_name},{country}\n")
            
        print(f"Flawlessly logged profile into spreadsheet: {csv_file}")
        
except Exception as e:
    print(f"Automation execution failed: {e}")
