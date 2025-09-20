import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url):
    """Extract filename from URL or generate one."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:  
        filename = "downloaded_image.jpg"
    return filename

def is_duplicate(filepath, content):
    """Check if the file already exists and matches content (by hash)."""
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            existing_hash = hashlib.md5(f.read()).hexdigest()
        new_hash = hashlib.md5(content).hexdigest()
        return existing_hash == new_hash
    return False

def fetch_image(url):
    """Fetch and save image from a given URL."""
    try:
        
        os.makedirs("Fetched_Images", exist_ok=True)

        
        headers = {"User-Agent": "UbuntuFetcher/1.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise exception for bad responses

        
        if "image" not in response.headers.get("Content-Type", ""):
            print(f"✗ The URL does not point to an image: {url}")
            return

        filename = get_filename_from_url(url)
        filepath = os.path.join("Fetched_Images", filename)

        
        if is_duplicate(filepath, response.content):
            print(f"⚠ Duplicate skipped: {filename}")
            return

        
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = input("Please enter one or more image URLs (comma separated): ").split(",")

    for url in [u.strip() for u in urls if u.strip()]:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
