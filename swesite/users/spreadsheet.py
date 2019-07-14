import gspread
from gspread import utils
from oauth2client.service_account import ServiceAccountCredentials
import pprint
from users.member import Member

"""
gspread API docs
https://gspread.readthedocs.io/en/latest/api.html#exceptions

more examples of gspread commands
https://gspread.readthedocs.io/en/latest/user-guide.html
"""

pp = pprint.PrettyPrinter()
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('swe_points_tracker_secret.json', scope)
client = gspread.authorize(creds)
points_sheet = client.open('Volunteer_point_tracker').sheet1
# you don't need to mess with anything above


"""
{'1st general meeting ': 0,
 'BASF': 0,
 'Bake Sale ': 0,
 'Big Event Weekend': 0,
 'Cajun GBN ': 0,
 'E&T': '',
 'Election Mtg. ': 0,
 'Fall 2019 1st Mtg': '',
 'First Name ': 'Katelyn',
 'King Cake': 0,
 'Kona Ice- End of Spring 2019': 0,
 'Last Name ': 'Loupe',
 'Science Olympiad': 0,
 'Total': 0,
 'Westlake': 0,
 'fundraising 1 ': '',
 'fundraising 2': '',
 'fundraising 3': '',
 'fundraising 4': '',
 'fundraising 5': '',
 'high school event ': '',
 'industrial tour ': '',
 'info session ': '',
 'interview and resume ': '',
 'other': '',
 'other ': '',
 'second Mtg ': ''}
 
 all_events is a list of dictionaries that holds all spreadsheet info in the form above. 
 Each members has their own dict in the list 
 You can do pp.pprint(all_events) to see what the whole thing looks like
"""

all_events = points_sheet.get_all_records()

all_swe_members = []


"""
 iterate over the list of dicts:
    make a new member object and put it into the members list
    pop the first/last/total key/value paris from dict[i]
    put the remaining dict (which is all the events) in the member object as a dict of events
"""
for i in range(len(all_events)):
    all_swe_members.append(Member(all_events[i].get('First Name'),
                                  all_events[i].get('Last Name'),
                                  all_events[i].get('Total')))

    all_events[i].pop('First Name')
    all_events[i].pop('Last Name')
    all_events[i].pop('Total')

    all_swe_members[i].set_events(all_events[i])


for member in all_swe_members:
    if member.last_name == "McCrary":
        print(member.__str__())
        print(member.get_events_attended())

"""
Testing - Ignore
for member in all_swe_members:
    print(member.__str__())
    print(member.events.items())

print(all_swe_members[10].get_events_attended())
"""
