import os
import requests
import time

url = "https://randomuser.me/api/"
csv_file = "bulk_users.csv"

# --- THE AUTOMATION LAYER: RUN THIS FOR LOOP 5 TIMES ---
for i in range(5):
    try:
        # i starts at 0, so adding 1 makes it print Profile 1, 2, 3...
        print(f"Automatically fetching profile #{i + 1} from the web...")
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            user = data['results'][0]
            
            first_name = user['name']['first']
            last_name = user['name']['last']
            country = user['location']['country']
            
            file_exists = os.path.exists(csv_file)
            
            with open(csv_file, "a") as file:
                if not file_exists:
                    file.write("First Name,Last Name,Country\n")
                    file_exists = True # Changes to True so headers don't repeat!
                
                file.write(f"{first_name},{last_name},{country}\n")
            
            # Safety Check: Pause for 1 second so we don't crash the server
            time.sleep(1)
            
        else:
            print(f"Failed on run #{i + 1}. Code: {response.status_code}")
            
    except Exception as e:
        print(f"Error on run #{i + 1}: {e}")

print("\n🎉 BULK AUTOMATION RUN COMPLETE! Check your left sidebar for bulk_users.csv!")
