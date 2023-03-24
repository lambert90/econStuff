# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:55:37 2022

@author: BUI3LAMBEJ
"""

import requests
import pandas as pd
import io
from datetime import datetime



currentUrl = 'https://www.ons.gov.uk/file?uri=/economy/inflationandpriceindices/datasets/consumerpriceindices/current/mm23.csv'

def extractData(url):
    data = requests.get(url).content

    df = pd.read_csv(io.StringIO(data.decode('utf-8')), low_memory=False)
    releaseDate = df[df.Title == 'Release Date'].iloc[:, 2].values[0]
    releaseDate = datetime.strptime(releaseDate, '%d-%m-%Y')

    

    codeNameMapping = df[df['Title'] == 'CDID']
    codeNameMapping = codeNameMapping.T.reset_index()
    
    df = df[~df['Title'].isin(
        [
         'PreUnit',
         'Unit',
         'Important Notes',
         'Next release',
         'Release Date',
         'CDID'
                    ]
                )]  # remove unnecessary rows
    
    # take first row as headers
    codeNameMapping.columns = codeNameMapping.iloc[0]
    codeNameMapping = codeNameMapping[1:]
    codeNameMapping.to_csv('codeNameMapping.csv')
    codeNameMapping = dict(zip(codeNameMapping.Title, codeNameMapping.CDID))

    colsToMelt = df.columns.drop('Title')

    df = pd.melt(df, id_vars=['Title'], value_vars=colsToMelt, var_name='type', value_name='value')
    df.rename(columns={'Title': 'period'}, inplace=True)
    df['Code'] = df.type.map(codeNameMapping)

    df['releaseDate'] = releaseDate
    df.dropna(subset=['value'], inplace=True)

    return df, codeNameMapping


