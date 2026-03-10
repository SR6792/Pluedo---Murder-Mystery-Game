from tkinter import *
from tkinter import messagebox

from tinydb import TinyDB, Query # Connects with a db ie json file

db = TinyDB('suspects_db.json')
Suspect = Query()

def get_suspect_data(name):
    # Hint: This looks for the first person in the DB matching the name
    result = db.search(Suspect.name == name)
    if result:
        return result[0]
    return None

def show_info(name):
    data = get_suspect_data(name)
    if data:
        messagebox.showinfo(f"{name}'s Whereabouts", data['info'])
window=Tk()
window.withdraw()
window.state('zoomed')

#check accusation
def check_accused(name):
    data = get_suspect_data(name)
    if(data['is_guilty']):
        messagebox.showinfo("Correct","Congratulation You got the killer")
    else:
        messagebox.showinfo("Incorrect","No This person is innocent")
    
#now make the start menu and suspect frame
start_menu = Frame(window,bg="#1a1a1a")
#level 1(ez)
suspects_menu=Frame(window,bg='white')
accuse_menu = Frame(window,bg='#821a05')
#to set func which on pressing btn goes to next page
def go_to_suspect():
    start_menu.pack_forget()
    suspects_menu.pack(expand=True,fill="both")

def exit():
    accuse_menu.pack_forget()
    start_menu.pack(expand=True,fill="both")

def accusation():
    suspects_menu.pack_forget()
    accuse_menu.pack(expand=True,fill='both')

window.title("Pluedo")
#now make startmenu
start_menu.pack(expand=True,fill="both")#to make a frame fill entire page
l1 = Label(start_menu,fg="White",bg="#1a1a1a",
           text="Pluedo-The Murder Mystery Game",
           font=("Helvetica", 40, "bold")).pack(pady=(200,20))
start_btn = Button(start_menu,text="Level 1",
                   command=go_to_suspect,padx=10,pady=10,font=("Helvetica", 22, "bold"),
                   bg="red",fg="white",activebackground="white",activeforeground="red").pack()


#now to make suspect page
murder_desc = Label(suspects_menu,
                    text="At Windfell Manor," \
                    "Thomas Windfell was murdered.His dead body was found at 10pm,Autopsy showed that he was dead 4 hours before the body was found.",
                    font=('arial',10),
                    fg="black",bg='white').pack()
suspects_title = Label(suspects_menu,text="Suspects",font=('arial',40,'bold'),bg='white').pack(pady=(20,10))

#now all 4 suspects(first inititalize img)
butler = PhotoImage(file="level 1/butler.png")
maid = PhotoImage(file="level 1/maid.png")
son = PhotoImage(file="level 1/son.png")
wife = PhotoImage(file="level 1/wife.png")

#create a min frame to store all suspects
f3 = Frame(suspects_menu,bg="white") 
f3.pack()
s1 = Label(f3,image=butler).grid(padx=20,pady=5,row = 0,column =0)
s1_btn = Button(f3,text="Butler",
                fg='white',bg='#1a1a1a',
                activebackground='white',activeforeground='#1a1a1a',command=lambda:show_info("Butler")).grid(row = 1,column =0)
s2 = Label(f3,image=maid).grid(row = 0,column =1)
s1_btn = Button(f3,text="Maid",fg='white',bg='#1a1a1a',
                activebackground='white',activeforeground='#1a1a1a',command=lambda:show_info("Maid")).grid(row = 1,column =1)
s3 = Label(f3,image=son).grid(pady=5,row = 2,column =0)
s1_btn = Button(f3,text="Son",fg='white',bg='#1a1a1a',
                activebackground='white',activeforeground='#1a1a1a',command=lambda:show_info("Son")).grid(row = 3,column =0)
s4 = Label(f3,image=wife).grid(row = 2,column =1)
s1_btn = Button(f3,text="Wife",fg='white',bg='#1a1a1a',
                activebackground='white',activeforeground='#1a1a1a',command=lambda:show_info("Wife")).grid(row = 3,column =1)

#accuse btn
accuse_btn = Button(suspects_menu,text="Accuse",fg="white",bg="red",command=accusation,padx=10,pady=10).pack(pady=(10,10))

#accuse screen
suspects_title = Label(accuse_menu,text="Whodunnit",font=('arial',40,'bold'),bg='#821a05',fg='black').pack(pady=(20,10))
f4 = Frame(accuse_menu,bg="white") 
f4.pack()
s11 = Label(f4,image=butler).grid(padx=20,pady=5,row = 0,column =0)
s11_btn = Button(f4,text="Accuse",
                fg='white',bg='#821a05',
                activebackground='white',activeforeground='#1a1a1a',command=lambda:check_accused("Butler")).grid(row = 1,column =0)
s22 = Label(f4,image=maid).grid(row = 0,column =1)
s22_btn = Button(f4,text="Accuse",fg='white',bg='#821a05',
                activebackground='white',activeforeground='#1a1a1a',command=lambda:check_accused("Maid")).grid(row = 1,column =1)
s33 = Label(f4,image=son).grid(pady=5,row = 2,column =0)
s33_btn = Button(f4,text="Accuse",fg='white',bg='#821a05',
                activebackground='white',activeforeground='#1a1a1a',command=lambda:check_accused("Son")).grid(row = 3,column =0)
s44 = Label(f4,image=wife).grid(row = 2,column =1)
s44_btn = Button(f4,text="Accuse",fg='white',bg='#821a05',
                activebackground='white',activeforeground='#1a1a1a',command=lambda:check_accused("Wife")).grid(row = 3,column =1)


exit_btn = Button(accuse_menu,text="Exit",bg="black",fg="white",activebackground='white',activeforeground='black',command=exit).pack()

#level 2(hard)
#case file
case_File=Frame(window,bg='white')
suspects_menu2=Frame(window,bg='white')
accuse_menu2 = Frame(window,bg='#821a05',padx=20,pady=20)
def go_to_caseFile2():
    start_menu.pack_forget()
    case_File.pack(expand=True,fill=BOTH)

start_btn2 = Button(start_menu,text="Level 2",
                   command=go_to_caseFile2,padx=10,pady=10,font=("Helvetica", 22, "bold"),
                   bg="red",fg="white",activebackground="white",activeforeground="red").pack(pady=(10,10))
case_File2 = PhotoImage(file='level 2/caseF2.png')
daughter = PhotoImage(file="level 2/daughter.png")
gardener = PhotoImage(file="level 2/gardener.png")
husband = PhotoImage(file="level 2/husband.png")
maid2 = PhotoImage(file="level 2/maid.png")
salesman = PhotoImage(file="level 2/salesman.png")
#case_File
canvas = Canvas(case_File,width=1200,height=700)
canvas.pack()

canvas.create_image(600,350,image=case_File2)
canvas.create_text(600,100,text="Victim died at 6pm.",font='25px',anchor='nw')
canvas.create_text(600,130,text="Body found by Mark Wain(Her Husband),when he went to her.",font='25px',justify='left',width=400,anchor="nw")
canvas.create_text(600,190,text="The Cause of death was blunt force trauma to the head caused by a heavy object.",font='25px',justify='left',width='400',anchor='nw')
canvas.create_text(600,270,text="Coincidentally,an candlestand was reported missing by the maid.",font='25px',justify='left',width='400',anchor='nw')
canvas.create_text(600,330,text="There was a salesman at the door who was being attended to by Agatha wain(victim's daughter),during the time of death.",font='25px',justify='left',width='400',anchor='nw')
canvas.create_text(600,430,text="Victim is Catherine Wain,who was a rich businesswomen from the pharmaceutical industry.",font='25px',justify='left',width='400',anchor='nw')
def go_to_statement():
    case_File.pack_forget()
    suspects_menu2.pack(expand=True,fill="both")
#statement
statement_btn = Button(case_File,text='Next',background='red',font='25',command=go_to_statement)
statement_btn.place(x=900,y=500)
label_head = Label(suspects_menu2,text='Suspect',font='25',background='white').pack()
all_sus = Frame(suspects_menu2,bg='#fdf5e6')
all_sus.pack(pady=10)
#new frame for each suspect
susp1_f = Frame(window,bg='white')
susp2_f = Frame(window,bg='white')
susp3_f = Frame(window,bg='white')
susp4_f = Frame(window,bg='white')
susp5_f = Frame(window,bg='white')
#now for function when info btn is clicked
def susp1_info():
    suspects_menu2.pack_forget()
    susp1_f.pack(expand=True,fill="both")

def susp2_info():
    suspects_menu2.pack_forget()
    susp2_f.pack(expand=True,fill="both")

def susp3_info():
    suspects_menu2.pack_forget()
    susp3_f.pack(expand=True,fill="both")

def susp4_info():
    suspects_menu2.pack_forget()
    susp4_f.pack(expand=True,fill="both")

def susp5_info():
    suspects_menu2.pack_forget()
    susp5_f.pack(expand=True,fill="both")

susp1 = Label(all_sus,image=daughter)
susp1.grid(row=0,column=0,padx=20, pady=10)
susp1_name=Label(all_sus,text='Daughter')
susp1_name.grid(row=1, column=0)
susp1_info_btn = Button(all_sus,text='Info',command=susp1_info)
susp1_info_btn.grid(row=2,column=0,pady=10)

susp2 = Label(all_sus,image=gardener)
susp2.grid(row=0,column=1,padx=20, pady=10)
susp2_name=Label(all_sus,text='Gardener')
susp2_name.grid(row=1 ,column=1)
susp2_info_btn = Button(all_sus,text='Info',command=susp2_info)
susp2_info_btn.grid(row=2,column=1,pady=10)

susp3 = Label(all_sus,image=salesman)
susp3.grid(row=0,column=2,padx=20, pady=10)
susp3_name=Label(all_sus,text='Salesman')
susp3_name.grid(row=1 ,column=2)
susp3_info_btn = Button(all_sus,text='Info',command=susp3_info)
susp3_info_btn.grid(row=2,column=2,pady=10)

susp4 = Label(all_sus,image=husband)
susp4.grid(row=3,column=0,padx=20, pady=10)
susp1_name=Label(all_sus,text='Husband')
susp1_name.grid(row=4 ,column=0)
susp4_info_btn = Button(all_sus,text='Info',command=susp4_info)
susp4_info_btn.grid(row=5,column=0,pady=10)

susp5 = Label(all_sus,image=maid2)
susp5.grid(row=3,column=2,padx=20, pady=10)
susp5_name=Label(all_sus,text='Maid')
susp5_name.grid(row=4 ,column=2)
susp5_info_btn = Button(all_sus,text='Info',command=susp5_info)
susp5_info_btn.grid(row=5,column=2,pady=10)


#detail on suspect 1
susp1_name1 = Label(susp1_f,text="Suspect 1",font='25',bg='white')
susp1_name1.pack(pady=10)
susp1_moreinfo = Frame(susp1_f,bg='white')
susp1_moreinfo.pack()

susp1_1 = Label(susp1_moreinfo,text="Agatha Wain(Daughter of Victim)",font='25',bg='white')
susp1_1.grid(row=0,column=0,pady=10)
susp1_img = Label(susp1_moreinfo,image=daughter)
susp1_img.grid(row=1,column=0)
susp1_2 = Label(susp1_moreinfo,text="Question Log",font='25',bg='white')
susp1_2.grid(row=2,column=0,pady=(10,1),padx=30)
resp = Frame(susp1_moreinfo,bg='white',relief="sunken",highlightbackground='black',highlightthickness='5')
resp.grid(row=0,column=1,rowspan=8,padx=20)
resp.grid_propagate(False)
resp.config(width=500,height=500)
h1 = Label(resp,text='Response Log',bg='white',font='25')
h1.place(x=10,y=10)
answer = Label(resp,text="Select a question to ask the suspect",bg='white',font='25', wraplength=400, justify='left')
answer.place(x=10,y=50)
#supsect 1 reply
def ans(ans_t):
    answer.config(text=ans_t)
q1 = Button(susp1_moreinfo,text='Explain your wherabouts during the murder',bg='white',command=lambda: ans('I was attending a persistant salesman who wanted to sell some expensive cream.'))
q1.grid(row=3,column=0,pady=2,sticky='ew')
q2 = Button(susp1_moreinfo,text='Do you think anybody could have a motive to kill your mother',bg='white',command=lambda : ans('Actually I believe all of them respected and cared for my mother.'))
q2.grid(row=4,column=0,pady=2,sticky='ew')
q3 = Button(susp1_moreinfo,text='What of the will,I assume she must have left money for her family being a rich person she is',bg='white',command=lambda : ans('I think she divided her wealth equally among us,You have to ask my father as he is in charge of the will.'))
q3.grid(row=5,column=0,pady=2,sticky='ew')
q4 = Button(susp1_moreinfo,text='Did you harbor her ill will',bg='white',command=lambda : ans('I am not in good state of mind to entertain such stupid questions'))
q4.grid(row=6,column=0,pady=2,sticky='ew')
q5 = Button(susp1_moreinfo,text='Anything else you want to add that can aid the investigation',bg='white',command=lambda : ans('None'))
q5.grid(row=7,column=0,pady=2,sticky='ew')
def goback(f,susn):#click this btn exit_to suspect then go back to supect frame ie f from sup1_moreinfo
    susn.pack_forget()
    f.pack(expand=True,fill='both')
exit_to_suspect = Button(susp1_moreinfo,text='Exit',command=lambda: goback(suspects_menu2,susp1_f),)
exit_to_suspect.grid(row=9 ,column = 4)


#detail on suspect 2
susp2_name1 = Label(susp2_f,text="Suspect 2",font='25',bg='white')
susp2_name1.pack(pady=10)
susp2_moreinfo = Frame(susp2_f,bg='white')
susp2_moreinfo.pack()

susp2_1 = Label(susp2_moreinfo,text="Mark Cain(Gardener)",font='25',bg='white')
susp2_1.grid(row=0,column=0,pady=10)
susp2_img = Label(susp2_moreinfo,image=gardener)
susp2_img.grid(row=1,column=0)
susp2_2 = Label(susp2_moreinfo,text="Question Log",font='25',bg='white')
susp2_2.grid(row=2,column=0,pady=(10,1),padx=30)
resp2 = Frame(susp2_moreinfo,bg='white',relief="sunken",highlightbackground='black',highlightthickness='5')
resp2.grid(row=0,column=1,rowspan=8,padx=20)
resp2.grid_propagate(False)
resp2.config(width=500,height=500)
h2 = Label(resp2,text='Response Log',bg='white',font='25')
h2.place(x=10,y=10)
answer2 = Label(resp2,text="Select a question to ask the suspect",bg='white',font='25', wraplength=400, justify='left')
answer2.place(x=10,y=50)
#supsect 2 reply
def ans2(ans_t):
    answer2.config(text=ans_t)
q1 = Button(susp2_moreinfo,text='Do you know anyone who has an motive to murder Mrs Wain',bg='white',command=lambda: ans2('Being the businesswomen she is,she must have many enemies,but none who wishes her dead.'))
q1.grid(row=3,column=0,pady=2,sticky='ew')
q2 = Button(susp2_moreinfo,text='What about your wherabouts during the murder',bg='white',command=lambda : ans2('I was Pruning the shrubs.'))
q2.grid(row=4,column=0,pady=2,sticky='ew')
q3 = Button(susp2_moreinfo,text='Is there anything else you saw or heard that may help us catch the murderer',bg='white',command=lambda : ans2('While I was pruning the bushes,I heard madam arguing with Sir.She said "I know what you did",which he denies.'))
q3.grid(row=5,column=0,pady=2,sticky='ew')

exit_to_suspect2 = Button(susp2_moreinfo,text='Exit',command=lambda: goback(suspects_menu2,susp2_f),)
exit_to_suspect2.grid(row=9 ,column = 4)

#suspect 3
susp3_name1 = Label(susp3_f,text="Suspect 3",font='25',bg='white')
susp3_name1.pack(pady=10)
susp3_moreinfo = Frame(susp3_f,bg='white')
susp3_moreinfo.pack()

susp3_1 = Label(susp3_moreinfo,text="Andrew Wares(The Salesman)",font='25',bg='white')
susp3_1.grid(row=0,column=0,pady=10)
susp3_img = Label(susp3_moreinfo,image=salesman)
susp3_img.grid(row=1,column=0)
susp3_2 = Label(susp3_moreinfo,text="Question Log",font='25',bg='white')
susp3_2.grid(row=2,column=0,pady=(10,1),padx=30)
resp3 = Frame(susp3_moreinfo,bg='white',relief="sunken",highlightbackground='black',highlightthickness='5')
resp3.grid(row=0,column=1,rowspan=8,padx=20)
resp3.grid_propagate(False)
resp3.config(width=500,height=500)
h3 = Label(resp3,text='Response Log',bg='white',font='25')
h3.place(x=10,y=10)
answer3 = Label(resp3,text="Select a question to ask the suspect",bg='white',font='25', wraplength=350, justify='left')
answer3.place(x=10,y=50)
#supsect 4 reply
def ans3(ans_t):
    answer3.config(text=ans_t)
q1 = Button(susp3_moreinfo,text="Did You know there was a murder that occured while You visited Wain's home",bg='white',command=lambda: ans3('Frankly I knew something had happened when the police came but I never guessed it was murder.'))
q1.grid(row=3,column=0,pady=2,sticky='ew')
q2 = Button(susp3_moreinfo,text='What about your wherabouts during the murder',bg='white',command=lambda : ans3('I was unsuccessfully trying to sell My wares to Mrs Wains Daughter.'))
q2.grid(row=4,column=0,pady=2,sticky='ew')
q3 = Button(susp3_moreinfo,text='Anything You can add which will aid the investigation',bg='white',command=lambda : ans3('I saw Mr Wain walking angrily'))
q3.grid(row=5,column=0,pady=2,sticky='ew')
exit_to_suspect3 = Button(susp3_moreinfo,text='Exit',command=lambda: goback(suspects_menu2,susp3_f),)
exit_to_suspect3.grid(row=9 ,column = 4)

#suspect 4
susp4_name1 = Label(susp4_f,text="Suspect 4",font='25',bg='white')
susp4_name1.pack(pady=10)
susp4_moreinfo = Frame(susp4_f,bg='white')
susp4_moreinfo.pack()

susp4_1 = Label(susp4_moreinfo,text="Mr Mark Wain(Victim's husband)",font='25',bg='white')
susp4_1.grid(row=0,column=0,pady=10)
susp4_img = Label(susp4_moreinfo,image=husband)
susp4_img.grid(row=1,column=0)
susp4_2 = Label(susp4_moreinfo,text="Question Log",font='25',bg='white')
susp4_2.grid(row=2,column=0,pady=(10,1),padx=30)
resp4 = Frame(susp4_moreinfo,bg='white',relief="sunken",highlightbackground='black',highlightthickness='5')
resp4.grid(row=0,column=1,rowspan=8,padx=20)
resp4.grid_propagate(False)
resp4.config(width=500,height=500)
h4 = Label(resp4,text='Response Log',bg='white',font='25')
h4.place(x=10,y=10)
answer4 = Label(resp4,text="Select a question to ask the suspect",bg='white',font='25', wraplength=350, justify='left')
answer4.place(x=10,y=50)
#supsect 4 reply
def ans4(ans_t):
    answer4.config(text=ans_t)
q1 = Button(susp4_moreinfo,text="How are you handling the news of your wife's death",bg='white',command=lambda: ans4('I am devastated ,but my daughter has been a good pillar of support for me.'))
q1.grid(row=3,column=0,pady=2,sticky='ew')
q2 = Button(susp4_moreinfo,text="Could you tell me more about your late wife's will",bg='white',command=lambda : ans4('Most of her assets go to a trust fund set up for our daughter, for which I am in charge till she graduates from College.'))
q2.grid(row=4,column=0,pady=2,sticky='ew')
q3 = Button(susp4_moreinfo,text='What about your wherabouts during the murder',bg='white',command=lambda : ans4('I was in the library till 7pm'))
q3.grid(row=5,column=0,pady=2,sticky='ew')
q3 = Button(susp4_moreinfo,text='Anything You can add which will aid the investigation',bg='white',command=lambda : ans4('None whatsoever'))
q3.grid(row=6,column=0,pady=2,sticky='ew')
exit_to_suspect4 = Button(susp4_moreinfo,text='Exit',command=lambda: goback(suspects_menu2,susp4_f),)
exit_to_suspect4.grid(row=9 ,column = 4)

#suspect 5
susp5_name1 = Label(susp5_f,text="Suspect 5",font='25',bg='white')
susp5_name1.pack(pady=10)
susp5_moreinfo = Frame(susp5_f,bg='white')
susp5_moreinfo.pack()

susp5_1 = Label(susp5_moreinfo,text="Carmelia Clean(The Maid)",font='25',bg='white')
susp5_1.grid(row=0,column=0,pady=10)
susp5_img = Label(susp5_moreinfo,image=maid2)
susp5_img.grid(row=1,column=0)
susp5_2 = Label(susp5_moreinfo,text="Question Log",font='25',bg='white')
susp5_2.grid(row=2,column=0,pady=(10,1),padx=30)
resp5 = Frame(susp5_moreinfo,bg='white',relief="sunken",highlightbackground='black',highlightthickness='5')
resp5.grid(row=0,column=1,rowspan=8,padx=20)
resp5.grid_propagate(False)
resp5.config(width=500,height=500)
h5 = Label(resp5,text='Response Log',bg='white',font='25')
h5.place(x=10,y=10)
answer5 = Label(resp5,text="Select a question to ask the suspect",bg='white',font='25', wraplength=350, justify='left')
answer5.place(x=10,y=50)
#supsect 5 reply
def ans5(ans_t):
    answer5.config(text=ans_t)
q1 = Button(susp5_moreinfo,text="You reported the Missing candlestand, Yes ?",bg='white',command=lambda: ans5('Yes I noticed the missing candlestand when i was busy cleaning the living room.'))
q1.grid(row=3,column=0,pady=2,sticky='ew')
q3 = Button(susp5_moreinfo,text='What about your wherabouts during the murder',bg='white',command=lambda : ans5('I was cleaning the house during that time'))
q3.grid(row=4,column=0,pady=2,sticky='ew')
q3 = Button(susp5_moreinfo,text='Anything You can add which will aid the investigation',bg='white',command=lambda : ans5("Two days ago I heard madame talking to someone about needing an 'audit'.She said something about being cheated ,about somebody embezzling her trust fund."))
q3.grid(row=5,column=0,pady=2,sticky='ew')
exit_to_suspect5 = Button(susp5_moreinfo,text='Exit',command=lambda: goback(suspects_menu2,susp5_f),)
exit_to_suspect5.grid(row=9 ,column = 4)

def accuse2():
    suspects_menu2.pack_forget()
    accuse_menu2.pack(expand=True,anchor='center')

accuse_btn2 = Button(all_sus,text="Accuse",bg='red',command=accuse2)
accuse_btn2.grid(row=5,column = 3,padx=10,pady=10)

#acc btn
def susp1_acc():
    messagebox.showinfo("Wrong","Daughter is not the Murderer,because she gets the money even if victim still alive")

def susp2_acc():
    messagebox.showinfo("Wrong","The gardener didnt kill Mrs Wain.")

def susp4_acc():
    messagebox.showinfo("Correct","Mr Wain killed his wife because:")
    messagebox.showinfo("1","She caught a 'Man' who embezzled her fund")
    messagebox.showinfo("2","Salesman noticed an angry Mark Wain,probably after arguing with the victim,")
    messagebox.showinfo("3","Gardener hears the victim arguing with a man saying 'I know what you did' further implying that the husband is guilty of something.")

def susp3_acc():
    messagebox.showinfo("Wrong","The salesman could'nt kill the victim as he had a good alibi,he was busy selling his goods to victim's daughter")

def susp5_acc():
    messagebox.showinfo("Wrong","The maid won't gain anything from the death of victim")
#accuse menu

susp1 = Label(accuse_menu2,image=daughter)
susp1.grid(row=0,column=0,padx=20, pady=10)
susp1_info_btn = Button(accuse_menu2,text='Accuse',command=susp1_acc)
susp1_info_btn.grid(row=1,column=0)

susp2 = Label(accuse_menu2,image=gardener)
susp2.grid(row=0,column=1,padx=20, pady=10)
susp2_info_btn = Button(accuse_menu2,text='Accuse',command=susp2_acc)
susp2_info_btn.grid(row=1,column=1)

susp3 = Label(accuse_menu2,image=salesman)
susp3.grid(row=0,column=2,padx=20, pady=10)
susp3_info_btn = Button(accuse_menu2,text='Accuse',command=susp3_acc)
susp3_info_btn.grid(row=1,column=2)

susp4 = Label(accuse_menu2,image=husband)
susp4.grid(row=3,column=0,padx=20, pady=10)
susp4_info_btn = Button(accuse_menu2,text='Accuse',command=susp4_acc)
susp4_info_btn.grid(row=4,column=0)

susp5 = Label(accuse_menu2,image=maid2)
susp5.grid(row=3,column=2,padx=20, pady=10)
susp5_info_btn = Button(accuse_menu2,text='Accuse',command=susp5_acc)
susp5_info_btn.grid(row=4,column=2)

def exit_to_main_menu():
    accuse_menu2.pack_forget()
    start_menu.pack(expand=True,fill="both")

exit_btn1 = Button(accuse_menu2,bg='black',fg='white',text='Exit',command=exit_to_main_menu)
exit_btn1.grid(row=5,column=3)
window.update_idletasks()
window.deiconify()
window.update()
window.mainloop()