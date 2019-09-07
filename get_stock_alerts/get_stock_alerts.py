from yahoo_fin import stock_info as si
from numpy import around
from win10toast import ToastNotifier
import pprint as pp
import time, argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--symbol',
    '-s',
    default='YESBANK.NS',
    help='Symbol name from yahoo finance website Ex: for Yes Bank, YESBANK.NS')

parser.add_argument(
    '--percent',
    '-p',
    default='0.01',
    help='Change in percent, on which price has to be notified')



input_arguments = parser.parse_args()



def ShowNotification(title, description, delay =2):
    toaster = ToastNotifier()
    toaster.show_toast(title, description, icon_path=None, duration=delay, threaded=True)
    while toaster.notification_active(): time.sleep(0.1)
    
    
previous_price = 0
profit = 0
current_price = 0

while True:  
    
    while (True):
        try:
            current_price  = around(si.get_live_price(input_arguments.symbol),2) 
            break
        except:
            print('Unable to get share price from yahoo. Retrying !!!')
        
              
    print (current_price)
    
    if previous_price == 0:
        previous_price = current_price   
        ShowNotification(  str(current_price) ,'Welcome')

    
    #        YESBANK.NS
    change = abs(100*(float(previous_price)-float(current_price))/float(previous_price) )
    
    if  change >= float(input_arguments.percent):
        previous_price = current_price   
        title = str(current_price)
        description = 'Change : ' + str(around(change,2))    
        ShowNotification( title ,description)   
    
         
    time.sleep(0.1)
    
    


#print(si.get_data(input_arguments.symbol))
#
#pp.pprint(si.get_quote_table(input_arguments.symbol))
#
#pp.pprint(si.get_stats(input_arguments.symbol))
#
#pp.pprint(si.get_holders(input_arguments.symbol))
#
#pp.pprint(si.get_analysts_info(input_arguments.symbol))
#
#pp.pprint(si.get_income_statement(input_arguments.symbol))
#
#pp.pprint(si.get_balance_sheet(input_arguments.symbol))
#
#pp.pprint(si.get_cash_flow(input_arguments.symbol))
        