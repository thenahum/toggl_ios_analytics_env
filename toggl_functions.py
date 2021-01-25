
#############################################################
###### Toggl Pythonista Controller Functions v1.2 ###########
###### Created by: Nahum Garcia #############################
#############################################################


#################################
###### Imports ##################
#################################

import requests
import json
import datetime
from credentials import headers,params


#################################
###### Assets ###################
#################################

##### Get Today
today = datetime.datetime.now()


#################################
###### Functions ################
#################################


"""
Get Weekly Data
Objective: Define function to get raw summary data for any specified window of time
Output: raw json output from toggls summary API (https://github.com/toggl/toggl_api_docs/blob/master/reports.md)

Notes: 
start and end dates need to be passed through in iso format

"""
def get_weekly_data(start,end,headers,params):							
    url='https://toggl.com/reports/api/v2/summary'
    params['since']=start
    params['until'] = end
    response=requests.get(url,headers=headers,params=params).json()
    return response


"""
Subtract Weeks
Objective: Easy way to get start and end date for any number of weeks until today
Output: duple with first value as since date, and second value as until date

Notes: 
Weeks should be an integer

"""
def subtract_weeks(weeks):
	until_calculation = weeks * 7
	until_value = datetime.datetime.now() 
	since_value = datetime.datetime.now() - datetime.timedelta(days = until_calculation)
	return since_value.isoformat(), until_value.isoformat()


"""
Get Last x Weeks Entries
Objective: Get all the entries for any number of weeks until today
Output: List with a dictionary for each entry with the following values: Project, Entry Name, and total time for entry in hours

Notes: 
Weeks should be an integer

"""
def get_last_x_weeks_entries(weeks):
	start, end = subtract_weeks(weeks)
	raw_data = get_weekly_data(start,end,headers,params)

	clean_data_entries = []
	
	for project in raw_data['data']:
		for task in project['items']:
			data_to_append_entries = {'project': project['title']['project']
										,'entry': task['title']['time_entry']
										, 'time': task['time'] / 3600000.000}

			clean_data_entries.append(data_to_append_entries)

	return clean_data_entries


"""
Search Entries
Objective: Get all the entries that match an input search term for any number of weeks until today
Output: A filterd list with a dictionary for each entry that contains search term with the following values: Project, Entry Name, and total time for entry in hours

Notes: 
Weeks should be an integer

"""
def search_entries(search_term, weeks):
	test_list = get_last_x_weeks_entries(weeks)

	filtered_entries= [sub for sub in test_list if search_term.lower() in sub['entry'].lower()]

	return filtered_entries


"""
Pretty Print Entries
Objective: Print entries in a nice way for shortcuts to display in an alert
Output: A string with total time listed on top, and entries below seperated by new lines

Notes: 
Entries should be a list with a dictionary for each entry with the following values: Project, Entry Name, and total time for entry in hours

"""
def pretty_print_entries(entries):	
	text = ''

	total_time = sum(entry['time'] for entry in entries)

	text += 'Total Time: {:.2f}\n\n'.format(total_time)

	for row in entries:
		text += '* {project}, {entry}, {time:.2f}m\n'.format(**row)


	return text		

def get_today_date():
	return today


