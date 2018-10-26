from scrap_pages.category import SelectCategory


class Main():
    if __name__ == '__main__':
       ops ="""
Any Category
Footholds
Files Containing Usernames
Sensitive Directories
Web Server Detection
Vulnerable Files
Vulnerable Servers
Error Messages
Files Containing Juicy Info
Files Containing Passwords
Sensitive Online Shopping Info
Network or Vulnerability Data
Pages Containing Login Portals
Various Online Devices
Advisories and Vulnerabilities"""
       print(ops)
       ia = SelectCategory()

       dork = input("Doork : ")

       pesquisa = input("Pesquisa : ")
       yy = ia.destintos(dork, pesquisa)

