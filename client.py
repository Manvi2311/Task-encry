import requests

import base64
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 16-byte AES key
iv = get_random_bytes(16)   # 16-byte IV

# base64 encode kar rahe hain
key_b64 = base64.b64encode(key).decode()
iv_b64 = base64.b64encode(iv).decode()

# Send to server
response = requests.post(
    "https://manvi:5000/upload-key",
    json={"key": key_b64, "iv": iv_b64},
    verify=False  # WARNING: sirf testing ke liye! Production mein verify=True hona chahiye.
)

print(response.json())
