#For more info visit toggl reports documentation: https://github.com/toggl/toggl_api_docs/blob/master/reports.md

import base64

###### Toggl API Token
token='<YOUR API TOKEN>'+':api_token'

###### Define headers and paramaters for Toggl Request 
headers={
    'Authorization':'Basic '+base64.b64encode(token.encode('ascii')).decode("utf-8")}
params={'user_agent':'<YOUR EMAIL ADDRESS>','workspace_id':'<YOUR WORKSPACE ID>'}
