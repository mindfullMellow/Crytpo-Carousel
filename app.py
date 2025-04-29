import requests

def download_crypto_image(coin_id, save_as="crypto.png"):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        image_url = data["image"]["large"]
        image_data = requests.get(image_url).content
        with open(save_as, "wb") as f:
            f.write(image_data)
        print(f"{coin_id.capitalize()} logo saved as {save_as}")
    else:
        print("Coin not found or API error.")

# Example usage
download_crypto_image("dogwifcoin", "dogwifcoin.png")
