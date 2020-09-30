import gspread
from gspread import utils
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import os

"""
gspread API docs
https://gspread.readthedocs.io/en/latest/api.html#exceptions

more examples of gspread commands
https://gspread.readthedocs.io/en/latest/user-guide.html

don't forget to share the spreadsheet file with the client email in swe_points_tracker_secret.json,
or you'll get a spreadsheet not found error.
Read the docs if you're having issues
"""
DIRNAME = os.path.dirname(__file__)

pp = pprint.PrettyPrinter()
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(DIRNAME, 'swe_points_tracker_secret.json'), scope)
client = gspread.authorize(creds)
# you don't need to mess with anything above

# get_worksheet() is ordinal and starts at 0
points_sheet = client.open('fall_2020_member_list').get_worksheet(0)
