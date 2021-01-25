################################################
###### Time Last 3 Months Query ################
###### Created by: Nahum Garcia ################
################################################


#################################
###### Imports ##################
#################################

# Sets path to parent folder to allow importing of controller functions
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from toggl_functions import *

import clipboard,shortcuts

#################################
###### Assets ###################
#################################

date_ranges = {}

# Generates a list with each since date for the last 13 weeks
for i in range(13):
	date_ranges[i] = today - datetime.timedelta(days=((i+1)*7))


#################################
###### Query ####################
#################################

completed_counts= {}

# Gathers hour totals for each date range in the date_ranges table, going one value before to get the new until date
# Data is stored into completed counts dictionary with the date index position as the key
for key in date_ranges:
	if key == 0:  # Since the list only contains since dates, for the first date, we use today as the until date
		week_data = get_weekly_data(date_ranges[key].isoformat(),today.isoformat(),headers,params)
		if week_data['total_grand'] is None:
			total_grand = 0
		else:
			total_grand = week_data['total_grand'] / 3600000.000

		completed_counts[key] = total_grand	

	else:
		week_data = get_weekly_data(date_ranges[key].isoformat(),date_ranges[key-1].isoformat(),headers,params)
		if week_data['total_grand'] is None:
			total_grand = 0
		else:
			total_grand = week_data['total_grand'] / 3600000.000

		completed_counts[key] = total_grand	


#################################
###### Prepare Output ###########
#################################

# Gathers completed_counts dictionary and date_range list to create string output to be used in shortcuts to generate chart
results = ''

# Creates comma delimited list of number of weeks (for X axis values)
for i in range(13):
	results = results + str(i) 
	if i < 12: 
		results = results +	',' 

results = results +'\n' # Delimiting different list with new line

# Creates comma delimited list of the total hours (for Y axis values)
for i in range(12,-1,-1):
	results= results +str(completed_counts[i])
	if i > 0: 
		results = results +	','

results = results +'\n' # Delimiting different list with new line

# Creates comma delimited list of strings for each date (for X Axis labels)
for i in range(12,-1,-1):
	results = results + date_ranges[i].strftime("%Y-%-m-%d")
	if i > 0: 
		results = results +	','


# Sets clipboard to final string of results
clipboard.set(results)

# Opens shortcuts to display insert data into Charty shortcuts
shortcuts.open_shortcuts_app()

