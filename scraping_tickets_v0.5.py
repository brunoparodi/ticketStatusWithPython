##'~~~~~~~~~~~~~~~~')
##'by Bruno Parodi ')
##'~~~~~~~~~~~~~~~~')

from bs4 import BeautifulSoup
from os.path import expanduser
import platform, os, requests

class userConfig():
    #print user OS (Linux for Linux, Darwin for Mac and Windows for Windows)
    def user_os(self):
        return platform.system()
    #get the user home folder (C:\Users\name)
    def home_folder(self):
        home = expanduser('~')
        return home
    #validate the split folder
    def split_folder_validator(self):
        if os.path.exists(self.split_ticket_folder()) == False:
            return ('Split ticket folder not found')
        else:
            True
    #return a list of all split tickets on folder
    def all_split_tickets(self):
        folder = os.listdir(self.split_ticket_folder())
        return folder
    #return a list of split ticket url
    def split_ticket_url(self):
        stu = []
        for split in self.all_split_tickets():
            stu.append(ticket.explorer_url(ticket) + split)
        return stu
    #complete split ticket folder
    def split_ticket_folder(self):
        complete_folder = user.home_folder() + ticket.default_split_folder(ticket)
        return complete_folder

class ticket():
    def __init__(self,url):
        self.url = url
    #default split ticket folder
    def default_split_folder(self):
        dsf = ('\.splitticketbuyer\data\sessions')
        return dsf
    #return a default Decred block explorer
    def explorer_url(self):
        eurl = ('https://explorer.dcrdata.org/tx/')
        return eurl
    #request info from url
    def page(self):
        page = requests.get(self.url)
        return BeautifulSoup(page.content, 'html.parser')
    #return ticket status
    def status(self):
#        print(self.page().find_all('td'))
        return (self.page().find_all('td')[9].get_text().split()[0].lower())
    # return ticket data
    def data(self):
        if self.status() == 'live':
            return (self.page().find_all('td')[3].get_text().split()[0])
        elif self.status() == 'voted':
            return (self.page().find_all('td')[3].get_text().split()[0])
        elif self.status() == 'immature':
            return (self.page().find_all('td')[3].get_text().split()[0])
    def print(self, x):
        print(x)
        print('Ticket data: ', ticket(x).data())
        print('Status     : ', ticket(x).status())
        print('')

print('\n\n\n')
print('________________________________________________________')
print('| Check files in folder \.splitticketbuyer\data\sessions|')
print('| and get online status of split ticket.          Enjoy.|')
print('|_______________________________________________________|\n')

user = userConfig()

# toprint = input('Press "A" to all;\n'
#                 'Press "V" to show Voted;\n'
#                 'Press "I" to show Immature;\n'
#                 'Press "L" to show Live;\n'
#                 'Press "O" to show live and immature.\n'
#                 'Press: ').lower()


total = immature = voted = live = 0

for x in user.split_ticket_url():
    ticket(x).print(x)
    if ticket(x).status() == 'live':
        live += 1
    elif ticket(x).status() == 'voted':
        voted += 1
    elif ticket(x).status() == 'immature':
        immature += 1
    total += 1
print(f'Resumo\nTotal: {total}\nVoted: {voted}\nLive: {live}\nImmature: {immature}')

input('\nPress ENTER to close.')