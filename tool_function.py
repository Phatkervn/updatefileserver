
from datetime import datetime
import os

def get_day_str():
    current_date = datetime.now()
    day_string = current_date.strftime('%d_%m_%y')
    return day_string

def check_folder(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)