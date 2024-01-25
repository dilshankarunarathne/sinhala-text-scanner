import requests


def singlish_to_english(singlish_text: str) -> str:
    url = "https://easysinhalaunicode.com/api/convert"
    data = {"data": singlish_text}
    response = requests.post(url, data=data)

    if response.status_code == 200:
        return response.text
    else:
        return "Error: Unable to convert text"
