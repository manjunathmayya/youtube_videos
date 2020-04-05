import webbrowser,sys,os

page_to_open   = ''
url            = 'www.google.com'
argumentcount  = len(sys.argv)
    
if argumentcount > 1:
        page_to_open = sys.argv[1].strip().lower()

filename = 'links.csv'
file = open(filename,"r")
links_data = file.readlines()

for link in links_data:
    data = link.split(',')    
    if page_to_open in data[0].strip().lower():
        url = data[1].strip()
        break 
file.close()
    
webbrowser.open_new_tab(url)
sys.exit()
