import requests


def singlish_to_english(singlish_text: str) -> str:
    url = "https://easysinhalaunicode.com/api/convert"
    data = {"data": singlish_text}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        return response.text
    else: # TODO bug 406
        print(response.status_code)
        return "Error: Unable to convert text"


if __name__ == "__main__":
    print(singlish_to_english("aayuboewan"))
