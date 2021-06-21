import mss, datetime, os, win32clipboard
from io import BytesIO
from PIL import Image

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

directory = 'C:\\Screenshots\\'
os.makedirs(directory, exist_ok=True) 
date_string = datetime.datetime.now().strftime("%d%m%Y_%H_%M_%S_%f")
output_filename = directory + date_string + '.jpeg'


def get_data_from_image(filename):
    image = Image.open(filename)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    return data


with mss.mss() as mss_instance:
    mss_instance.shot(output=output_filename)
    data = get_data_from_image(output_filename)
    send_to_clipboard(win32clipboard.CF_DIB, data)
