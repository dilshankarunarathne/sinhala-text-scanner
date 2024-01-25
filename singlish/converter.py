import requests


def singlish_to_english(singlish_text: str) -> str:
    url = "https://easysinhalaunicode.com/api/convert"
    data = {"data": singlish_text}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        print("Singlish translation: ", response.text)
        return response.text
    else:
        print(response.text)
        return "Error: Unable to convert text"


if __name__ == "__main__":
    print(singlish_to_english("aayuboewan"))
