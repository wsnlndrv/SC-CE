#!/usr/bin/python
# -*- coding: utf-8; -*-

import a2s, sys, os, re, requests, time

IP = ("x.x.x.x", 28015) #Servidor oficial nºxxxx de Conan Exiles
listado= a2s.players(IP)
print(*listado, sep = "\n")
