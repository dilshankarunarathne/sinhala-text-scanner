import requests

url = "https://easysinhalaunicode.com/api/convert"


def singlish_to_english(singlish_text: str) -> str:
    data = {"data": singlish_text}
    response = requests.post(url, data=data)

    if response.status_code == 200:
        return response.text
    else:
        return "Error: Unable to convert text"


if __name__ == "__main__":
    print(singlish_to_english("ආයුබෝවන්"))
