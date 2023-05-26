<p align="center">
  <h3 align="center">MyCards</h3>

  <p align="center">
    MyCards is an app made to store your own vocabulary words.
  </p>
  <p align="center">

   <div class="badges" align="center">
        <img alt="Issues" src="https://img.shields.io/github/issues/Hidden-Warden/MyCards">
        <img alt="License" src="https://img.shields.io/github/license/Hidden-Warden/MyCards">
    </div>
</p>

## Built With
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## What does it features?
|Light Mode|Dark Mode|
|--|--|
|![LightMode](https://user-images.githubusercontent.com/70717127/166895375-186bdaa9-780f-4a6f-92f6-8ac3e7dbd331.png)|![DarkMode](https://user-images.githubusercontent.com/70717127/166895388-a46eaa57-f200-4a52-8fed-d1217b223841.png)|

## You are free to personalise it!
In the `settings.py` file, you can:
* Change the language. (s_language=)
* Activate/de-activate the dark mode. (darkmode=)
* Enable the full screen mode. (full_screen=)
* You can move both columns. (first_colone= / scnd_colone=)
* You can change the delimiter for the CSV file. (s_delimiter=)
And more...

## How can I add my own Cards ?
To do so, open the `DataBase.csv` file, and add your own list of words, by default the delimiter is `;` but you change it in the settings (`settings.py`), line 6 (s_delimiter).
You can modify it as your wish.

* Line 1 ; 2 ; 3 ; 6 ; 7 up to 42 characters (without moving the columns)
* Line 4 ; 5 up to 135 characters (without moving the columns)

### Without moving the columns
![maximum of character(1)](https://user-images.githubusercontent.com/70717127/166919710-5814b19c-4213-4942-8ae9-45e35cf862d2.png)
### First columns moved to the left. Change "first_colone=5" to "first_colone=7"
![maximum of character(2)](https://user-images.githubusercontent.com/70717127/166919714-679dc889-2473-4e02-9083-7436a784ad72.png)

### Example taken:
    - This sentence is composed of 42 characters 
    
    - ##############################################This sentence is composed of 135 characters######################################12345678

## How to update MyCards?
Download the new released on GitHub, extract the.zip file and transfert/copy the following files to the new folder (`settings.py` & `DataBase.csv`).
* If one of these files comes to change, I will notify it in the changelog so you can manually put your settings back on the new version.


### Font used in the screenshot is from Google Fonts
https://fonts.google.com/specimen/Open+Sans

### How to add your own screenshot and how it is working ?

* Go in the folder called "Screenshots" I you don't see it, just launch the program once.
How to name your file. It's simple. **Let's take an example:**
For my first card (word) I want to put an image with a flower on it. So because it is my first card, I will call it
* `#1-1.png` 
* `#` <=  For the program to understand that this is a screenshot that you want to use
* `1` <= First card
* `-1 `<= The first screenshot for that word, but your not limited to one image. Ex: `#1-5.png` 

I will also soon release a new version with some test image for you to see.

There also new keyboard shortcut, made for using the screenshot option.

* `B` Show the screenshot related to the word. It will show if it exist
* `N`Go to the next screenshot (Will not work if there's only one.
* `V` Go back 

### Why are my screenshots & images pixelated ?
* It's because you activated the following setting: `adjust_screenshot_size`. Unfortunately, when activated, to rezeise the image, I use two function, on to zoom in and another to zoom out, and by doing this the image become pixelated. I haven't found any other way to match the picture to the canva.
If you see my project, and try it out, I would love to have your feedback ! :D
And please don't hesitate to correct me!

## Can I use MyCards on my iPhone ?
* Yes it's now possible with this [MyCards 1.0](https://www.icloud.com/shortcuts/f7fdae15eb864ef3818e640538cfb5db) & [MyCards 1.0 Get](https://www.icloud.com/shortcuts/f29af42af8ea4520b6ae83cccc4fb729) with this one (Get), you can choose which Card you want to see.
Select the file location & edit the categories names.

I can't sadly made the same for Android sorry. 

## License

Distributed under the Mozilla Public License 2.0 License. See [LICENSE](https://github.com/Hidden-Warden/Marmit65/blob/main/LICENSE) for more information.

## Image of presentation
From Pixabay:
* https://pixabay.com/fr/illustrations/oui-cartes-spirale-beaucoup-68480/
* https://pixabay.com/fr/photos/japon-hiver-quatre-saisons-neige-3460431/

## Authors

* **[Hidden-Warden](https://github.com/Hidden-Warden)** - *French student in high school*
