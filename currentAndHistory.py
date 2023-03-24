# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:17:30 2022

@author: BUI3LAMBEJ
"""


import extractFromONS


currentDF, codeNameMapping = extractFromONS.extractData(extractFromONS.currentUrl)

baseURL = 'https://www.ons.gov.uk/file?uri=/economy/inflationandpriceindices/datasets/consumerpriceindices/current/previous/vENTERVERSION/mm23.csv'

versionHistory = [i for i in range(1,88)]

versionHistory = [baseURL.replace('ENTERVERSION', str(i)) for i in versionHistory]

df, codeNameMapping = extractFromONS.extractData(versionHistory[0])

currentDF.to_csv('a.csv')