import tkinter as tk
import random
from tkinter import *
from tkinter import ttk
from Tournament import Tournament
from Rot import *
from Player import Player

class Registration(tk.Frame):
    def __init__(self, master=None, new_user_name = StringVar(), new_user_rank = StringVar(),
    number_of_players = 0, no_players = "Brak graczy", number_of_players_var = StringVar()):
        tk.Frame.__init__(self, master)
        self.new_user_name = new_user_name
        self.new_user_rank = new_user_rank
        self.number_of_players = number_of_players
        self.number_of_players_var = number_of_players_var
        self.no_players = no_players
        self.Reg_frame = ttk.Frame(self, padding="6 6 12 12")
        self.Reg_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.Reg_frame.columnconfigure(0, weight=1)
        self.Reg_frame.rowconfigure(0, weight=1)
        self.scrollbar = Scrollbar(self.Reg_frame, width = 240)
        self.players_list = Listbox(self.Reg_frame, yscrollcommand=self.scrollbar.set, exportselection=0, 
                                    width = 55, height = 5 )
        self.players_list.insert(self.number_of_players, no_players)
        self.scrollbar.config(command=self.players_list.yview)

        self.pack()
        self.createWidgets()

    def __del__(self, master=None):
        tk.Frame.__init__(self, master)

    def next(self):
        root2.deiconify()
        app = Tournament(master=root2)
        root1.withdraw()

    def quit(self):
        quitProgram()
        root3.destroy
        root2.destroy
        root1.destroy

    def add_new_user(self):
        """Add new user to program - players list"""
        user_id = self.number_of_players
        try:
            user_name = str(self.new_user_name.get())
            user_rank = int(self.new_user_rank.get())
            if (((isinstance(user_name, str)) == True) and
            (isinstance(user_rank, int) == True)):
                if (((user_name != "") and (user_name != self.no_players))
                and ((user_rank != "") )):
                    if (self.players_list.get(0,self.number_of_players) == self.no_players):
                        self.players_list.delete(0)
                    player = Player(user_id, user_name)
                    player.user_rank = user_rank
                    color = random.randrange(0,2)
                    if color == 1:
                        player.user_color = [1,0]
                    else:
                        player.user_color = [0,1]
                    len_of_name = len(player.user_name)
                    user_space = 50 - len_of_name
                    user_line =" "
                    for _ in range(user_space):
                        user_line +=" "
                    user_line = player.user_name + str(user_line) + str(player.user_rank)
                    print(user_line)
                    self.players_list.insert(self.number_of_players, user_line)
                    self.players_list.grid(column=5, columnspan=3, row=2, rowspan = 2, sticky=N)
                    self.new_user_name.set('')
                    self.new_user_rank.set('0')
                    self.number_of_players += 1
                    self.number_of_players_var.set(self.number_of_players)
                    ttk.Label(self.Reg_frame, 
                              textvariable=self.number_of_players_var).grid(column=7, row=4, sticky=E)
                    if self.number_of_players >= 2:
                        Start_tournament_button = ttk.Button(self.Reg_frame,
                        text="Rozegraj turniej >>", command = self.next, state=ACTIVE)
                        Start_tournament_button.grid(column=6, row=5, sticky=E)

                else:
                    #Add Message!
                    self.new_user_name.set('')
                    self.new_user_rank.set('')
            else:
                    #Add Message!
                    self.new_user_name.set('')
                    self.new_user_rank.set('')
        except ValueError:
            pass

    def createWidgets(self):
    # 4 Column
        ttk.Label(self.Reg_frame, text="Ilosc graczy:").grid(column=6, row=4, sticky=E)
        
        New_player_entry = ttk.Entry(self.Reg_frame, width=7, textvariable=self.new_user_name)
        New_player_entry.grid(column=4, row=2, sticky=(W, E), pady=5, padx=5)
        New_player_entry.focus()
        New_your_rank_entry = Spinbox(self.Reg_frame, from_=0.0, to=10000.0, textvariable=self.new_user_rank)
        New_your_rank_entry.grid(column=4, row=4, sticky=(W, E), pady=5, padx=5)

        self.players_list.grid(column=5, columnspan=3, row=2, rowspan = 2, sticky=N)
        self.scrollbar.grid(column=6, columnspan=2, row = 2, rowspan = 1, sticky=W, ipadx = 6, ipady = 16)

        Add_new_user = ttk.Button(self.Reg_frame, text="Dodaj uczestnika", command = self.add_new_user)
        Add_new_user.grid(column=4, row=5, sticky=W, pady=5, padx=5)
        
        ttk.Label(self.Reg_frame, text="Imie i nazwisko:").grid(column=4, row=1, sticky=W)
        ttk.Label(self.Reg_frame, text="Punkty rankingowe:").grid(column=4, row=3, sticky=W)
        # 5 Column
        List_of_users = ttk.Label(self.Reg_frame, text="Uczestnicy - Ranking")
        List_of_users.grid(column=5, row=1, sticky=W)
        Start_tournament_button = ttk.Button(self.Reg_frame, text="Rozegraj turniej >>", state=DISABLED)

        Start_tournament_button.grid(column=6, row=5, sticky=E)
        # 8 Column
        Button_End_Program = ttk.Button(self.Reg_frame, text="Zakoncz", command=quitProgram)
        Button_End_Program.grid(column=7, row=5, sticky=E)

