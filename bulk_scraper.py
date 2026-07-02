import requests
from bs4 import BeautifulSoup

# We change the link to the main store shelf page where all books are listed
url = "http://books.toscrape.com"

try:
    print("Connecting to the main bookstore catalog...")
    response = requests.get(url, timeout=5)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # --- THE BULK UPGRADE LAYER ---
        # Every book on the webpage is wrapped in a box called a 'product_pod'
        # find_all() sweeps the entire site code and grabs ALL of these boxes at once!
        book_boxes = soup.find_all('article', class_='product_pod')
        
        print(f"\n--- SUCCESS: Found {len(book_boxes)} books on the shelf ---")
        
        # Now we loop through each individual box to extract its unique data
        for box in book_boxes:
            # 1. Grab the title hidden inside the link tag attribute
            title = box.h3.a['title']
            
            # 2. Grab the price text inside the price class
            price = box.find(class_='price_color').text
            
            print(f"📚 Book: {title} | Price: {price}")
            
    else:
        print(f"Could not connect to catalog. Server code: {response.status_code}")
        
except Exception as e:
    print(f"Bulk scraping execution failed: {e}")
