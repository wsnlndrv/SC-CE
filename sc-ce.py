#!/usr/bin/python
# -*- coding: utf-8; -*-

# Para usarlo en wintendows hay que suprimir la primera linea.
# Y la linea 30, cambiar "clear" por "cls"

import threading, time, a2s, os, sys, datetime
import pandas as pd

nombre_servidor = "  Nombre del servidor"
filigrana = "**********************************"
IPDS = "0.0.0.0"
PUERTEISHON = 27015

class Base(threading.Thread):
    def __init__(self):
        self._timer_runs = threading.Event()
        self._timer_runs.set()
        super().__init__()
        
    def iniciar(self):
        while self._timer_runs.is_set():
            self.timer()
            time.sleep(self.__class__.interval)

    def parar(self):
        self._timer_runs.clear()
    
    def mostrar(self):
        os.system('clear')
        print(filigrana+"\n"+nombre_servidor+"\n"+filigrana)
        IP = (IPDS, PUERTEISHON)
        df = pd.DataFrame(a2s.players(IP))
        
        try:
            columna1 = df.iloc[:,1]
            print("\n".join(usuario[1] for usuario in columna1))
        except IndexError:
            print("Nadie conectado.")

class Consultar(Base):
    interval = 60
    def timer(self):
        base = Base()
        base.mostrar()

consultar = Consultar()
consultar.iniciar()
consultar.parar()
