import urllib.request
import re
import os
import sys

# Support reading Google Drive Folder ID or URL from environment variables
raw_folder_input = os.environ.get("GDRIVE_FOLDER_ID") or os.environ.get("GDRIVE_FOLDER_URL") or "1mH-m8PJ9obzBU5WiMb3iPoNUWB2tVuSr"

# Extract Folder ID if full URL was provided
url_match = re.search(r'folders/([a-zA-Z0-9_-]{25,50})', raw_folder_input)
FOLDER_ID = url_match.group(1) if url_match else raw_folder_input.strip()

PUBLIC_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public")

# Default fallback file IDs mapping (known files in folder)
DEFAULT_FILE_IDS = {
    '1.jpg': '1YuDEgn0fegw2I0qlh2wFP9myQPZtYGkq',
    '2.jpg': '1tCa2mLNCjDglzq5dR3kVkigPCwy1a_Re',
    '3.jpg': '1GQmY-A_zObrFaLLZNeSv0cdcgJMxaY3E',
    '4.jpg': '1DZioMj5tAN3BBpjjOGLAYU30Ppa-UNnj',
    '5.jpg': '1wBi84h6lpO875JpEP2lTxSUZKO_VqV0Z',
    '6.jpg': '1dxsKFYx2QFTt9mpOEoFLfrI_zWqOsOxX',
    '7.jpg': '1j8ro34Sff5j7ZkkImiiT4oRZPHl3IyBg'
}

def get_folder_metadata(folder_id):
    file_map = {}
    urls_to_try = [
        f"https://drive.google.com/drive/folders/{folder_id}?usp=sharing",
        f"https://drive.google.com/drive/folders/{folder_id}"
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    for url in urls_to_try:
        try:
            print(f"Trying to fetch folder metadata from: {url}")
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                matches = re.finditer(r'([a-zA-Z0-9_-]{33}).{1,100}?([1-7]\.jpg)', html)
                for m in matches:
                    file_id, filename = m.groups()
                    if filename not in file_map:
                        file_map[filename] = file_id
                if len(file_map) > 0:
                    print(f"Successfully scraped {len(file_map)} files from Google Drive folder.")
                    return file_map
        except Exception as e:
            print(f"Notice: Fetching {url} returned: {e}")
            
    print("Folder metadata scraping failed or blocked by Google Drive. Using default direct file ID fallback map.")
    return DEFAULT_FILE_IDS

def sync_images():
    os.makedirs(PUBLIC_DIR, exist_ok=True)
    file_map = get_folder_metadata(FOLDER_ID)

    for i in range(1, 8):
        filename = f"{i}.jpg"
        file_id = file_map.get(filename) or DEFAULT_FILE_IDS.get(filename)
        save_path = os.path.join(PUBLIC_DIR, filename)

        if not file_id:
            print(f"Warning: No file ID found for {filename}, skipping.")
            continue

        download_urls = [
            f"https://drive.google.com/uc?export=download&id={file_id}",
            f"https://lh3.googleusercontent.com/d/{file_id}"
        ]

        downloaded = False
        for durl in download_urls:
            try:
                req = urllib.request.Request(durl, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=15) as resp:
                    content = resp.read()
                    if len(content) > 1000: # Ensure valid image size
                        with open(save_path, 'wb') as f:
                            f.write(content)
                        print(f"Successfully saved {filename} ({len(content)} bytes) via {durl}")
                        downloaded = True
                        break
            except Exception as e:
                print(f"Download attempt for {filename} from {durl} failed: {e}")

        if not downloaded:
            if os.path.exists(save_path):
                print(f"Warning: Could not download {filename} from GDrive, keeping existing local {filename}.")
            else:
                print(f"Error: {filename} missing and download failed.")

if __name__ == "__main__":
    try:
        sync_images()
    except Exception as overall_e:
        print(f"Warning: Image sync encountered an issue ({overall_e}). Proceeding with build using cached images.")
