import requests
import base64
import random
import string
import os
from urllib.parse import urlparse

def git_upload(file_url, bytes=False, extension=".png"):
    git_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    if bytes == True:
        file_response = file_url
        file_extension = extension
        encoded_content = base64.b64encode(file_response).decode('utf-8')
    else:
        file_response = requests.get(file_url)
        file_response.raise_for_status()
        parsed_url = urlparse(file_url)
        base_file_name = os.path.basename(parsed_url.path)
        file_extension = os.path.splitext(base_file_name)[1]
        encoded_content = base64.b64encode(file_response.content).decode('utf-8')

        
    filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16)) + file_extension
    upload_url = f"https://api.github.com/repos/NexusAILab/cdn/contents/cdn/{filename}"
    headers = {
        "Authorization": f"token {git_token}",
    }
    
    data = {
        "message": f"Add new file: {filename}",
        "content": encoded_content,
    }
    upload_response = requests.put(upload_url, headers=headers, json=data)
    upload_response.raise_for_status()
    return upload_response.json()["content"]["download_url"]

def git_file_upload(file_path):
    git_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    with open(file_path, 'rb') as file:
        file_content = file.read()

    base_file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(base_file_name)[1]
    filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16)) + file_extension
    upload_url = f"https://api.github.com/repos/NexusAILab/cdn/contents/cdn/{filename}"
    headers = {
        "Authorization": f"token {git_token}",
    }
    encoded_content = base64.b64encode(file_content).decode('utf-8')
    data = {
        "message": f"Add new file: {filename}",
        "content": encoded_content,
    }
    upload_response = requests.put(upload_url, headers=headers, json=data)
    upload_response.raise_for_status()
    return upload_response.json()["content"]["download_url"]
