# MyCards
### -What is MyCards?
   -MyCards is an app made to store your own vocabulary words.

### -What does it features?
##### -A Light mode:
![LightMode](https://user-images.githubusercontent.com/70717127/166895375-186bdaa9-780f-4a6f-92f6-8ac3e7dbd331.png)

##### -A Dark mode:
![DarkMode](https://user-images.githubusercontent.com/70717127/166895388-a46eaa57-f200-4a52-8fed-d1217b223841.png)

### -You are free to personalise it!
In the "settings.py" file, you can:
- Change the language. (s_language=)
- Activate/de-activate the dark mode. (darkmode=)
- Enable the full screen mode. (full_screen=)
- You can move both columns. (first_colone= / scnd_colone=)
- You can change the delimiter for the CSV file. (s_delimiter=)
And more...

### -How can I add my own Cards ?
To do so, open the "DataBase.csv" file, and add your own list of words, by default the delimiter is ";" but you change it in the settings('settings.py'), line 6 (s_delimiter).
You can modify it as your wish.

- Line 1 ; 2 ; 3 ; 6 ; 7 up to 42 characters (without moving the columns)
- Line 4 ; 5 up to 135 characters (without moving the columns)

#### -Without moving the columns
![maximum of character(1)](https://user-images.githubusercontent.com/70717127/166919710-5814b19c-4213-4942-8ae9-45e35cf862d2.png)
#### -First columns moved to the left. Change "first_colone=5" to "first_colone=7"
![maximum of character(2)](https://user-images.githubusercontent.com/70717127/166919714-679dc889-2473-4e02-9083-7436a784ad72.png)

#### -Example taken:
    - This sentence is composed of 42 characters 
    
    - ##############################################This sentence is composed of 135 characters######################################12345678

### -How to update MyCards?
Download the new released on GitHub, extract the.zip file and transfert/copy the following files to the new folder ('settings.py' & 'DataBase.csv').
   - If one of these files comes to change, I will notify it in the changelog so you can manually put your settings back on the new version.


#### -Font used in the screenshot is from Google Fonts
https://fonts.google.com/specimen/Open+Sans

If you see my project, and try it out, I would love to have your feedback ! :D
And please don't hesitate to correct me!

