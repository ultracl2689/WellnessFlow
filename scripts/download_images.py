import urllib.request
import urllib.parse
import json
import re
import os
import sys

# Read configuration from environment variables
raw_folder_input = os.environ.get("GDRIVE_FOLDER_ID") or os.environ.get("GDRIVE_FOLDER_URL") or "1mH-m8PJ9obzBU5WiMb3iPoNUWB2tVuSr"
API_KEY = os.environ.get("GDRIVE_API_KEY")

# Extract Folder ID if full URL was provided
url_match = re.search(r'folders/([a-zA-Z0-9_-]{25,50})', raw_folder_input)
FOLDER_ID = url_match.group(1) if url_match else raw_folder_input.strip()

PUBLIC_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public")

DEFAULT_FILE_IDS = {
    '1.jpg': '1YuDEgn0fegw2I0qlh2wFP9myQPZtYGkq',
    '2.jpg': '1tCa2mLNCjDglzq5dR3kVkigPCwy1a_Re',
    '3.jpg': '1GQmY-A_zObrFaLLZNeSv0cdcgJMxaY3E',
    '4.jpg': '1DZioMj5tAN3BBpjjOGLAYU30Ppa-UNnj',
    '5.jpg': '1wBi84h6lpO875JpEP2lTxSUZKO_VqV0Z',
    '6.jpg': '1dxsKFYx2QFTt9mpOEoFLfrI_zWqOsOxX',
    '7.jpg': '1j8ro34Sff5j7ZkkImiiT4oRZPHl3IyBg'
}

def get_folder_files_via_api(folder_id, api_key):
    """Use official Google Drive API v3 to list folder files cleanly."""
    query = f"'{folder_id}' in parents and trashed = false"
    url = f"https://www.googleapis.com/drive/v3/files?q={urllib.parse.quote(query)}&fields=files(id,name)&key={api_key}"
    
    print(f"Fetching file list using official Google Drive API v3...")
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            file_map = {}
            for item in data.get('files', []):
                filename = item.get('name')
                file_id = item.get('id')
                if filename and file_id:
                    file_map[filename] = file_id
            print(f"Google Drive API returned {len(file_map)} files: {file_map}")
            return file_map
    except Exception as e:
        print(f"Google Drive API call failed: {e}")
        return None

def get_folder_files_via_scraping(folder_id):
    """Attempt web scraping (works locally, may be blocked in CI)."""
    file_map = {}
    url = f"https://drive.google.com/drive/folders/{folder_id}?usp=sharing"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            matches = re.finditer(r'([a-zA-Z0-9_-]{33}).{1,100}?([1-7]\.jpg)', html)
            for m in matches:
                file_id, filename = m.groups()
                if filename not in file_map:
                    file_map[filename] = file_id
            if len(file_map) > 0:
                print(f"Scraped {len(file_map)} files from Google Drive folder page.")
                return file_map
    except Exception as e:
        print(f"Folder scraping failed: {e}")
    return None

def sync_images():
    os.makedirs(PUBLIC_DIR, exist_ok=True)
    file_map = None

    if API_KEY:
        file_map = get_folder_files_via_api(FOLDER_ID, API_KEY)
    
    if not file_map:
        file_map = get_folder_files_via_scraping(FOLDER_ID)
        
    if not file_map:
        print("Using default file ID fallback mapping.")
        file_map = DEFAULT_FILE_IDS

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
                    if len(content) > 1000:
                        with open(save_path, 'wb') as f:
                            f.write(content)
                        print(f"Successfully saved {filename} ({len(content)} bytes)")
                        downloaded = True
                        break
            except Exception as e:
                print(f"Download attempt for {filename} failed: {e}")

        if not downloaded and not os.path.exists(save_path):
            print(f"Error: {filename} missing and download failed.")

if __name__ == "__main__":
    try:
        sync_images()
    except Exception as e:
        print(f"Warning: Image sync failed ({e}). Proceeding with existing local assets.")
