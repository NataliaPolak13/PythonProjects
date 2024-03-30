import calendar
import os

# Zmienna przechowująca lokalizację w której znajduję się skrypt
script_path = os.path.normpath(os.path.join(os.path.dirname(__file__)))

# Zmienna przechowująca lokalizację folderu, w którym znajdują się zdjęcia, za pomocą funkcji join dodajemy nazwę folderu do ścieżki
photos_path = os.path.join(script_path, "photos")

# Tworzymy foldery i podfoldery z nazwami miesięcy - mamy podany konkretny zakres lat
for year in range(2020, 2023):
    folder_year = str(year)
    if not os.path.exists(os.path.join(photos_path, folder_year)):
        os.mkdir(os.path.join(photos_path, folder_year))
        for month in range(1, 13):
            folder_month = os.path.join(photos_path, folder_year, calendar.month_name[month])
            if not os.path.exists(os.path.join(photos_path, folder_month)):
                os.makedirs(folder_month)

# Przenosimy zdjęcia w formacie IMG_dzień_miesiąc_rok.png do odpowiedniego folderu
for filename in os.listdir(photos_path):
    if filename.endswith(".png"):
        file_parts = filename.split('_')
        print(file_parts)
        if len(file_parts) == 4:
            year = file_parts[3].split('.')[0]
            month_number = int(file_parts[2])
            month_name = calendar.month_name[month_number]
            destination_folder = os.path.join(photos_path, year, month_name)
            destination_path = os.path.join(destination_folder, filename)
            os.rename(os.path.join(photos_path, filename), destination_path)