import requests
import os
import shutil
import random

# Zmienna przechowująca lokalizację w której znajduję się skrypt
script_path = os.path.normpath(os.path.join(os.path.dirname(__file__)))

# Zmienna przechowująca lokalizację folderu, w którym znajdują się zdjęcia, za pomocą funkcji join dodajemy nazwę folderu do ścieżki
photos_path = os.path.join(script_path, "photos")

# Zmienna przechowująca lokalizacje pliku z przykładowym zdjęciem
cat_path = os.path.join(photos_path, 'cat.png')

# Korzystam z obrazu ze strony https://pixabay.com/pl/
image_url = "https://cdn.pixabay.com/photo/2016/03/23/04/57/cat-1274094_1280.png"

# Pobranie zdjęcia z wykorzystaniem biblioteki requests
img_data = requests.get(image_url).content

# Sprawdzenie czy folder na zdjęcia znajduję się na dysku, jeżeli nie zostanie stworzony
if os.path.exists(photos_path) is False:
    os.mkdir(photos_path)