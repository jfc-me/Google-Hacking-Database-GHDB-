# -*- coding: utf-8 -*-
import re
import bs4
import time
from colors.cor import CYELLOW, CYELLOW2, CBLUE, CWHITE
from connections.connection import Connection

class SelectCategory:

    def category(self, tipoVulne, pesq):
        _conect = Connection()
        _ghdb = 'https://www.exploit-db.com/google-hacking-database/?action=search&ghdb_search_cat_id={}&ghdb_search_text=' + pesq
        _nameanyCategory = ["Any Category", "Footholds", "Files Containing Usernames", "Sensitive Directories",
                            "Web Server Detection", "Vulnerable Files", "Vulnerable Servers", "Error Messages",
                            "Files Containing Juicy Info", "Files Containing Passwords",
                            "Sensitive Online Shopping Info",
                            "Network or Vulnerability Data", "Pages Containing Login Portals",
                            "Various Online Devices", " Advisories and Vulnerabilities", ]
        sorted(_nameanyCategory)
        for lista in range(len(_nameanyCategory)):
            if tipoVulne in _nameanyCategory[lista]:
                print(CYELLOW, "\n[ Selecionado ]", CWHITE, CYELLOW2, _nameanyCategory[lista], " {> ", pesq, " <}", CWHITE)
                ends = _conect.ref = _ghdb.format(lista)
                return ends


    def destintos(self, doork, txt):
        urlFixa = SelectCategory().category(doork, txt)
        newConect = Connection()
        tempo_Inicial = time.time()
        newConect.ref = urlFixa
        files = re.findall('href="(https://www.exploit-db.com/ghdb/(.*?)/)"', newConect.ref)
        x = [i for i in files]
        oquetemLa = Connection()
        for a, b in x:
            oquetemLa.ref = a

            desc = re.compile(r'<td><strong>(.*?)</strong>(.*?)</td>', re.UNICODE)
            data = re.compile(r'<td><strong>(.*?)</strong>: <time>(.*?)</time></td>', re.UNICODE)
            inf1 = desc.search(str(oquetemLa.ref))
            inf2 = data.search(str(oquetemLa.ref))

            listaTitulo = []
            listaInformacao = []

            soup = bs4.BeautifulSoup(oquetemLa.ref, 'lxml')

            for ponteiroTi in soup.select("tbody tr td strong "):
                listaTitulo.append(ponteiroTi.text)
            for ponteiroIn in soup.select("tbody tr td a "):
                listaInformacao.append(ponteiroIn.text)

            GHDB_ID = listaInformacao[0]
            GHDB_ID_C = listaTitulo[1]
            Author = listaInformacao[2]
            Author_C = listaTitulo[5]

            description = """{}..................................................................................................................................{}
{}{}{}  {}                                                           
{}{}{} : {}{}:..........   .   ..... .  ............ . . . . . . . . . . . . .................. . .  ....:{}{}{} {}:{}
{}{}{}:  {} 
{}..................................................................................................................................{}""".format(
                           CBLUE, CWHITE, CYELLOW2, inf1.group(1), CWHITE, inf1.group(2),
                           CYELLOW2, Author_C, CWHITE, Author.strip("\n").replace(" ", ""),
                           CBLUE, CWHITE,
                           CYELLOW2, GHDB_ID_C,CWHITE,
                           GHDB_ID.strip("\n").replace(" ", ""),
                           CYELLOW2, inf2.group(1), CWHITE, inf2.group(2),
                           CBLUE, CWHITE)
            print(description)

            tempo_final = time.time()
            tempo_percorrido = tempo_final - tempo_Inicial
            print("{0:.3} seg".format(tempo_percorrido))
