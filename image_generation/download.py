import requests
import datetime
import os


def download_image(url, filename):
    filename = filename.replace(" ", "_")
    date = datetime.datetime.now().strftime("%d-%m-%Y")
    folder_path = f'images/{date}/'

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    try:
        response = requests.get(url)
        with open(f'images/{date}/{filename}.png', 'wb') as file:
            file.write(response.content)
    except Exception as e:
        print(e)
