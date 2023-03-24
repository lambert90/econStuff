# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:57:17 2022

@author: BUI3LAMBEJ
"""

import requests
import csv
import pandas as pd
import io
from datetime import datetime

apiLink = 'https://api.beta.ons.gov.uk/v1'

a = requests.get(apiLink + '/datasets', params={'limit': 1000})


cpi = 'https://api.beta.ons.gov.uk/v1/datasets/cpih01/editions'


cpi_json = requests.get(cpi).json()
cpi_items = cpi_json.get('items')[0]
cpi_links = cpi_items.get('links')
cpi_latest_version = cpi_links.get('latest_version')
cpi_latest_url = cpi_latest_version.get('href')

cpi_latest_json = requests.get(cpi_latest_url).json()
download_url = cpi_latest_json.get('downloads').get('csv').get('href')

release_date = cpi_latest_json.get('release_date')
release_date = datetime.strptime(release_date[:10], '%Y-%m-%d')

data = requests.get(download_url).content
df = pd.read_csv(io.StringIO(data.decode('utf-8')))
df.to_csv('cpis.csv')

print(release_date)
#b = requests.get(cpi_latest)
#url = 'https://download.beta.ons.gov.uk/downloads/datasets/cpih01/editions/time-series/versions/25.csv'

# file = requests.get(url)
# content = file.content.decode('UTF-8')
# content = content.splitlines()

# with open('cpi.csv', 'w+', newline='') as f:
    
#     data = content
#     writer = csv.writer(f, delimiter=',')
    
#     for row in content:
#         writer.writerow(row.split(','))
        
        