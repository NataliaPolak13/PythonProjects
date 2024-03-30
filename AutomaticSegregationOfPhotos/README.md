# Automatic segregation of photos

This script is created to manage images, including downloading, organizing, and moving them into folders based on the year and month they were created.

## Functionalities

1. **Downloading Image**: The script starts by downloading an image from the internet using the `requests` library. The image URL is defined in the `image_url` variable, and the downloaded data is stored in the `img_data` variable.

2. **Creating Folder Structure**: The script then creates a folder structure in the `photos` directory, representing yearly and monthly subdirectories from the year 2020 to 2022. Using the `calendar` module, month names are automatically generated.

3. **Organizing Images**: The script iterates through all files in the `photos` directory and moves images according to their names into the respective yearly and monthly folders. Images with filenames in the format `IMG_day_month_year.png` are moved to folders corresponding to the given year and month.

4. **Displaying Folder Division**: Finally, the script displays the division of folders by year and months for each year.

Through this process, images are organized and easily accessible by their creation date.
## Script Overview
- **Setting Paths**: The script sets up paths for the script location, photo directory, and a sample photo.
- **Downloading Images**: It downloads an image from the specified URL using the `requests` library.
- **Creating Yearly and Monthly Folders**: The script creates folders for each year from 2020 to 2022, and subfolders for each month within those years.
- **Organizing Images**: It moves images with filenames in the format `IMG_day_month_year.png` to the respective year and month folders.

Author Natalia Polak
