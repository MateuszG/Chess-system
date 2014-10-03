import tkinter as tk
from tkinter import *
from tkinter import ttk
from Rot import *
from Player import Player

class Results(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.Res_frame = ttk.Frame(self, padding="6 12 12 12")
        self.Res_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.Res_frame.columnconfigure(0, weight=1)
        self.Res_frame.rowconfigure(0, weight=1)
        self.scrollbar = Scrollbar(self.Res_frame)
        self.sort_list = []
        self.Buchholz_list = []
        self.Buchholz_list_to_add = []
        self.players_list = Listbox(self.Res_frame, width = 55, height = 10, yscrollcommand=self.scrollbar.set, 
                                    exportselection=0)
        self.scrollbar.config(command=self.players_list.yview)

        self.pack()
        self.createWidgets()

    def __del__(self, master=None):
        tk.Frame.__init__(self, master)

    def next(self):
        root2.destroy()
        quitProgram()

    def quit(self):
        root3.destroy
        quitProgram()
        
    def Buchholz(self):
        numbers_players_of_same_points = 0
        max_point = self.sort_list[0].user_points
        for item in self.sort_list:
            if item.user_points == max_point:
                numbers_players_of_same_points += 1
            
        if numbers_players_of_same_points > 1:
            print("Zastosowano Buchholz")
            for item in self.sort_list:
                if item.user_points == max_point:
                    self.Buchholz_list.append(item)
            print(self.Buchholz_list)
            for item in self.Buchholz_list:
                oponents_id = item.oponents
                for oponents in oponents_id:
                    user_id = oponents
                    player = Player
                    for player in player._registry:
                        if player.user_id == user_id:
                            self.Buchholz_list_to_add.append([item.user_id, player.user_points]) 
                            print("Graczowi", item.user_name, " (", item.user_points ," pkt)",
                                  "przyznano: ", player.user_points, " punktow gracza ", player.user_name)
            
            for player in player._registry:
                for item in self.Buchholz_list_to_add:
                    if player.user_id == item[0]:
                        player.user_points += item[1]

    def createWidgets(self):
        i = 0
        self.sort_list = sorted(Player._registry, key=lambda player: player.user_points, reverse=True)
        print("Lista posortowana")
        print(self.sort_list)
        self.Buchholz()
        self.sort_list = sorted(Player._registry, key=lambda player: player.user_points, reverse=True)
        print("Lista posortowana po Buchholz")
        print(self.sort_list)
        for item in self.sort_list:
            len_of_name = len(item.user_name)
            user_space = 20 - len_of_name
            user_line =" "
            for _ in range(user_space):
                user_line +=" "
            user_line = item.user_name + str(user_line) + str(item.user_points) 
            user_line += str(" pkt, ") + str(" rozegranych rund: ") + str(item.user_round - 1) 
            self.players_list.insert(i, user_line)
            i += 1
            
        List_of_users = ttk.Label(self.Res_frame, text="Wyniki uczestnikow:")
        List_of_users.grid(column=1, row=1, sticky=W)
        
        self.players_list.grid(column=1, columnspan=2, row=2, rowspan = 2, sticky=N, pady=6)
        self.scrollbar.grid(column=3, columnspan=2, row = 2, rowspan = 4, sticky=N, pady = 7, ipady = 55)
        Button_End_Program = ttk.Button(self.Res_frame, text="Zakoncz", command=quitProgram)
        Button_End_Program.grid(column=1, row=5, sticky=W, pady=6, padx=6)
        ttk.Label(self.Res_frame, text="Autor: Mateusz Galganek").grid(column=2, row=5, sticky=E)
