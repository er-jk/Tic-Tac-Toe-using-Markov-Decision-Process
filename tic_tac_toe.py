import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random





def button(frame):          #Function to define a button
    b=Button(frame,bg="cyan",height=0,width=3,text="",font=('arial',60,'bold'),relief="sunken",bd=4)
    return b


root= tk.Tk(className = ' Tic Tac Toe')
root.geometry('483x545')
root.resizable(False,False)



def reset():
    for x in range(3):
        for y in range(3):
            b[x][y]['text'] = ""
            b[x][y]['state'] = 'normal'
            
def system_turn():
        win_check_opponent = [b[0][0]['text']==b[0][1]['text']==b[0][2]['text']=='X',
                                  b[1][0]['text']==b[1][1]['text']==b[1][2]['text']=='X',
                                  b[2][0]['text']==b[2][1]['text']==b[2][2]['text']=='X',
                                  b[0][0]['text']==b[1][0]['text']==b[2][0]['text']=='X',
                                  b[0][1]['text']==b[1][1]['text']==b[2][1]['text']=='X',
                                  b[0][2]['text']==b[1][2]['text']==b[2][2]['text']=='X',
                                  b[0][0]['text']==b[1][1]['text']==b[2][2]['text']=='X',
                                  b[2][0]['text']==b[1][1]['text']==b[0][2]['text']=='X']
        #print(win_check_opponent)
        if sum(win_check_opponent) > 0:
            messagebox.showinfo("Match Won!!","You Won")
            reset()
        else:
            win_oppurtunity_palayer = [(b[0][0]['text']==b[0][1]['text']== 'X' and b[0][2]['text']!='O') or (b[0][0]['text']==b[0][2]['text']=='X' and b[0][1]['text']!='O') or (b[0][1]['text']==b[0][2]['text']=='X' and b[0][0]['text']!='O'),
                               (b[1][0]['text']==b[1][1]['text']== 'X' and b[1][2]['text']!='O') or (b[1][0]['text']==b[1][2]['text']=='X' and b[1][1]['text']!='O') or (b[1][1]['text']==b[1][2]['text']=='X' and b[1][0]['text']!='O'),
                               (b[2][0]['text']==b[2][1]['text']== 'X' and b[2][2]['text']!='O') or (b[2][0]['text']==b[2][2]['text']=='X' and b[2][1]['text']!='O') or (b[2][1]['text']==b[2][2]['text']=='X' and b[2][0]['text']!='O'),
                               (b[0][0]['text']==b[1][0]['text']== 'X' and b[2][0]['text']!='O') or (b[0][0]['text']==b[2][0]['text']=='X' and b[1][0]['text']!='O') or (b[1][0]['text']==b[2][0]['text']=='X' and b[0][0]['text']!='O'),
                               (b[0][1]['text']==b[1][1]['text']== 'X' and b[2][1]['text']!='O') or (b[0][1]['text']==b[2][1]['text']=='X' and b[1][1]['text']!='O') or (b[1][1]['text']==b[2][1]['text']=='X' and b[0][1]['text']!='O'),
                               (b[0][2]['text']==b[1][2]['text']== 'X' and b[2][2]['text']!='O') or (b[0][2]['text']==b[2][2]['text']=='X' and b[1][2]['text']!='O') or (b[1][2]['text']==b[2][2]['text']=='X' and b[0][2]['text']!='O'), 
                               (b[0][0]['text']==b[1][1]['text']== 'X' and b[2][2]['text']!='O') or (b[0][0]['text']==b[2][2]['text']=='X' and b[1][1]['text']!='O') or (b[1][1]['text']==b[2][2]['text']=='X' and b[0][0]['text']!='O'),
                               (b[2][0]['text']==b[1][1]['text']== 'X' and b[0][2]['text']!='O') or (b[2][0]['text']==b[0][2]['text']=='X' and b[1][1]['text']!='O') or (b[1][1]['text']==b[0][2]['text']=='X' and b[2][0]['text']!='O')]

            print('win_oppurtunity_player'+str(win_oppurtunity_palayer))
            
            win_oppurtunity_machine = [(b[0][0]['text']==b[0][1]['text']== 'O' and b[0][2]['text']!='X') or (b[0][0]['text']==b[0][2]['text']=='O' and b[0][1]['text']!='X') or (b[0][1]['text']==b[0][2]['text']=='O' and b[0][0]['text']!='X'),
                               (b[1][0]['text']==b[1][1]['text']== 'O' and b[1][2]['text']!='X') or (b[1][0]['text']==b[1][2]['text']=='O' and b[1][1]['text']!='X') or (b[1][1]['text']==b[1][2]['text']=='O' and b[1][0]['text']!='X'),
                               (b[2][0]['text']==b[2][1]['text']== 'O' and b[2][2]['text']!='X') or (b[2][0]['text']==b[2][2]['text']=='O' and b[2][1]['text']!='X') or (b[2][1]['text']==b[2][2]['text']=='O' and b[2][0]['text']!='X'),
                               (b[0][0]['text']==b[1][0]['text']== 'O' and b[2][0]['text']!='X') or (b[0][0]['text']==b[2][0]['text']=='O' and b[1][0]['text']!='X') or (b[1][0]['text']==b[2][0]['text']=='O' and b[0][0]['text']!='X'),
                               (b[0][1]['text']==b[1][1]['text']== 'O' and b[2][1]['text']!='X') or (b[0][1]['text']==b[2][1]['text']=='O' and b[1][1]['text']!='X') or (b[1][1]['text']==b[2][1]['text']=='O' and b[0][1]['text']!='X'),
                               (b[0][2]['text']==b[1][2]['text']== 'O' and b[2][2]['text']!='X') or (b[0][2]['text']==b[2][2]['text']=='O' and b[1][2]['text']!='X') or (b[1][2]['text']==b[2][2]['text']=='O' and b[0][2]['text']!='X'), 
                               (b[0][0]['text']==b[1][1]['text']== 'O' and b[2][2]['text']!='X') or (b[0][0]['text']==b[2][2]['text']=='O' and b[1][1]['text']!='X') or (b[1][1]['text']==b[2][2]['text']=='O' and b[0][0]['text']!='X'),
                               (b[2][0]['text']==b[1][1]['text']== 'O' and b[0][2]['text']!='X') or (b[2][0]['text']==b[0][2]['text']=='O' and b[1][1]['text']!='X') or (b[1][1]['text']==b[0][2]['text']=='O' and b[2][0]['text']!='X')]

            print('win_oppurtunity_machine'+str(win_oppurtunity_machine))
##            print(sum(win_oppurtunity_machine))
##            print(sum(win_oppurtunity_palayer))
##            if sum(win_oppurtunity_palayer)>1:
##                messagebox.showinfo("Match Won!!","You Won")
##                reset()
            
##            if sum(win_oppurtunity_machine)>1:
##                pass


            if sum(win_oppurtunity_machine) >= 1:
                o_turn = win_oppurtunity_machine.index(True)
                #print(o_turn)
                if o_turn <= 2:
                    #print("entered")
                    for x in range(3):
                        #print(b[o_turn][x]['text'])
                        if b[o_turn][x]['text'] == "":
                            b[o_turn][x].config(text='O',state=DISABLED,disabledforeground='black')
                    
                            
                elif o_turn > 2 and o_turn <= 5:
                    #print("entered")
                    for x in range(3):
                        #print(b[o_turn][x]['text'])
                        if b[x][o_turn - 3]['text'] == "":
                            b[x][o_turn - 3].config(text='O',state=DISABLED,disabledforeground='black')
                    

                elif o_turn == 6:
                    #print("entered")
                    for x in range(3):
                        #print(b[o_turn][x]['text'])
                        if b[x][x]['text'] == "":
                            b[x][x].config(text='O',state=DISABLED,disabledforeground='black')

                elif o_turn == 7:
                    if b[2][0]['text'] == "":
                        b[2][0].config(text='O',state=DISABLED,disabledforeground='black')
                    if b[1][1]['text'] == "":
                        b[1][1].config(text='O',state=DISABLED,disabledforeground='black')    
                    if b[0][2]['text'] == "":
                        b[0][2].config(text='O',state=DISABLED,disabledforeground='black')

                messagebox.showinfo("Match Losed!!","Machine Won")
                reset()

                        
            elif sum(win_oppurtunity_palayer) >= 1:
                
                o_turn = win_oppurtunity_palayer.index(True) 
                #print(o_turn)
                if o_turn <= 2:
                    #print("entered")
                    for x in range(3):
                        #print(b[o_turn][x]['text'])
                        if b[o_turn][x]['text'] == "":
                            b[o_turn][x].config(text='O',state=DISABLED,disabledforeground='black')
                            
                elif o_turn > 2 and o_turn <= 5:
                    #print("entered")
                    for x in range(3):
                        #print(b[o_turn][x]['text'])
                        if b[x][o_turn - 3]['text'] == "":
                            b[x][o_turn - 3].config(text='O',state=DISABLED,disabledforeground='black')

                elif o_turn == 6:
                    #print("entered")
                    for x in range(3):
                        #print(b[o_turn][x]['text'])
                        if b[x][x]['text'] == "":
                            b[x][x].config(text='O',state=DISABLED,disabledforeground='black')

                elif o_turn == 7:
                    if b[2][0]['text'] == "":
                        b[2][0].config(text='O',state=DISABLED,disabledforeground='black')
                    if b[1][1]['text'] == "":
                        b[1][1].config(text='O',state=DISABLED,disabledforeground='black')    
                    if b[0][2]['text'] == "":
                        b[0][2].config(text='O',state=DISABLED,disabledforeground='black')

                
                        
            

                        
            else:
                 empty_area = []
                 for x in range(3):
                     for y in range(3):
                         if b[x][y]['text'] == "":
                             empty_area.append(str(x)+' '+str(y))

                 #print(empty_area)
                 try:
                     o_present=[]
                     for x in range(3):
                         for y in range(3):
                             if b[x][y]['text'] == 'O':
                                 o_present.append(str(x)+' '+str(y))
                     #print("O_presen----------------"+str(o_present))
                    
                     if o_present == []:
                         o_index = random.choice(empty_area)
                         #print(o_index)
                         b[int(o_index.split(' ')[0])][int(o_index.split(' ')[1])].config(text='O',state=DISABLED,disabledforeground='black')

                     else:
                         x = int(o_present[-1].split(' ')[0])
                         y = int(o_present[-1].split(' ')[1])
                         next_possibles = []
                         #print("entered")
                         next_move = [['0 0','0 1','0 2'],
                                      ['1 0','1 1','1 2'],
                                      ['2 0','2 1','2 2'],
                                      ['0 0','1 0','2 0'],
                                      ['0 1','1 1','2 1'],
                                      ['0 2','1 2','2 2'],
                                      ['0 0','1 1','2 2'],
                                      ['0 2','1 1','0 2']]
                         #print(o_present[-1])
                         for i in next_move:
                             if str(o_present[-1]) in i:
                                 next_possibles.append(i)
                         #print("next_possibles--------------------------"+str(next_possibles))
                         next_turn = []
                         for i in next_possibles:
                             #print("entered")
                             for j in i:
                                 #print(j)
                                 #print(b[int(j.split(' ')[0])][int(j.split(' ')[1])]['text'])
                                 if b[int(j.split(' ')[0])][int(j.split(' ')[1])]['text'] != 'X' and b[int(j.split(' ')[0])][int(j.split(' ')[1])]['text'] != 'O':
                                     next_turn.append(i)
                                     
                         #print("next_turn-----------------------------"+str(next_turn))
                         #print(len(next_turn))
                         r = random.randint(0,len(next_turn)-1)
                         #print(r)
                         #print(random.choice(next_turn[r]))
                         next_place = random.choice(next_turn[r])
                         if b[int(next_place.split(' ')[0])][int(next_place.split(' ')[1])]['text'] == '':
                            b[int(next_place.split(' ')[0])][int(next_place.split(' ')[1])].config(text='O',state=DISABLED,disabledforeground='black')
                         else:
                             o_index = random.choice(empty_area)
                             #print(o_index)
                             b[int(o_index.split(' ')[0])][int(o_index.split(' ')[1])].config(text='O',state=DISABLED,disabledforeground='black')
                              
                         

                         
                        
                             
                                   
                 except:
                     messagebox.showinfo("Tied!!","The match ended in a draw")
                     reset()      
            
        
        
                

def click(row,col):
        
        b[row][col].config(text='X',state=DISABLED,disabledforeground='red')
        system_turn()
                




colour={'O':"black",'X':"red"}
b=[[],[],[]]
for i in range(3):
    for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)


reset_button = tk.Button(root,bg = 'red',fg = 'black',text = 'Reset',font=('arial',12),command = reset)
reset_button.place(x=220,y=507)


root.mainloop()

