#Global settings
s_language="EN" #Choosable languages: FR(Français), EN(English)
darkmode=False #True(Dark mode), False(Light mode)
full_screen=False #True(Full screen), False(Windowed)
reseizeable_windows=True #True(Resizeable windows), False(Fixed windows)
s_delimiter=";" #Delimiter used in the CSV file (";" / ",")
screenshot_type=".png" #Type of screenshot (".png" / ".jpg")
adjust_screenshot_size=True #True(Adjust screenshot size) to the frame, False(Keep original size)
Screenshots_Folder_Path="Screenshots/" #Path to the Screenshots folder | "Screenshots/" default (if in the same folder as the program) | "C:/Folder1/Screenshots-MyCards/" don't forget the "/" at the end and replace all the "\" by "/" in the path

first_colonne=5 #The higher the value, the more to the left
scnd_colonne=2.2 #The higher the value, the more to the left

#Window & font settings 
s_screen_width=1920
s_screen_height=1080
s_font_family=('Open Sans','20','bold') #font / font size / font style
s_font_color="black" #general color

###Buttons settings###
s_button_color_unactive="#525E70" #Couleur du BOUTON quand non cliqué #Default: #00CEFF CYAN
s_button_color_active="#FFFFFF" #Couleur du BOUTON quand cliqué #Default: #E300FF VIOLET
s_button_texte_color="#FFFFFF" #Couleur du texte BOUTON

s_button_texte_color_scr="#FFFFFF" #Couleur du texte BOUTON screenshot if found / Next if found / And back if found
s_button_color_unactive_scr="#6D4AFF" #Couleur du BOUTON quand non cliqué.

s_button_font_size=12 #Taille texte police BOUTON
s_button_font_family='Open Sans' #Type de police BOUTON
s_button_height=2 #Hauteur du bouton
s_button_width=12 #Largeur du bouton

#In test#
data_base_free_category=False #True(Shown), False(Hidden)
super_mode=False #True(Shown), False(Hidden) #Not yet implemented

###
if darkmode==True:
    s_background_color="#081b36"
    s_text_color="#FFFFFF"
    s_zone_texte="#3F4E63"  
    s_contour_zone_texte="#FFFFFF"
else:
    s_background_color="#081b36"
    s_text_color="#FFFFFF"
    s_zone_texte="#E5E5E5" 
    s_contour_zone_texte="#FFFFFF"