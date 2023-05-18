#importing libraries 
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog


#add many songs to the playlist
def addsongs():
    #a list of songs is returned 
    t=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    #loop through everyitem in the list
    for i in t:
        i=i.replace("C:/Users/ar123/OneDrive/Desktop/","")
        songs_list.insert(END,i)
        
            
def deletesong():
    Current=songs_list.curselection()
    songs_list.delete(Current[0])
    
    
def Play():
    s=songs_list.get(ACTIVE)
    s=f'C:/Users/ar123/OneDrive/Desktop/{s}'
    mixer.music.load(s)
    mixer.music.play()

#to pause the song 
def Pause():
    mixer.music.pause()

#to stop the  song 
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

#to resume the song

def Resume():
    mixer.music.unpause()
    

#Function to navigate from the current song
def Previous():
    #to get the selected song index
    prev=songs_list.curselection()
    #to get the previous song index
    prev=prev[0]-1
    #to get the previous song
    temp2=songs_list.get(prev)
    temp2=f'C:/Users/ar123/OneDrive/Desktop/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #activate new song
    songs_list.activate(prev)
    #set the next song
    songs_list.selection_set(prev)

def Next():
    #to get the selected song index
    next_song=songs_list.curselection()
    #to get the next song index
    next_song=next_song[0]+1
    #to get the next song 
    temp=songs_list.get(next_song)
    temp=f'C:/Users/ar123/OneDrive/Desktop/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #activate newsong
    songs_list.activate(next_song)
     #set the next song
    songs_list.selection_set(next_song)

#creating the root window 
root=Tk()
root.title('Anurag music player ')
#initialize mixer 
mixer.init()

#create the listbox to contain songs
songs_list=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('arial',15),height=12,width=47,selectbackground="gray",selectforeground="black")
songs_list.grid(columnspan=9)

#font is defined which is to be used for the button font 
defined_font = font.Font(family='Britannic Bold')

#play button
play_button=Button(root,text="Play",width =7,command=Play)
play_button['font']=defined_font
play_button.grid(row=1,column=0)

#pause button 
pause_button=Button(root,text="Pause",width =7,command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1,column=1)

#stop button
stop_button=Button(root,text="Stop",width =7,command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1,column=2)

#resume button
Resume_button=Button(root,text="Resume",width =7,command=Resume)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=3)

#previous button
previous_button=Button(root,text="Prev",width =7,command=Previous)
previous_button['font']=defined_font
previous_button.grid(row=1,column=4)

#nextbutton
next_button=Button(root,text="Next",width =7,command=Next)
next_button['font']=defined_font
next_button.grid(row=1,column=5)

#menu 
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)


mainloop()

