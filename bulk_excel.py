import os
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com"
csv_file = "bulk_books.csv"

try:
    print("Connecting to the bookstore storefront...")
    response = requests.get(url, timeout=5)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        book_boxes = soup.find_all('article', class_='product_pod')
        
        # Check if the spreadsheet already exists. If not, we make it fresh!
        file_exists = os.path.exists(csv_file)
        
        with open(csv_file, "a") as file:
            if not file_exists:
                # Write our Excel column headers first
                file.write("Book Title,Book Price\n")
            
            # Loop through each book card, extract data, and pipe it directly to Excel
            for box in book_boxes:
                title = box.h3.a['title']
                price = box.find(class_='price_color').text
                
                # Clean commas out of book titles so they don't break our spreadsheet layout columns!
                clean_title = title.replace(",", "-")
                
                # Write the row into our spreadsheet separated by a clear comma
                file.write(f"{clean_title},{price}\n")
                
        print(f"\n🎉 EXCEL AUTOMATION SUCCESS: 20 books saved into '{csv_file}'!")
            
    else:
        print(f"Could not connect to catalog. Server code: {response.status_code}")
        
except Exception as e:
    print(f"Bulk spreadsheet automation failed: {e}")
