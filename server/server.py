from flask import Flask, send_from_directory
import os
import random
import hashlib
import sys

app = Flask(__name__)

#Set the mount directory of the server's docker volume
datadir = "/serverdata"
# Ensure that the data directory exists
os.makedirs(datadir, exist_ok=True)

filename = "test_data.txt"
filepath = os.path.join(datadir, filename)

# Function to generate a 1KB file with random data
def generate_file():
    with open(filepath, 'w') as file:
        file.write(''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=1024)))
    print("File generated")

# Function to calculate file checksum
def calculate_checksum():
    hasher = hashlib.md5()
    with open(filepath, 'rb') as file:
        buffer = file.read()
        hasher.update(buffer)
    return hasher.hexdigest()


# Endpoint to download the file
@app.route('/download')
def download_file():
    response = send_from_directory(datadir, filename, as_attachment=True)
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    return response

# Endpoint to get the checksum
@app.route('/checksum')
def get_checksum():
    return checksum

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9000
    generate_file()
    checksum = calculate_checksum()
    app.run(host='0.0.0.0', port=port)
