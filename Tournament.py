import tkinter as tk
from tkinter import *
from tkinter import ttk
from Results import Results
from Rot import *
from Player import Player
from operator import itemgetter
from itertools import groupby

class Tournament(tk.Frame):
    def __init__(self, master=None, First_user_name = StringVar(), Second_user_name = StringVar(), 
                 player_one_id = 0, player_two_id = 0, First_player = 0, Second_player = 0, 
                 first_new_user_points = StringVar(), second_new_user_points = StringVar(), 
                 second_player_id = 0, first_player_id = 0, rounde = StringVar()):
        tk.Frame.__init__(self, master)
        self.First_user_name = StringVar()
        self.Second_user_name = StringVar()
        self.player_two_id = player_two_id
        self.player_one_id = player_one_id
        self.rounde = rounde
        self.round = 1
        self.player_one_oponents = [] 
        self.player_two_oponents = []
        self.first_new_user_points = first_new_user_points
        self.second_new_user_points = second_new_user_points
        self.second_player_id = second_player_id
        self.first_player_id = first_player_id
        self.Tou_frame = ttk.Frame(self, padding="6 12 12 12")
        self.Tou_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.Tou_frame.columnconfigure(0, weight=1)
        self.Tou_frame.rowconfigure(0, weight=1)
        
        self.scrollbar = Scrollbar(self.Tou_frame)
        self.players_list = Listbox(self.Tou_frame, width = 55, height = 10, yscrollcommand=self.scrollbar.set, 
                                    exportselection=0)
        self.scrollbar.config(command=self.players_list.yview)
        
        self.first_players_list = []
        self.second_players_list = []
        self.third_unpaired_list = []
        self.list_of_players = []
        self.pack()
        self.createWidgets()
        self.updateTable()

    def __del__(self, master=None):
        tk.Frame.__init__(self, master)

    def next(self):
        root3.deiconify()
        app = Results(master=root3)
        root2.withdraw()

    def quit(self):
        quitProgram()
        root.quit() 
        
    def add_points_to_players(self):
        print(self.player_one_id)
        print(self.player_two_id)
        First_player = None
        Second_player = None
        
        for item in self.list_of_players:
            if item.user_id == self.player_one_id:
                First_player = item
            elif item.user_id == self.player_two_id: 
                Second_player =  item  
                
        if First_player == None and Second_player == None:
            print("Blad, brakuje ID")
        
        added_first_user_points = int(self.first_new_user_points.get())
        added_second_user_points = int(self.second_new_user_points.get())
        first_user_points = First_player.user_points
        second_user_points = Second_player.user_points
        
        if (added_first_user_points != None and added_second_user_points != None):
            First_player.user_points = added_first_user_points + first_user_points
            Second_player.user_points = added_second_user_points + second_user_points
            First_player.oponents.append(Second_player.user_id)
            Second_player.oponents.append(First_player.user_id)

            if First_player.user_color[0] >= First_player.user_color[1]:   
                First_player.user_color[1] = First_player.user_color[1] + 1
            else:
                First_player.user_color[0] = First_player.user_color[0] + 1
 
            if Second_player.user_color[0] >= Second_player.user_color[1]:   
                Second_player.user_color[1] = Second_player.user_color[1] + 1
            else:
                Second_player.user_color[0] = Second_player.user_color[0] + 1
                               
            First_player.user_round = First_player.user_round + 1
            Second_player.user_round = Second_player.user_round + 1
            
            print(First_player.user_name, " rozegral walke z ", Second_player.user_name)
            print(First_player.user_name, "(", First_player.user_id ,") walczyl juz z ", First_player.oponents)
            print(Second_player.user_name, "(", Second_player.user_id , ")  walczyl juz z ", Second_player.oponents)
            
            print("Gracz ", First_player.user_name, " otrzymal punktow: ", 
                  added_first_user_points, "i ma ich obecnie", First_player.user_points, " tego gracza to ", 
                  First_player.user_round, " runda.")
            print("Gracz ", Second_player.user_name, " otrzymal punktow: ", 
                  added_second_user_points, "i ma ich obecnie", Second_player.user_points, " tego gracza to ", 
                  Second_player.user_round, " runda.")
            
            self.first_new_user_points = StringVar()
            self.second_new_user_points = StringVar()
            self.First_user_name.set("")
            self.Second_user_name.set("")
            if (self.third_unpaired_list != []):
                self.third_unpaired_list[0].user_points = self.third_unpaired_list[0].user_points + 1
                print("Gracz", self.third_unpaired_list[0].user_name, " otrzymuje wolny los, czyli dostaje punkt bez gry.")
                print(self.third_unpaired_list[0].user_name, " ma wiec teraz: ", self.third_unpaired_list[0].user_points)
                self.third_unpaired_list[0].user_round = self.third_unpaired_list[0].user_round + 1
                self.third_unpaired_list[0].free_point = 1
            self.updateTable()
            self.add_points(DISABLED)

    def add_points(self, status):
        if status == ACTIVE:
            Add_new_user = ttk.Button(self.Tou_frame, text="Przyznaj punkty", 
                                      command = self.add_points_to_players, state = ACTIVE)
            Add_new_user.grid(column=3, row=5, sticky=W, pady=6, padx=6)
            Results_button = ttk.Button(self.Tou_frame, state = DISABLED, 
                                        text="Pokaz ostateczne wyniki >>", command = self.next)
            Results_button.grid(column=3, row=6, sticky=W, pady=6, padx=6)
            Search_players_button = ttk.Button(self.Tou_frame, text="Wylosuj graczy", state = DISABLED)
            Search_players_button.grid(column=3, row=3, sticky=W, pady=6, padx=6)
            
            First_player_points_box = Spinbox(self.Tou_frame, from_=0.0, to=10000.0,
            textvariable=self.first_new_user_points, state = NORMAL)
            First_player_points_box.grid(column=1, row=5, sticky=(W, E), pady=6, padx=6)
            Second_player_points_box = Spinbox(self.Tou_frame, from_=0.0, to=10000.0,
            textvariable=self.second_new_user_points, state = NORMAL)
            Second_player_points_box.grid(column=2, row=5, sticky=(W, E), pady=6, padx=6)
            print("ACTIVE")
            
        if status == DISABLED:
            Add_new_user = ttk.Button(self.Tou_frame, text="Przyznaj punkty", state = DISABLED)
            Add_new_user.grid(column=3, row=5, sticky=W, pady=6, padx=6)
            Results_button = ttk.Button(self.Tou_frame, state = ACTIVE, text="Pokaz ostateczne wyniki >>", 
                                        command = self.next)
            Results_button.grid(column=3, row=6, sticky=W, pady=6, padx=6)
            Search_players_button = ttk.Button(self.Tou_frame, text="Wylosuj graczy", 
                                               command = self.look_for_players, state = ACTIVE)
            Search_players_button.grid(column=3, row=3, sticky=W, pady=6, padx=6)
            
            First_player_points_box = Spinbox(self.Tou_frame, from_=0.0, to=10000.0,
            textvariable=self.first_new_user_points, state = DISABLED)
            First_player_points_box.grid(column=1, row=5, sticky=(W, E), pady=6, padx=6)
            Second_player_points_box = Spinbox(self.Tou_frame, from_=0.0, to=10000.0,
            textvariable=self.second_new_user_points, state = DISABLED)
            Second_player_points_box.grid(column=2, row=5, sticky=(W, E), pady=6, padx=6)
            print("DISABLED")
            
    def updateTable(self):
        self.players_list = Listbox(self.Tou_frame, width = 55, height = 10, yscrollcommand=self.scrollbar.set, 
                                    exportselection=0)
        i = 0
        print("Lista posortowana")
        sort_list = sorted(Player._registry, key=lambda player: player.user_points, reverse=True)
        print(sort_list)
        for item in sort_list:
            len_of_name = len(item.user_name)
            user_space = 20 - len_of_name
            user_line =" "
            for _ in range(user_space):
                user_line +=" "
            user_line = item.user_name + str(user_line) + str(item.user_points) 
            user_line += str(" pkt, ") + str(" rozegranych rund: ") + str(item.user_round - 1) 
            self.players_list.insert(i, user_line)
            i += 1
            
        List_of_users = ttk.Label(self.Tou_frame, text="Wyniki uczestnikow:")
        List_of_users.grid(column=6, row=1, sticky=W)
        
        self.players_list.grid(column=6, columnspan=2, row=2, rowspan = 2, sticky=N, pady=6)
        self.scrollbar.grid(column=8, columnspan=2, row = 2, rowspan = 4, sticky=N, pady = 7, ipady = 55)
        
    def createWidgets(self):
        ttk.Label(self.Tou_frame, text="Przyznaj punkty wybranym przez system gracza").grid(
        column=2, columnspan=2, row=1, sticky=W, pady=6)
        
        # 1 Column
        First_player_points_entry = ttk.Entry(self.Tou_frame, width=7, textvariable=self.First_user_name,
        state = DISABLED)
        First_player_points_entry.grid(column=1, row=3, sticky=(W, E), pady=6, padx=6)
        ttk.Label(self.Tou_frame, text="Imie i nazwisko:").grid(column=1, row=2, sticky=W, pady=6, padx=6)
        ttk.Label(self.Tou_frame, text="Punkty rankingowe:").grid(column=1, row=4, sticky=W, pady=6, padx=6)

        # 2 Column
        Second_player_points_entry = ttk.Entry(self.Tou_frame, width=7, 
                                               textvariable=self.Second_user_name, state = DISABLED)
        Second_player_points_entry.grid(column=2, row=3, sticky=(W, E), pady=6, padx=6)
        ttk.Label(self.Tou_frame, text="Imie i nazwisko:").grid(column=2, row=2, sticky=W, pady=6, padx=6)
        ttk.Label(self.Tou_frame, text="Punkty rankingowe:").grid(column=2, row=4, sticky=W, pady=6, padx=6)
        
        # 6 Row
        Button_End_Program = ttk.Button(self.Tou_frame, text="Zakoncz", command=self.quit)
        Button_End_Program.grid(column=5, row=6, sticky=W, pady=6, padx=6)

        self.rounde.set(self.round)
        ttk.Label(self.Tou_frame, text="Tura:").grid(column=1, row=6, sticky=W)
        ttk.Label(self.Tou_frame, textvariable=self.rounde).grid(column=1, row=6, sticky=W, padx=30)
                       
        self.add_points(DISABLED)
            
    def look_for_players(self):
        if self.first_players_list == [] and self.second_players_list == []:
            print("Trwa runda:", self.round)
            self.create_list("rank")
            self.get_id_players()
        else:
            self.get_id_players()
        
    def get_id_players(self):
        print("ID - Start") 
        self.player_one_id = None
        self.player_two_id = None
        
        if self.first_players_list != []:
            print("ID - 1")
            for item in self.first_players_list:
                if item.user_round == self.round:
                    if item.user_color[0] < 3 and item.user_color[1] < 3:
                        self.player_one_oponents = item.oponents
                        self.player_one_id = item.user_id 
                        print(self.player_one_id)
                        break
                else:
                    if self.round == len(self.list_of_players):
                        self.next()
                        return 0
        else:
            print("Pusta lista nr 1!") 
            
        if self.second_players_list != []:
            print("ID - 2")     
            for item in self.second_players_list:
                if item.user_round == self.round:
                    self.player_two_oponents = item.oponents
                    if self.player_one_id not in self.player_two_oponents:
                        if item.user_color[0] < 3 and item.user_color[1] < 3:
                            print(self.player_one_oponents)
                            print(self.player_two_oponents)
                            self.player_two_id = item.user_id
                            
                            print(self.player_two_id)
                            break
                    else:
                        if self.round == len(self.list_of_players):
                            self.next()
                            return 0
        else:
            print("Pusta lista nr 2!") 
        print("ID - Koniec") 
        self.next_round()
        
    def next_round(self):
        if self.player_one_id != None and self.player_two_id != None:
            pass
        else:
            self.round += 1;
            print("Trwa runda:", self.round)
            self.create_list("points")
            self.get_id_players()
        self.take_id_and_get_players()
        self.createWidgets()
        self.add_points(ACTIVE)

    def take_id_and_get_players(self):
        print("TAKE ID")
        player = Player
        for player in player._registry:
            if player.user_id == self.player_one_id:
                First_player = player
                self.First_user_name.set(First_player.user_name) 
                print(First_player.user_name)
            else:
                continue
        
        for player in player._registry:
            if player.user_id == self.player_two_id: 
                Second_player = player
                self.Second_user_name.set(Second_player.user_name) 
                print(Second_player.user_name)
            else:
                continue
    
    def create_list(self, user_type):
        i = 0
        self.list_of_players = []
        self.first_players_list = []
        self.second_players_list = []
        self.third_unpaired_list = []
        
        for player in Player._registry:
            self.list_of_players.append(player)
            i +=1
        print("Lista uczestnikow")
        print(self.list_of_players)
        
        if user_type == "points":
            self.list_of_players = sorted(Player._registry, key=lambda player: player.user_points, reverse=True)
        if user_type == "rank":
            self.list_of_players = sorted(Player._registry, key=lambda player: player.user_rank)
        print("Lista posortowana")
        print(self.list_of_players)
        
        i = 0
        number_of_players = int((len(self.list_of_players)))  
                  
        if user_type == "points":
            
            if number_of_players % 2 != 0:
                for item in self.list_of_players:
                    i += 1
                    if i == number_of_players and item.free_point != 1:
                        self.third_unpaired_list.append(item)
                    elif i % 2 == 1 and item.free_point == 1:
                        self.second_players_list.append(item) 
                        item.free_point = 0
                    elif i % 2 == 0 and item.free_point == 1:
                        self.first_players_list.append(item)  
                        item.free_point = 0
                    elif i % 2 == 1:
                        self.second_players_list.append(item) 
                    elif i % 2 == 0:
                        self.first_players_list.append(item) 
 
            else:
                for item in self.list_of_players:
                    i += 1
                    if i % 2 == 1:
                        self.second_players_list.append(item) 
                    elif i % 2 == 0:
                        self.first_players_list.append(item) 
                                    
        if user_type == "rank":
            
            if number_of_players % 2 != 0:
                for item in self.list_of_players:
                    i += 1
                    if i > int(number_of_players/2) and i < int(number_of_players):
                        self.second_players_list.append(item) 
                    elif i <= int(number_of_players/2):
                        self.first_players_list.append(item)  
                    else:
                        self.third_unpaired_list.append(item)  
            else:
                for item in self.list_of_players:
                    i += 1
                    if i > int(number_of_players/2):
                        self.second_players_list.append(item) 
                    else:
                        self.first_players_list.append(item) 
                                
        print("Lista podzielona")
        print("Lista nr 1")
        print(self.first_players_list)  
        print("Lista nr 2") 
        print(self.second_players_list)
        print("Lista nr 3 (nie ma pary)") 
        print(self.third_unpaired_list)
