#Version:
#0.2.3
###
import os ###  Librairie
import csv ### Docs /  Librairie
import random ###  Librairie
import webbrowser    ### Librairie
import tkinter.font as font
from tkinter import * ### Librairie
from settings import * ### Docs
from language_modules import * ### Docs
###
Language=[] #List (will contain the words)
NumberOfWord=-1 #The number of the word in the list (DataBase.csv)
GitHub="https://github.com/Hidden-Warden/MyCards/blob/main/README.md" #Link to GitHub ;D
Last_Random=-1
Last_Random_List=[]
###
with open("DataBase.csv", encoding='utf-8', newline='') as csvfile:
    BaseDeMots=list(csv.reader(csvfile,delimiter=s_delimiter)) 
    Rappel_CSV_Title=BaseDeMots[0]
    Rappel_CSV_Title.pop(0)
    print("Rappel_CSV_Title",Rappel_CSV_Title)
    BaseDeMots.pop(0) # Delete the first line in BaseDeMots
###
def language(input_language):
    ##Choice of the language from the settings:
    global Language
    if True:
        if input_language=="FR":
            Language=FR
        elif input_language=="EN":
            Language=EN
    return Language
###
def on_click():
    # Refresh the window (delete the previous content)
    canvas.delete('all')
###
def Randow_Word():
    #Random word from the database
    global NumberOfWord
    global Last_Random
    global Last_Random_List
    if True:
        old_NumberOfWord=NumberOfWord
        NumberOfWord=random.randint(0,len(BaseDeMots)-1)
        if NumberOfWord==old_NumberOfWord:
            NumberOfWord=random.randint(0,len(BaseDeMots)-1)
        Update(NumberOfWord)
        Last_Random=NumberOfWord
        Last_Random_List.append(NumberOfWord)
    return NumberOfWord
###
def Next():
    global NumberOfWord
    global Last_Random
    if True:
        Last_Random=-1
        NumberOfWord+=1
        if NumberOfWord>=len(BaseDeMots):
            NumberOfWord=len(BaseDeMots)-1
        Update(NumberOfWord)
    return NumberOfWord
###
def Back():
    global NumberOfWord
    global Last_Random
    global Last_Random_List
    if True:
        if Last_Random!=-1:
            Last_Random=-1
            NumberOfWord=Last_Random_List[(len(Last_Random_List)-2)]
            #print(Last_Random_List)
            Update(NumberOfWord)
        else:
            NumberOfWord-=1
            if NumberOfWord<0:
                NumberOfWord=0
            Update(NumberOfWord)
        return NumberOfWord

def GitHubLink():
    if True:
        webbrowser.open(GitHub)
###

root = Tk()
root.title("MyCards")
root.iconbitmap("MyCards.ico")
root.configure(background=s_background_color)
root.attributes('-fullscreen', full_screen)
###
if s_screen_height > 150 and s_screen_width > 100:
    root.geometry(str(s_screen_width)+"x"+str(s_screen_height))
else: #Default size
    root.geometry("600x500")
###
if reseizeable_windows==True:
    root.resizable(True,True)
else:
    root.resizable(False,False)
###////###
language(s_language) #Call the language function.

### All the buttons shown in the window ### 
btn1 = Button(root, text =Language[2], activebackground=s_button_color_active,bg=s_button_color_unactive,fg=s_button_texte_color,height=s_button_height, width=s_button_width,borderwidth = 0,command =Randow_Word) #Bouton#// Random
btn1.pack(side = 'top')
    #
btn2 = Button(root, text =Language[3], activebackground=s_button_color_active,bg=s_button_color_unactive,fg=s_button_texte_color,height=s_button_height, width=s_button_width,borderwidth = 0,command = root.destroy) #Bouton#// Quit
btn2.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
    #
btn3 = Button(root, text =Language[1], activebackground=s_button_color_active,bg=s_button_color_unactive,fg=s_button_texte_color,height=s_button_height, width=s_button_width,borderwidth = 0,command =Back) #Bouton#// Back
btn3.pack(side = 'left')
    #
btn4 = Button(root, text =Language[0], activebackground=s_button_color_active,bg=s_button_color_unactive,fg=s_button_texte_color,height=s_button_height, width=s_button_width,borderwidth = 0,command =Next) #Bouton#// Next
btn4.pack(side = 'right')
    #
btn5 = Button(root, text =Language[6], activebackground=s_button_color_active,bg=s_button_color_unactive,fg=s_button_texte_color,height=s_button_height, width=s_button_width,borderwidth = 0,command =GitHubLink) #Bouton#// About
btn5.pack(side='bottom')

if super_mode==True:
    btn6 = Button(root, text =Language[7], activebackground=s_button_color_active,bg=s_button_color_unactive,fg=s_button_texte_color,height=s_button_height, width=s_button_width,borderwidth = 0,command =GitHubLink) #Bouton#// Super Mode
    btn6.pack(anchor=W)
 ### End of the buttons ###

# Font and size of the buttons
f = font.Font(family=s_button_font_family, size=s_button_font_size)
btn1['font'] = f
btn2['font'] = f
btn3['font'] = f
btn4['font'] = f
btn5['font'] = f
if super_mode==True:
    btn6['font'] = f
###
canvas= Canvas(root, width=s_screen_width, height=s_screen_height, bg=s_zone_texte,highlightthickness=3, highlightbackground=s_contour_zone_texte)  
canvas.pack()

def Update(Numéro): 
    # Update the window content with the new word
    print("N.O.F",NumberOfWord)
    on_click()
    if True:
            canvas.create_text((s_screen_width/first_colonne), (80), text=Rappel_CSV_Title[0],fill="red", font=s_font_family) ##1 
            canvas.create_text((s_screen_width/first_colonne), (160), text=Rappel_CSV_Title[1],fill=s_font_color, font=s_font_family) ##2
            canvas.create_text((s_screen_width/first_colonne), (240), text=Rappel_CSV_Title[2],fill="green", font=s_font_family) ##3
            canvas.create_text((s_screen_width/first_colonne), (320), text=Rappel_CSV_Title[3],fill=s_font_color, font=s_font_family) ##4
            canvas.create_text((s_screen_width/first_colonne), (420), text=Rappel_CSV_Title[4],fill=s_font_color, font=s_font_family) ##5
            canvas.create_text((s_screen_width/first_colonne), (560), text=Rappel_CSV_Title[5],fill=s_font_color, font=s_font_family) ##6
            if data_base_free_category==True: ##Free category 
                canvas.create_text((s_screen_width/first_colonne), (640), text=Rappel_CSV_Title[6],fill=s_font_color, font=s_font_family) ##7
            canvas.create_text((s_screen_width/scnd_colonne), (80), text=BaseDeMots[Numéro][1],fill="red", font=s_font_family) ##1
            canvas.create_text((s_screen_width/scnd_colonne), (160), text=BaseDeMots[Numéro][2],fill=s_font_color, font=s_font_family) ##2
            canvas.create_text((s_screen_width/scnd_colonne), (240), text=BaseDeMots[Numéro][3],fill="green", font=s_font_family) ##3
            #################################################################################################################################
            N4_1=("")
            N4_2=("")
            N4_3=("")
            #print("Len",len(BaseDeMots[Numéro][4]))
            if len(BaseDeMots[Numéro][4])<=45:
                N4_1=(BaseDeMots[Numéro][4][:45])
                #
            elif len(BaseDeMots[Numéro][4])<=90:
                N4_1=(BaseDeMots[Numéro][4][:45])
                #
                N4_2=(BaseDeMots[Numéro][4][45:90])
                if N4_1[len(N4_1)-1]!=" " or N4_1[len(N4_1)-1]!=",":
                    if N4_2[0]!=" " or N4_2[0]!=",":
                        N4_2="-"+N4_2
                #
            elif len(BaseDeMots[Numéro][4])<=135 and len(BaseDeMots[Numéro][4])>90:
                N4_1=(BaseDeMots[Numéro][4][:45])
                #
                N4_2=(BaseDeMots[Numéro][4][45:90])
                if N4_1[len(N4_1)-1]!=" " or N4_1[len(N4_1)-1]!=",":
                    if N4_2[0]!=" " or N4_2[0]!=",":
                        N4_2="-"+N4_2
                #    
                N4_3=(BaseDeMots[Numéro][4][90:135])
                if N4_2[len(N4_2)-1]!=" " or N4_2[len(N4_2)-1]!=",":
                    if N4_3[0]!=" " or N4_3[0]!=",":
                        N4_3="-"+N4_3
                #
            canvas.create_text((s_screen_width/scnd_colonne), (320), text=N4_1,fill=s_font_color, font=s_font_family) ##4
            canvas.create_text((s_screen_width/scnd_colonne), (350), text=N4_2,fill=s_font_color, font=s_font_family) ##4
            canvas.create_text((s_screen_width/scnd_colonne), (380), text=N4_3,fill=s_font_color, font=s_font_family) ##4
            #################################################################################################################################
            N5_1=("")
            N5_2=("")
            N5_3=("")
            #print("Len",len(BaseDeMots[Numéro][5]))
            if len(BaseDeMots[Numéro][5])<=45:
                N5_1=(BaseDeMots[Numéro][5][:45])
                #
            elif len(BaseDeMots[Numéro][5])<=90:
                N5_1=(BaseDeMots[Numéro][5][:45])
                #
                N5_2=(BaseDeMots[Numéro][5][45:90])
                if N5_1[len(N5_1)-1]!=" " or N5_1[len(N5_1)-1]!=",":
                    if N5_2[0]!=" " or N5_2[0]!=",":
                        N5_2="-"+N5_2
                #
            elif len(BaseDeMots[Numéro][5])<=135 and len(BaseDeMots[Numéro][5])>90:
                N5_1=(BaseDeMots[Numéro][5][:45])
                #
                N5_2=(BaseDeMots[Numéro][5][45:90])
                if N5_1[len(N5_1)-1]!=" " or N5_1[len(N5_1)-1]!=",":
                    if N5_2[0]!=" " or N5_2[0]!=",":
                        N5_2="-"+N5_2
                #
                N5_3=(BaseDeMots[Numéro][5][90:135])
                if N5_2[len(N5_2)-1]!=" " or N5_2[len(N5_2)-1]!=",":
                    if N5_3[0]!=" " or N5_3[0]!=",":
                        N5_3="-"+N5_3
                #
            canvas.create_text((s_screen_width/scnd_colonne), (420), text=N5_1,fill=s_font_color, font=s_font_family) ##5
            canvas.create_text((s_screen_width/scnd_colonne), (450), text=N5_2,fill=s_font_color, font=s_font_family) ##5
            canvas.create_text((s_screen_width/scnd_colonne), (480), text=N5_3,fill=s_font_color, font=s_font_family) ##5
            #################################################################################################################################
            if len(BaseDeMots[Numéro][6])>=45: ##6
                N6_1=(BaseDeMots[Numéro][6][:45])
                #
                N6_2=(BaseDeMots[Numéro][6][45:])
                if N6_1[len(N6_1)-1]!=" " or N6_1[len(N6_1)-1]!=",":
                    if N6_2[0]!=" " or N6_2[0]!=",":
                        N6_2="-"+N6_2
                canvas.create_text((s_screen_width/scnd_colonne), (560), text=N6_1,fill=s_font_color, font=s_font_family) ##6
                canvas.create_text((s_screen_width/scnd_colonne), (590), text=N6_2,fill=s_font_color, font=s_font_family) ##6
            else: ##5
                canvas.create_text((s_screen_width/scnd_colonne), (560), text=BaseDeMots[Numéro][6],fill=s_font_color, font=s_font_family) ##6
            #################################################################################################################################
            if data_base_free_category==True: ##Free category ##7
                if len(BaseDeMots[Numéro][7])>=45: ##6
                    N7_1=(BaseDeMots[Numéro][7][:45])
                    #
                    N7_2=(BaseDeMots[Numéro][7][45:])
                    if N7_1[len(N7_1)-1]!=" " or N7_1[len(N7_1)-1]!=",":
                        if N7_2[0]!=" " or N7_2[0]!=",":
                            N7_2="-"+N7_2
                    canvas.create_text((s_screen_width/scnd_colonne), (640), text=N7_1,fill=s_font_color, font=s_font_family) ##7
                    canvas.create_text((s_screen_width/scnd_colonne), (670), text=N7_2,fill=s_font_color, font=s_font_family) ##7
                else: ##5
                    canvas.create_text((s_screen_width/scnd_colonne), (640), text=BaseDeMots[Numéro][7],fill=s_font_color, font=s_font_family) ##7
            #################################################################################################################################
####End of the function Update####
Next() #Show the first card at launch.
root.mainloop()



###old features###

#menubar = Menu(root) ##1
#filemenu = Menu(menubar, tearoff=0) ##1
#menubar.add_cascade(label=Language[4], menu=filemenu) ##-Ajoute le bouton principale "Menu" ##1