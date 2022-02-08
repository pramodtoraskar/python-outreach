# outreach
Python wrapper functions for Outreach APIs, tested with Python 3.8 - 3.9.

This python client wrapper helps connects outreach API by authentication flow, any request use two distinct
sets of credentials. The API key and secret identify the requester.

## Quick Start

1. Installation
   1. Dependent libraries The following dependent libraries were installed.
   > pip install singer-python
   > pip install requests
   2. Install from pypi using pip
   > pip install python-outreach
   3. Clone this repository, and then install using setup.py. Recommend using a virtualenv: 
   ```bash
   > virtualenv -p python3 venv
   > source venv/bin/activate
   > python setup.py install
   OR
   > cd .../python-outreach
   > pip install .
   ```
2. Set the environment variables, `refresh_token`, `redirect_uri`, `client_id`, and `client_secret` 
are the credentials need to set for outreach client. More details for Authentication is [here](https://api.outreach.io/api/v2/docs#authentication)
    ```dotenv
   export client_id=<Application_Identifier>
   export client_secret=<Application_Secret>
   export redirect_uri=<Application_Redirect_URI>
   export refresh_token=<Refresh_Token>
   ```                                 
3. To work with the API client, we start with the `OutreachClient` class:
   ```python    
   connect_config = {
           'user_agent': '',
           'client_id': environ['OUTREACH_CLIENT_ID'],
           'client_secret': environ['OUTREACH_CLIENT_SECRET'],   
           'redirect_uri': environ['OUTREACH_REDIRECT_URI'],
           'refresh_token': environ['OUTREACH_REFRESH_TOKEN'],
           'quota_limit': 9999
       }
   or_client = OutreachClient(connect_config)
   ```
4. To Fetch prospects by email address or prospect id use 
   ```python
   or_client.get(path=f'prospects?filter[emails]={:email}')
   # or
   or_client.get(path=f'prospects/{:id}')
   ```
5. To Create new prospects or update existing
   ```python
    # To Create New  
    or_client.post(path=f'prospects',
                              json={
                                  "data": {
                                      "type": "prospect",
                                      "attributes": {:Prospect_rec_attributes key:value}
                                  }
                              })

    # For update
    or_client.update(path=f'prospects/{prospect_id}',   
                             json={
                                 "data": {
                                     "type": "prospect",
                                     "id": int(prospect_id),
                                     "attributes": prospect_rec
                                 }
                             })  
   ```

### Feature requests
To request a new feature in this package, please open a new issue on the Github repo. To report problems, please open a new issue on the Github repo.

### Contribution
Pull requests are welcomed! All pull requests must have the following:
- OK global score from pylint using PEP8 standards
  - This one is a bit loose for now given that the old code is still a mess; once the renovation is complete, we will implement a minimum passing pylint score
- Passing unit tests (nosetests) that cover the included use cases and pass the current tox config