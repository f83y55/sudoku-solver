#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tkinter as tk

d = {}
for k in range(9) :
    for l in range(9) :
        d[(k,l)] = list(range(1,10))
ancien = []



class Ihm :
    def __init__(self) :
        self = tk.Tk()
        self.title("Sudoku")
        for k in range(9) :   # Grille
            self.rowconfigure(k, weight=1)
            self.columnconfigure(k, weight=1)

        def parse(event) :
            fw = tuple( map(int,str(self.focus_get())[1:].split(",")) )
            d[fw] = list(map(int,self.db[fw].get("0.0",tk.END)[:-1].split(" ")))
            print(d[fw])
            if len(d[fw])==1 :
                nettoie(fw)
                ancien.append(fw)
            nouveau = []
            for k in range(9) :
                for l in range(9) :
                    if len(d[(k,l)])==1 and (k,l) not in ancien :
                        nouveau.append((k,l))
            while nouveau :
                el = nouveau.pop()
                nettoie(el)
                ancien.append(el)
                for k in range(9) :
                    for l in range(9) :
                        if len(d[(k,l)])==1 and (k,l) not in ancien :
                            nouveau.append((k,l))
                        
        def nettoie(fw) :
            for k in range(3*(fw[0]//3),3*(fw[0]//3+1)) :
                for l in range(3*(fw[1]//3),3*(fw[1]//3+1)) :
                    if k != fw[0] and l != fw[1] :
                        for el in list(d[fw]) :
                            if el in d[(k,l)] :
                                d[(k,l)].remove(el)
                        self.db[(k,l)].delete("1.0",tk.END)
                        self.db[(k,l)].insert("1.0",d[(k,l)])
            for k in range(9) :
                l = fw[1]
                if k != fw[0]  :
                    for el in list(d[fw]) :
                        if el in d[(k,l)] :
                            d[(k,l)].remove(el)
                    self.db[(k,l)].delete("1.0",tk.END)
                    self.db[(k,l)].insert("1.0",d[(k,l)])
            for l in range(9) :
                k = fw[0]
                if l != fw[1] :
                    for el in list(d[fw]) :
                        if el in d[(k,l)] :
                            d[(k,l)].remove(el)
                    self.db[(k,l)].delete("1.0",tk.END)
                    self.db[(k,l)].insert("1.0",d[(k,l)])

        self.db = {}
        for k in range(9) :   # Text
            for l in range(9) :
                self.db[(k,l)] = tk.Text(self, name=str(k)+","+str(l), width=20)
                self.db[(k,l)].grid(row=k, column=l, sticky="nsew")
                self.db[(k,l)].bind('<Return>', parse)
                self.db[(k,l)].insert(tk.INSERT, d[(k,l)])
        self.mainloop()




def main(args) : return 0

if __name__ == '__main__' :
    import sys
    Ihm()
    sys.exit(main(sys.argv))
