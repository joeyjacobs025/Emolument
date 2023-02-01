# -*- coding: utf-8 -*-
"""
Emolument 2

"""


# modules
#import beautifulSoup4 as bs4
import yfinance as yf
#import tensorflow as tf
import numpy as np
import pandas as pd 
import datetime
from datetime import datetime
from datetime import timedelta
import operator

stocks = ['AOS',
"	ABT	",
"	ABBV	",
"	ABMD	",
"	ACN	"]


dictionary = {}


for stock in stocks:

    score = 0
    

    closeScore = 0
    openScore = 0
    lowScore = 0
    highScore = 0

    

    stock_data = yf.Ticker(stock).info


    # get date
    today = datetime.today()

    datedListThirty = today - timedelta(days=30)


    stock_price = yf.download(stock, start=datedListThirty, end=today, group_by="ticker") 
    close_df1 = stock_price.drop(columns=['Open','High','Low','Adj Close','Volume'])

    close_df2 = close_df1.values.tolist()

    for i in range(len(close_df2)):
        if close_df2[i] > close_df2[i-1]:
            closeScore = closeScore + 1
        else:
            closeScore = closeScore - 1
            


    open_df1 = stock_price.drop(columns=['Close','High','Low','Adj Close','Volume'])
       
    open_df2 = open_df1.values.tolist()

    for i in range(len(close_df2)):
        if open_df2[i] > open_df2[i-1]:
            openScore = openScore + 1
        else:
            openScore = openScore - 1
            

       

    low_df1 = stock_price.drop(columns=['Close','Open','High','Adj Close','Volume'])

    low_df2 = low_df1.values.tolist()

    for i in range(len(low_df2)):
        if low_df2[i] > low_df2[i-1]:
            lowScore = lowScore + 1
        else:
            lowScore = lowScore - 1
            



    high_df1 = stock_price.drop(columns=['Close', 'Open', 'Low', 'Adj Close', 'Volume'])

    high_df2 = high_df1.values.tolist()

    for i in range(len(high_df2)):
        if high_df2[i] > high_df2[i-1]:
            highScore = highScore + 1
        else:
            highScore = highScore - 1
            
    
    
    # # compares P/E ratios by sector
    stock_data = yf.Ticker(stock)
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
