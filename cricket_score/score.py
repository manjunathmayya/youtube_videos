import requests, argparse
from lxml.html import fromstring
from win10toast import ToastNotifier
import time
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument(
    '--url',
    '-url',    
    default='https://www.espncricinfo.com/series/8050/game/1203608/bengal-vs-odisha-2nd-quarter-final-ranji-trophy-2019-20' ,
    help='url from espncricinfo.com of match')

args = parser.parse_args()

left = '('
right = ' ov'
PreviousRuns = 0;
PreviousWickets = 0;        
previous_overs = 0
commentary = ''
score = ''
overs = ''
ignore_first = True

def GetScore():
    page = requests.Session().get(args.url)
    score = fromstring(page.content).findtext('.//title').split('- Live')[0]
    soup = BeautifulSoup(page.text,'lxml')
    commentary = soup.find("div", {"class": "commentary-item"})
    description = commentary.find("div", {"class": "description"})  
    
    return score, description.text.strip() if description is not None else ''


def ShowNotification(title, score, delay =5):
    toaster = ToastNotifier()
    toaster.show_toast(title, score, icon_path=None, duration=delay, threaded=True)
    while toaster.notification_active(): time.sleep(0.1)
    
def printSummary():
    print('\n', commentary + '\n' +score + ' ' + str(overs))
    #ShowNotification('Test !!!',score+ ' ' + str(overs))
    
while (True): 
    time.sleep(3)
    summary, commentary = GetScore()         
    score = summary.split(' ')[1]
    Runs = score.split('/')[0]
    Wickets = score.split('/')[1]   
    
    overs = float(summary[summary.index(left)+len(left):summary.index(right)])    
    
    if (int(Runs)-int(PreviousRuns)) == 4:
        ShowNotification('Four !!!',commentary + '\n' +score)
    elif (int(Runs)-int(PreviousRuns)) == 6:
        ShowNotification('Six !!!',score)
        
    if (int(Runs)-int(PreviousRuns)) >= 1 or overs > previous_overs:
        printSummary()  
    
    if int(Wickets) - int(PreviousWickets) == 1 and not ignore_first:            
        ShowNotification('Wicket!!!',commentary + '\n' + score)      
        printSummary()
        ignore_first = False
        
    
    PreviousRuns = Runs;
    PreviousWickets = Wickets;        
    previous_overs = overs
