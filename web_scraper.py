import requests
from bs4 import BeautifulSoup

# The safe bookstore site built specifically for scraping practice
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

try:
    print("Connecting to the bookstore site to scrape code...")
    response = requests.get(url, timeout=5)
    
    if response.status_code == 200:
        # Feed the website layout text into BeautifulSoup to organize it
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 1. Target the Book Title
        # On this site, the main book title is stored inside an <h1> text tag
        book_title = soup.find('h1').text
        
        # 2. Target the Price
        # The price is stored inside a text block labeled with the class 'price_color'
        book_price = soup.find(class_='price_color').text
        
        print("\n--- DATA SCRAPED SUCCESSFULLY ---")
        print(f"Book Title: {book_title}")
        print(f"Book Price: {book_price}")
        
    else:
        print(f"Could not load page. Server code: {response.status_code}")
        
except Exception as e:
    print(f"Scraping failed due to error: {e}")
