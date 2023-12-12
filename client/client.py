import requests
import os
import hashlib

server_url = 'http://host.docker.internal:9000'

#Get the current working directory
cwd = os.getcwd()
datadir = os.path.join(cwd, 'clientdata')
os.makedirs(datadir, exist_ok=True)
filename = 'test_data.txt'
filepath = os.path.join(datadir, filename)

def download_file():
    response = requests.get(f'{server_url}/download')
    if response.status_code == 200:
        with open(filepath, 'wb') as file:
            file.write(response.content)
    else:
        print('Failed to download the file')
        exit(1)

def download_checksum():
    response = requests.get(f'{server_url}/checksum')
    if response.status_code == 200:
        return response.text
    else:
        print('Failed to download the checksum')
        exit(1)

def calculate_checksum():
    hasher = hashlib.md5()
    with open(filepath, 'rb') as file:
        buffer = file.read()
        hasher.update(buffer)
    return hasher.hexdigest()


def verify_checksum():
    download_file()
    server_checksum = download_checksum()
    calculated_checksum = calculate_checksum()
    if server_checksum == calculated_checksum:
        print('File verification using checksum is successful')
    else:
        print('File verification failed.')


if __name__ == '__main__':
    verify_checksum()

