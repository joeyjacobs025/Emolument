# -*- coding: utf-8 -*-
"""
Emolument 1

"""

# modules
import yfinance as yf
import numpy as np
import pandas as pd 
import datetime
from datetime import datetime
from datetime import timedelta
import operator

stocks = ['AOS',
"	ABT	",
"	ABBV	",
"	ABMD	"]

dictionary = {}


for stock in stocks:

    score = 0

    stock_data = yf.Ticker(stock)

    
    # # compares P/E ratios by sector
    stockSector = stock_data.info['sector']
    stockPE = stock_data.info['forwardPE']
    
    # P/E ratios
    consumerd_PE = 22.914
    comm_PE = 17.13
    consumers_PE = 19.80
    energy_PE = 10.24
    financials_PE = 12.55
    healthcare_PE = 22.32
    industrials_PE = 18.84
    infoTech_PE = 24.40
    materials_PE = 8.19
    realEstate_PE = 21.74
    utilities_PE = 21.99
    
    margin_low = 0.9
    margin_high = 1.1
    
    if stockSector == 'consumer discretionary':  
        if consumerd_PE*margin_low < stockPE: 
            if stockPE < consumerd_PE*margin_high:
                score = score + 10
        
    if stockSector == 'communication services':
        if comm_PE*margin_low < stockPE:
            if stockPE < comm_PE*margin_high :
                score = score + 10
     
    if stockSector == 'consumer staples':
        if consumers_PE*margin_low < stockPE:
            if stockPE < consumers_PE*margin_high:
                score = score + 10
    
    if stockSector == 'energy':
        if energy_PE*margin_low < stockPE:
            if stockPE < energy_PE*margin_high:
                score = score + 10
    
    if stockSector == 'financials':
        if financials_PE*margin_low < stockPE:
            if stockPE < financials_PE*margin_high:
                score = score + 10
    
    if stockSector == 'healthcare':
        if healthcare_PE*margin_low < stockPE:
            if stockPE < healthcare_PE*margin_high:
                score = score + 10
    
    if stockSector == 'industrials':
        if industrials_PE*margin_low < stockPE:
            if stockPE < industrials_PE*margin_high:
                score = score + 10
    
    if stockSector == 'information technology':
        if infoTech_PE*margin_low < stockPE:
            if stockPE < infoTech_PE*margin_high:
                score = score + 10
    
    if stockSector == 'materials':
        if materials_PE*margin_low < stockPE:
            if stockPE < materials_PE*margin_high:
                score = score + 10
    
    if stockSector == 'real estate':
        if realEstate_PE*margin_low < stockPE:
            if stockPE < realEstate_PE*margin_high:
                score = score + 10
    
    if stockSector == 'utilities':
        if utilities_PE*margin_low < stockPE:
            if stockPE < utilities_PE*margin_high:
                score = score + 10
    
        
    # # Beta difference
    stockBeta = stock_data.get('beta')
    print(stockBeta)
    if(stockBeta < 1.5):
        score += 5
    if(stockBeta < 1):
        score += 2
    if(stockBeta > 2):
        score -= 3

   
    result = {**dictionary, **{stock: score}}  
    print(result)
    

maximum = max(result, key=result.get(0))
print(maximum)


