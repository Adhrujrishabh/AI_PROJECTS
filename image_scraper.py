import os
import time
import requests
from bs4 import BeautifulSoup

# The catalog link we are targeting
url = "http://toscrape.com"
image_folder = "downloaded_images"

# --- SYSTEM ASSIST: Create a dedicated local folder for the images ---
if not os.path.exists(image_folder):
    os.makedirs(image_folder)
    print(f"📁 Created a brand new folder: '{image_folder}' on your Mac!")

try:
    print("Connecting to the storefront to scan for images...")
    response = requests.get(url, timeout=5)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Grab all 20 book product cards on the shelf
        book_boxes = soup.find_all('article', class_='product_pod')
        print(f"📊 Scanning complete. Found {len(book_boxes)} product cards to extract.\n")
        
        # Loop through each book card to pull text AND download images
        for position, box in enumerate(book_boxes, start=1):
            title = box.h3.a['title']
            
            # --- THE IMAGE URL EXTRACTION LAYER ---
            # Websites store images in 'img' tags under the 'src' source attribute
            relative_img_url = box.find('img', class_='thumbnail')['src']
            
            # Clean the link path so Python can find it on the global web server
            full_img_url = url + relative_img_url.replace("../", "")
            
            # Clean special characters out of the title to create a safe file name
            safe_title = title.replace(",", "-").replace("/", "-").replace(":", "")
            file_extension = ".jpg"
            image_filename = f"{image_folder}/{position}_{safe_title}{file_extension}"
            
            # --- THE CODES DOWNLOAD PIPELINE ---
            # Python hits the image link directly and downloads the raw image pixels
            img_data = requests.get(full_img_url).content
            
            # Open a blank file on your Mac drive and write the raw pixel bytes into it
            with open(image_filename, 'wb') as img_file:
                img_file.write(img_data)
                
            print(f"📸 Saved Image {position}/20: {title[:30]}...")
            
            # Polite-throttle timer to keep the connection smooth and stable
            time.sleep(0.5)
            
        print(f"\n🎉 SUCCESS: All 20 images downloaded into your '{image_folder}' folder!")
            
    else:
        print(f"Failed to connect. Server code: {response.status_code}")
        
except Exception as e:
    print(f"Image pipeline execution failed: {e}")
