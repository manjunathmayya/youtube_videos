import win32com.client as win32
import argparse,os

def SendEmail(emailAddress, subject, message):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = emailAddress
    mail.Subject = subject
    message = message.encode("raw_unicode_escape")
    message = message.decode("unicode_escape")
    mail.Body = message
    # Attach a file
    attachment  = os.getcwd() + "\\test_attachment.txt" #Path to attachment.
    mail.Attachments.Add(attachment)    
    mail.Send()

parser = argparse.ArgumentParser()
parser.add_argument(
    '--emailAddress',
    '-e',
    default='xxxx@gmail.com',
    help='Enter email address of the recepient')

parser.add_argument(
    '--subject',
    '-s',
    default='Default Subject',
    help='Enter subject for the email')

parser.add_argument(
    '--message',
    '-m',    
    default='Default message',
    help='Enter message for the email')

args = parser.parse_args()

SendEmail(args.emailAddress, args.subject, args.message)


