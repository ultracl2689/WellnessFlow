import urllib.request
import re
import os
import sys

# Support reading Google Drive Folder ID or URL from environment variables
raw_folder_input = os.environ.get("GDRIVE_FOLDER_ID") or os.environ.get("GDRIVE_FOLDER_URL") or "1mH-m8PJ9obzBU5WiMb3iPoNUWB2tVuSr"

# Extract Folder ID if full URL was provided
url_match = re.search(r'folders/([a-zA-Z0-9_-]{25,50})', raw_folder_input)
FOLDER_ID = url_match.group(1) if url_match else raw_folder_input

PUBLIC_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public")

def sync_images():
    url = f"https://drive.google.com/drive/folders/{FOLDER_ID}"
    print(f"Fetching folder metadata from {url} (Folder ID: {FOLDER_ID})...")
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')

    # Find file ID and filename mappings
    matches = re.finditer(r'([a-zA-Z0-9_-]{33}).{1,100}?([1-7]\.jpg)', html)
    file_map = {}
    for m in matches:
        file_id, filename = m.groups()
        if filename not in file_map:
            file_map[filename] = file_id

    print(f"Found {len(file_map)} target files in Google Drive folder: {file_map}")

    os.makedirs(PUBLIC_DIR, exist_ok=True)

    for i in range(1, 8):
        filename = f"{i}.jpg"
        file_id = file_map.get(filename)
        if not file_id:
            print(f"Warning: {filename} not found in folder metadata, skipping.")
            continue

        download_url = f"https://lh3.googleusercontent.com/d/{file_id}"
        save_path = os.path.join(PUBLIC_DIR, filename)
        print(f"Downloading {filename} (ID: {file_id}) -> {save_path}...")
        
        req = urllib.request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            content = resp.read()
            with open(save_path, 'wb') as f:
                f.write(content)
            print(f"Successfully saved {filename} ({len(content)} bytes)")

if __name__ == "__main__":
    sync_images()
