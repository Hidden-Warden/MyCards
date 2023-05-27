# Version:
# 0.9.1
###
import os  # Librairie #4
import csv  # .py & Librairie #5
import random  # Librairie #6
import webbrowser  # Librairie #7
import tkinter.font as font  # Librairie #8
import time # Librairie #9
from tkinter import *  # Librairie #10
from settings import *  # .py #11
from language_modules import *  # .py #12

# Start- Discord RPC
try:
    from pypresence import Presence
    cliend_id = "1111771604746244117"
    RPC = Presence(cliend_id)
    RPC.connect()
    RPC.update(
        state = "Learn vocabulary",
        start = int(time.time()),
        large_image = "logo",
        buttons = [{"label": "GitHub", "url": "https://github.com/Hidden-Warden/MyCards"}]
    )
except:
    print("Module pypresence not found so the Discord RPC is not working")
# End- Discord RPC

## ///DEF\\\##
def language(input_language):
    # Choice of the language from the settings:
    global Language
    if True:
        if input_language == "FR":
            Language = FR
        elif input_language == "EN":
            Language = EN
    return Language


def on_click():
    # Refresh the window (delete the previous content)
    canvas.delete('all')


def Randow_Word():
    # Random word from the database
    global NumberOfWord
    global Last_Random
    global Last_Random_List
    if True:
        old_NumberOfWord = NumberOfWord
        NumberOfWord = random.randint(0, len(BaseDeMots)-1)
        if NumberOfWord == old_NumberOfWord:
            NumberOfWord = random.randint(0, len(BaseDeMots))
        if NumberOfWord == 0:
            NumberOfWord = 1
        Last_Random = NumberOfWord
        Last_Random_List.append(NumberOfWord)
        Update(NumberOfWord)
    return NumberOfWord


def Next():
    global NumberOfWord
    global Last_Random
    if True:
        Last_Random = -1
        NumberOfWord += 1
        if NumberOfWord >= len(BaseDeMots):
            NumberOfWord = len(BaseDeMots)-1
        Update(NumberOfWord)
    return NumberOfWord


def Back():
    global NumberOfWord
    global Last_Random
    global Last_Random_List
    if True:
        if Last_Random != -1:
            Last_Random = -1
            NumberOfWord = Last_Random_List[(len(Last_Random_List)-2)]
            # print(Last_Random_List)
        else:
            NumberOfWord -= 1
            if NumberOfWord < 0:
                NumberOfWord = 0

        if NumberOfWord == 0:
            NumberOfWord = 1

        Update(NumberOfWord)
        return NumberOfWord


def GitHubLink():
    if True:
        webbrowser.open(GitHub)


# Keyborad shortcuts
def Randm(x):
    Randow_Word()


def Nxt(x):
    Next()


def Bck(x):
    Back()


def Escp(x):
    root.destroy()


def IMG_related(x):
    ImageRelated()


def IMG_Next(x):
    ImageNext()


def IMG_Back(x):
    ImageBack()


def Update(Numéro):
    # Update the window content with the new word
    print("Card N°", NumberOfWord)
    on_click()
    if True:
        # Lefft side
        canvas.create_text((s_screen_width/first_colonne), (80),
                           text=Rappel_CSV_Title[0], fill="red", font=s_font_family)  # 1
        canvas.create_text((s_screen_width/first_colonne), (160),
                           text=Rappel_CSV_Title[1], fill=s_font_color, font=s_font_family)  # 2
        canvas.create_text((s_screen_width/first_colonne), (240),
                           text=Rappel_CSV_Title[2], fill="green", font=s_font_family)  # 3
        canvas.create_text((s_screen_width/first_colonne), (320),
                           text=Rappel_CSV_Title[3], fill=s_font_color, font=s_font_family)  # 4
        canvas.create_text((s_screen_width/first_colonne), (420),
                           text=Rappel_CSV_Title[4], fill=s_font_color, font=s_font_family)  # 5
        canvas.create_text((s_screen_width/first_colonne), (560),
                           text=Rappel_CSV_Title[5], fill=s_font_color, font=s_font_family)  # 6
        if data_base_free_category == True:  # Free category
            canvas.create_text((s_screen_width/first_colonne), (640),
                               text=Rappel_CSV_Title[6], fill=s_font_color, font=s_font_family)  # 7
        # Right Side
        # 1
        canvas.create_text((s_screen_width/scnd_colonne), (80), text=BaseDeMots[Numéro][1], fill="red", font=s_font_family)
        # 2
        canvas.create_text((s_screen_width/scnd_colonne), (160), text=BaseDeMots[Numéro][2], fill=s_font_color, font=s_font_family)
        # 3
        canvas.create_text((s_screen_width/scnd_colonne), (240), text=BaseDeMots[Numéro][3], fill="green", font=s_font_family)

        btn10 = Button(root, text=(Language[11]+str(NumberOfWord)), activebackground=s_button_color_active, bg=s_button_color_unactive,
                       fg=s_button_texte_color, height=s_button_height, width=s_button_width, borderwidth=0)  # Bouton#// About
        btn10.place(rely=0, relx=0, x=0, y=600, anchor=W)

        #################################################################################################################################
        # 4
        N4_1 = ("")
        N4_2 = ("")
        N4_3 = ("")
        # print("Len",len(BaseDeMots[Numéro][4]))
        if len(BaseDeMots[Numéro][4]) <= 45:
            N4_1 = (BaseDeMots[Numéro][4][:45])
            
        elif len(BaseDeMots[Numéro][4]) <= 90:
            N4_1 = (BaseDeMots[Numéro][4][:45])
            
            N4_2 = (BaseDeMots[Numéro][4][45:90])
            if N4_1[len(N4_1)-1] != " " or N4_1[len(N4_1)-1] != ",":
                if N4_2[0] != " " or N4_2[0] != ",":
                    N4_2 = "-"+N4_2
            
        elif len(BaseDeMots[Numéro][4]) <= 135 and len(BaseDeMots[Numéro][4]) > 90:
            N4_1 = (BaseDeMots[Numéro][4][:45])
            
            N4_2 = (BaseDeMots[Numéro][4][45:90])
            if N4_1[len(N4_1)-1] != " " or N4_1[len(N4_1)-1] != ",":
                if N4_2[0] != " " or N4_2[0] != ",":
                    N4_2 = "-"+N4_2
            
            N4_3 = (BaseDeMots[Numéro][4][90:135])
            if N4_2[len(N4_2)-1] != " " or N4_2[len(N4_2)-1] != ",":
                if N4_3[0] != " " or N4_3[0] != ",":
                    N4_3 = "-"+N4_3
            
        canvas.create_text((s_screen_width/scnd_colonne), (320),
                           text=N4_1, fill=s_font_color, font=s_font_family)  # 4
        canvas.create_text((s_screen_width/scnd_colonne), (350),
                           text=N4_2, fill=s_font_color, font=s_font_family)  # 4
        canvas.create_text((s_screen_width/scnd_colonne), (380),
                           text=N4_3, fill=s_font_color, font=s_font_family)  # 4
        #################################################################################################################################
        # 5
        N5_1 = ("")
        N5_2 = ("")
        N5_3 = ("")
        N5_4 = ("")
        # print("Len",len(BaseDeMots[Numéro][5]))
        if len(BaseDeMots[Numéro][5]) <= 45:
            N5_1 = (BaseDeMots[Numéro][5][:45])
            
        elif len(BaseDeMots[Numéro][5]) <= 90:
            N5_1 = (BaseDeMots[Numéro][5][:45])
            
            N5_2 = (BaseDeMots[Numéro][5][45:90])
            if N5_1[len(N5_1)-1] != " " or N5_1[len(N5_1)-1] != ",":
                if N5_2[0] != " " or N5_2[0] != ",":
                    N5_2 = "-"+N5_2

        elif len(BaseDeMots[Numéro][5]) <= 135 and len(BaseDeMots[Numéro][5]) > 90:
            N5_1 = (BaseDeMots[Numéro][5][:45])

            N5_2 = (BaseDeMots[Numéro][5][45:90])
            if N5_1[len(N5_1)-1] != " " or N5_1[len(N5_1)-1] != ",":
                if N5_2[0] != " " or N5_2[0] != ",":
                    N5_2 = "-"+N5_2

            N5_3 = (BaseDeMots[Numéro][5][90:135])
            if N5_2[len(N5_2)-1] != " " or N5_2[len(N5_2)-1] != ",":
                if N5_3[0] != " " or N5_3[0] != ",":
                    N5_3 = "-"+N5_3

        elif len(BaseDeMots[Numéro][5]) <= 180 and len(BaseDeMots[Numéro][5]) > 135:
            N5_1 = (BaseDeMots[Numéro][5][:45])
            
            N5_2 = (BaseDeMots[Numéro][5][45:90])
            if N5_1[len(N5_1)-1] != " " or N5_1[len(N5_1)-1] != ",":
                if N5_2[0] != " " or N5_2[0] != ",":
                    N5_2 = "-"+N5_2
            
            N5_3 = (BaseDeMots[Numéro][5][90:135])
            if N5_2[len(N5_2)-1] != " " or N5_2[len(N5_2)-1] != ",":
                if N5_3[0] != " " or N5_3[0] != ",":
                    N5_3 = "-"+N5_3
            
            N5_4 = (BaseDeMots[Numéro][5][135:180])
            if N5_3[len(N5_3)-1] != " " or N5_3[len(N5_3)-1] != ",":
                if N5_4[0] != " " or N5_4[0] != ",":
                    N5_4 = "-"+N5_4

        canvas.create_text((s_screen_width/scnd_colonne), (420),
                           text=N5_1, fill=s_font_color, font=s_font_family)  # 5
        canvas.create_text((s_screen_width/scnd_colonne), (450),
                           text=N5_2, fill=s_font_color, font=s_font_family)  # 5
        canvas.create_text((s_screen_width/scnd_colonne), (480),
                           text=N5_3, fill=s_font_color, font=s_font_family)  # 5
        canvas.create_text((s_screen_width/scnd_colonne), (510),
                           text=N5_4, fill=s_font_color, font=s_font_family)  # 5
        #################################################################################################################################
        # 6
        if len(BaseDeMots[Numéro][6]) >= 45:  # 6
            N6_1 = (BaseDeMots[Numéro][6][:45])
            #
            N6_2 = (BaseDeMots[Numéro][6][45:])
            if N6_1[len(N6_1)-1] != " " or N6_1[len(N6_1)-1] != ",":
                if N6_2[0] != " " or N6_2[0] != ",":
                    N6_2 = "-"+N6_2
            canvas.create_text((s_screen_width/scnd_colonne), (560),
                               text=N6_1, fill=s_font_color, font=s_font_family)  # 6
            canvas.create_text((s_screen_width/scnd_colonne), (590),
                               text=N6_2, fill=s_font_color, font=s_font_family)  # 6
        else:  # 6
            # 6
            canvas.create_text((s_screen_width/scnd_colonne), (560), text=BaseDeMots[Numéro][6], fill=s_font_color, font=s_font_family)
        #################################################################################################################################
        # 7 Free column
        if data_base_free_category == True:  # Free category ##7
            if len(BaseDeMots[Numéro][7]) >= 45:  # 7
                N7_1 = (BaseDeMots[Numéro][7][:45])
                #
                N7_2 = (BaseDeMots[Numéro][7][45:])
                if N7_1[len(N7_1)-1] != " " or N7_1[len(N7_1)-1] != ",":
                    if N7_2[0] != " " or N7_2[0] != ",":
                        N7_2 = "-"+N7_2
                canvas.create_text((s_screen_width/scnd_colonne), (640),
                                   text=N7_1, fill=s_font_color, font=s_font_family)  # 7
                canvas.create_text((s_screen_width/scnd_colonne), (670),
                                   text=N7_2, fill=s_font_color, font=s_font_family)  # 7
            else:  # 7
                # 7
                canvas.create_text((s_screen_width/scnd_colonne), (640), text=BaseDeMots[Numéro][7], fill=s_font_color, font=s_font_family)

        #################################################################################################################################
        # Update color of screenshot button if screenshot is found

        if ImageRelated(Only_Return_True_if_there_is_an_image=True) == True:
            btn7 = Button(root, text=Language[8], activebackground=s_button_color_active, bg=s_button_color_unactive_scr, fg=s_button_texte_color_scr,
                          height=s_button_height, width=s_button_width, borderwidth=0, command=ImageRelated)  # Bouton#// Screenshots
            # old y=100 (v0.8.0) -> 150 (v0.9.0) | Change oder of buttons
            btn7.place(rely=0, relx=0, x=0, y=150, anchor=W)
        else:
            btn7 = Button(root, text=Language[8], activebackground=s_button_color_active, bg=s_button_color_unactive, fg=s_button_texte_color,
                          height=s_button_height, width=s_button_width, borderwidth=0, command=ImageRelated)  # Bouton#// Screenshots
            # old y=100 (v0.8.0) -> 150 (v0.9.0) | Change oder of buttons
            btn7.place(rely=0, relx=0, x=0, y=150, anchor=W)

        ###
        if ImageNext(Only_Return_True_if_there_is_an_image=True) == True:
            btn8 = Button(root, text=Language[9], activebackground=s_button_color_active, bg=s_button_color_unactive_scr,
                          fg=s_button_texte_color_scr, height=s_button_height, width=s_button_width, borderwidth=0, command=ImageNext)  # Bouton#// Next Image
            # old y=150 (v0.8.0) -> 100 (v0.9.0) | Change oder of buttons
            btn8.place(rely=0, relx=0, x=0, y=100, anchor=W)
        else:
            btn8 = Button(root, text=Language[9], activebackground=s_button_color_active, bg=s_button_color_unactive, fg=s_button_texte_color,
                          height=s_button_height, width=s_button_width, borderwidth=0, command=ImageNext)  # Bouton#// Next Image
            # old y=150 (v0.8.0) -> 100 (v0.9.0) | Change oder of buttons
            btn8.place(rely=0, relx=0, x=0, y=100, anchor=W)
         ###
        """ #Not working
            if ImageBack(Only_Return_True_if_there_is_an_image=True)==True:
                btn9 = Button(root, text =Language[10], activebackground=s_button_color_active,bg=s_button_color_unactive_scr,fg=s_button_texte_color_scr,height=s_button_height, width=s_button_width,borderwidth = 0,command =ImageBack) #Bouton#// Back Image
                btn9.place(rely=0, relx=0, x=0, y=200,anchor=W)
            else:   
                btn9 = Button(root, text =Language[10], activebackground=s_button_color_active,bg=s_button_color_unactive,fg=s_button_texte_color,height=s_button_height, width=s_button_width,borderwidth = 0,command =ImageBack) #Bouton#// Back Image
                btn9.place(rely=0, relx=0, x=0, y=200,anchor=W)
            """

####

######### Images #########


def ImageRelated(Only_Return_True_if_there_is_an_image=False):
    global ListScrennshot
    global ImageNum
    global Activated
    global Final
    ListScrennshot = []
    ImageNum = 0
    Activated = True  # Was the function called?
    path = Screenshots_Folder_Path
    dir_list = os.listdir(path)
    ##
    for i in range(0, 99):
        try:
            if NumberOfWord <= 9:
                if dir_list[i][2:3] == "-":  # 9
                    ListScrennshot.append(dir_list[i])
            elif NumberOfWord >= 10 and NumberOfWord <= 99:
                if dir_list[i][3:4] == "-":  # 10
                    ListScrennshot.append(dir_list[i])
            elif NumberOfWord >= 100 and NumberOfWord <= 999:
                if dir_list[i][4:5] == "-":  # 100
                    ListScrennshot.append(dir_list[i])
            elif NumberOfWord >= 1000:
                if dir_list[i][5:6] == "-":  # 1000
                    ListScrennshot.append(dir_list[i])
        except:
            pass

    print(ListScrennshot, "Liste des Screenshots")
    Final = []
    Sample = []
    if ListScrennshot != []:
        for u in range(0, 101):
            Sample.append(str("#"+str(NumberOfWord) +
                          "-"+str(u)+screenshot_type))
        print(Sample, "Sample")
        print(ListScrennshot, "Liste des Screenshots")
        for i in range(0, 101):
            for u in range(0, 101):
                try:
                    if Sample[i] == ListScrennshot[u]:
                        Final.append(Sample[i])
                except:
                    pass
    if Final == []:  # No screenshot was found
        print("No screenshot for this word")
        Activated = False
        print(Final, "Final")
    else:  # If there is a screenshot
        if Only_Return_True_if_there_is_an_image == False:
            print('Found a screenshot for this word')
            print(Final, "Final")
            img = PhotoImage(file=path+Final[0])
            if adjust_screenshot_size == True:
                img = img.zoom(2)
                img = img.subsample(3)
            canvas2 = canvas.create_image(
                s_screen_width/3, s_screen_height/3, image=img)
            canvas.create_image()
            Activated = True
            return Activated
        else:
            return True
    # End of ImageRelated()


def ImageNext(Only_Return_True_if_there_is_an_image=False):
    global ImageNum
    global Activated
    if Activated == True:
        path = Screenshots_Folder_Path
        dir_list = os.listdir(path)
        if Only_Return_True_if_there_is_an_image == False:
            if len(Final) > ImageNum+1:
                print('ok Next')
                ImageNum += 1
                img = PhotoImage(file=path+Final[ImageNum])
                if adjust_screenshot_size == True:
                    img = img.zoom(2)
                    img = img.subsample(3)
                canvas2 = canvas.create_image(
                    s_screen_width/3, s_screen_height/3, anchor=CENTER, image=img)
                canvas.create_image()
            else:
                ImageRelated()
        else:
            if len(Final) > ImageNum+1:
                return True
            else:
                return False
    # End of ImageNext()


def ImageBack(Only_Return_True_if_there_is_an_image=False):
    global ImageNum
    global Activated
    if Activated == True:
        path = Screenshots_Folder_Path
        dir_list = os.listdir(path)
        if Only_Return_True_if_there_is_an_image == False:
            if ImageNum > 0:
                print('ok Back')
                ImageNum -= 1
                img = PhotoImage(file=path+Final[ImageNum])
                if adjust_screenshot_size == True:
                    img = img.zoom(2)
                    img = img.subsample(3)
                canvas2 = canvas.create_image(
                    s_screen_width/3, s_screen_height/3, anchor=CENTER, image=img)
                canvas.create_image()
            else:
                ImageRelated()
        else:
            if ImageNum > 0:
                return True

    # End of ImageBack()
######### Images #########

## ///END_DEF\\\##  ##///END_DEF\\\##  ##///END_DEF\\\##


## ///MAIN\\\##  ##///MAIN\\\##  ##///MAIN\\\##
Language = []  # List (will contain the words)
NumberOfWord = 0  # The number of the word in the list (DataBase.csv)
GitHub = "https://github.com/Hidden-Warden/MyCards/blob/main/README.md"  # Link to GitHub ;D
Last_Random = -1
Last_Random_List = []
ListScrennshot = []
###
with open("DataBase.csv", encoding='utf-8', newline='') as csvfile:
    BaseDeMots = list(csv.reader(csvfile, delimiter=s_delimiter))
    Rappel_CSV_Title = BaseDeMots[0]
    Rappel_CSV_Title.pop(0)
    print("Rappel_CSV_Title", Rappel_CSV_Title)
###

# Start- Check if the folder exists and create it if not (event if the path for the screenshots was changed.)
path0 = "Screenshots"
isExist = os.path.exists(path0)
if False == isExist:  # If the folder does not exist, create it
    os.makedirs(path0)
    # If the folder is created successfully, print this message
    print("Directory created successfully (Screenshots)")
else:
    print("Directory already created (Screenshots)")
# End

##
root = Tk()
root.title("MyCards")
root.iconbitmap("MyCards.ico")
root.configure(background=s_background_color)
root.attributes('-fullscreen', full_screen)
###
if s_screen_height > 150 and s_screen_width > 100:
    root.geometry(str(s_screen_width)+"x"+str(s_screen_height))
else:  # Default size
    root.geometry("600x500")
###
if reseizeable_windows == True:
    root.resizable(True, True)
else:
    root.resizable(False, False)
### ////###
language(s_language)  # Call the language function.

### All the buttons shown in the window ###
btn1 = Button(root, text=Language[2], activebackground=s_button_color_active, bg=s_button_color_unactive, fg=s_button_texte_color,
              height=s_button_height, width=s_button_width, borderwidth=0, command=Randow_Word)  # Bouton#// Random
btn1.pack(side='top')
#
btn2 = Button(root, text=Language[3], activebackground=s_button_color_active, bg=s_button_color_unactive,
              fg=s_button_texte_color, height=s_button_height, width=s_button_width, borderwidth=0, command=root.destroy)  # Bouton#// Quit
btn2.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
#
btn3 = Button(root, text=Language[1], activebackground=s_button_color_active, bg=s_button_color_unactive,
              fg=s_button_texte_color, height=s_button_height, width=s_button_width, borderwidth=0, command=Back)  # Bouton#// Back
btn3.pack(side='left')
#
btn4 = Button(root, text=Language[0], activebackground=s_button_color_active, bg=s_button_color_unactive,
              fg=s_button_texte_color, height=s_button_height, width=s_button_width, borderwidth=0, command=Next)  # Bouton#// Next
btn4.pack(side='right')
#
btn5 = Button(root, text=Language[6], activebackground=s_button_color_active, bg=s_button_color_unactive,
              fg=s_button_texte_color, height=s_button_height, width=s_button_width, borderwidth=0, command=GitHubLink)  # Bouton#// About
btn5.pack(side='bottom')

# btn7# (old place) now line 236 and after
# btn8# (old place) now line 23. and after
# btn9# Line 238 and after not working
btn9 = Button(root, text=Language[10], activebackground=s_button_color_active, bg=s_button_color_unactive, fg=s_button_texte_color,
              height=s_button_height, width=s_button_width, borderwidth=0, command=ImageBack)  # Bouton#// Back Image
btn9.place(rely=0, relx=0, x=0, y=200, anchor=W)

if super_mode == True:
    btn6 = Button(root, text=Language[7], activebackground=s_button_color_active, bg=s_button_color_unactive, fg=s_button_texte_color,
                  height=s_button_height, width=s_button_width, borderwidth=0, command=GitHubLink)  # Bouton#// Super Mode
    btn6.pack(anchor=W)

 ### End of the buttons ###

# Font and size of the buttons
f = font.Font(family=s_button_font_family, size=s_button_font_size)
btn1['font'] = f
btn2['font'] = f
btn3['font'] = f
btn4['font'] = f
btn5['font'] = f
if super_mode == True:
    btn6['font'] = f
###
canvas = Canvas(root, width=s_screen_width, height=s_screen_height, bg=s_zone_texte,
                highlightthickness=3, highlightbackground=s_contour_zone_texte)  # Texte
canvas2 = Canvas(root, width=s_screen_width, height=s_screen_height)  # Image
canvas.pack()
###

#### End of the function Update####
root.bind("<space>", Randm)  # Space BAR
root.bind("<Left>", Bck)  # Left Arrow
root.bind("<Right>", Nxt)  # Right Arrow
root.bind("<Escape>", Escp)  # Echap / Escape

root.bind("<b>", IMG_related)  # Image Related ?
root.bind("<n>", IMG_Next)  # Image Next
root.bind("<v>", IMG_Back)  # Image Back

###
Next()  # Show the first card at launch.
root.mainloop()
