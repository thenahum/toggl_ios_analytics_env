# toggl_ios_analytics_env
An set of functions for use with Pythonista for iOS to access toggl public API (https://github.com/toggl/toggl_api_docs)

## Contents of Repository
* [toggl_fuctions.py](toggl_functions.py) - This file contains basic functions for gathering data. You can use these functions to build out different data outputs for whichever reporting methond you want to use in iOS. 
* [Charty Queries Folder](01-charty_queries) - This folder contains any programs made to gather data to use to build a Charty graph with iOS Shortcuts. Currently it only contains the Time in the Last 3 Months chart.
* [search_entries_program.py](search_entries_program.py) - This file contains the code to run the "Search Entries" shortcuts. 
* [Time_Data_URLS](Time_Data_URLS) - This is a text file used to keep track of the iOS url which can be used to run the code.

## Installation
1. Download repository as a zip file
2. Uncompress zip file and copy folder into Pythonista folder in your iCloud account. 
3. Update credentials.py with your API Token
4. viola! Now you can use the repository to build out your own analysis. 

## Shortcuts Links

Below are the links for shortcuts using this library. Documentation for these will be available over at [codebeast](https://thecodebeast.com) soon.

### Search Entries
[iCloud URL](https://www.icloud.com/shortcuts/30f5faf127b84855b5cc8b65e4e424a8)


### Charty Time Last 3 Months
[iCloud URL](https://www.icloud.com/shortcuts/4215b9aa5d74401fbe9d5264bd39787f) 
