
#############################################################
###### Search Entries Controller v1.2 #######################
###### Created by: Nahum Garcia #############################
#############################################################


#################################
###### Imports ##################
#################################

from toggl_functions import *

import sys, clipboard,shortcuts

#################################
###### Arguments ################
#################################

search_term = sys.argv[1]
weeks = int(sys.argv[2])

#################################
###### Program ##################
#################################

# Stores into text all the entries with the inputed search term for the last inputed number of weeks (int)
text = pretty_print_entries(search_entries(search_term,weeks))

# Sets clipboard to string output from above
clipboard.set(text)

# Opens shortcuts to display data as an alert
shortcuts.open_shortcuts_app()

