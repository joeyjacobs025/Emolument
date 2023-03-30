

"""

Emolument 6


The following are comments (thoughts, descriptions, ideas about the code):

Previous 30 closes, highs, lows, opens. volumes
va
Compare the closes --> if a stock on day x closes lower than day x-1. subtract a point 

Compare the opens --> if a stock on day x opens lower than day x-1. adds a point 

Compare the lows --> if a stock low on day x is less than stock low on day x-1, subtract a point

Compare the highs --> if a stock high on day x is more than stock high on day x-1. add a point

first 5 days average of volumes (days x-30 -> x-25) compared to last 5 days average of volumes (days x-5 -> x)

P/E ratio : P/E ratios by sector 
good P/E's by sector
- energy
- materials
- financials
- real estate
- healthcare
- utilities
- industrials
- IT
- consumer staples
- consumer discretionary
- industrials

Beta difference : if under 1.5, add 5 points, if under 1, add 7 points, if over 3, subtract 3 points

52 week range : if stock price current is in the ____ percentile of the 52 wk range, add ___
*5 - 10
*12 - 8
*19 - 6
*26 - 2
*33 - 0
*40 - -5


    
Projected 1 yr target: if 1 year target is 10% over the average of the 30 day previous close, add 8 points 



Threshold between, consider and pitch -- 35 points

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
from operator import itemgetter

stocks = ['AOS',
"	ABT	",
"	ABBV	",
"	ABMD	",
"	ACN	",
"	ATVI	",
"	AAP	",
"	AMD	",
"	AFL	",
"	A	",
"	APD	",
"	AKAM	",
"	ALK	",
"	ALB	",
"	ARE	",
"	ALGN	",
"	ALLE	",
"	LNT	",
"	ALL	",
"	GOOG	",
"	GOOGL	",
"	MO	",
"	AMZN	",
"	AMCR	",
"	AEE	",
"	AAL	",
"	AEP	",
"	AXP	",
"	AIG	",
"	AMT	",
"	AWK	",
"	AMP	",
"	ABC	",
"	AME	",
"	AMGN	",
"	APH	",
"	ADI	",
"	ANSS	",
"	ANTM	",
"	AON	",
"	APA	",
"	AAPL	",
"	AMAT	",
"	APTV	",
"	ADM	",
"	ANET	",
"	AJG	",
"	AIZ	",
"	T	",
"	ATO	",
"	ADSK	",
"	ADP	",
"	AZO	",
"	AVB	",
"	AVY	",
"	BKR	",
"	BLL	",
"	BAC	",
"	BBWI	",
"	BAX	",
"	BDX	",
"	BRK.B	",
"	BBY	",
"	BIIB	",
"	BIO	",
"	TECH	",
"	BLK	",
"	BA	",
"	BKNG	",
"	BWA	",
"	BXP	",
"	BSX	",
"	BMY	",
"	AVGO	",
"	BR	",
"	BRO	",
"	BF.B	",
"	CHRW	",
"	CDNS	",
"	CZR	",
"	CPB	",
"	COF	",
"	CAH	",
"	KMX	",
"	CARR	",
"	CTLT	",
"	CAT	",
"	CBOE	",
"	CBRE	",
"	CDW	",
"	CE	",
"	CNC	",
"	CNP	",
"	CDAY	",
"	CERN	",
"	CF	",
"	CRL	",
"	SCHW	",
"	CHTR	",
"	CVX	",
"	CMG	",
"	CB	",
"	CHD	",
"	CI	",
"	CINF	",
"	CTAS	",
"	CSCO	",
"	C	",
"	CFG	",
"	CTXS	",
"	CLX	",
"	CME	",
"	CMS	",
"	KO	",
"	CTSH	",
"	CL	",
"	CMCSA	",
"	CMA	",
"	CAG	",
"	COP	",
"	ED	",
"	STZ	",
"	CPRT	",
"	GLW	",
"	CTVA	",
"	COST	",
"	CTRA	",
"	CCI	",
"	CSX	",
"	CMI	",
"	CVS	",
"	DHI	",
"	RCL	",
"	DHR	",
"	DRI	",
"	DVA	",
"	SRE	",
"	DE	",
"	DAL	",
"	XRAY	",
"	DVN	",
"	DXCM	",
"	FANG	",
"	DLR	",
"	DFS	",
"	DISCA	",
"	DISCK	",
"	DISH	",
"	DG	",
"	DLTR	",
"	D	",
"	DPZ	",
"	DOV	",
"	DOW	",
"	DTE	",
"	DUK	",
"	DRE	",
"	DD	",
"	DXC	",
"	EMN	",
"	ETN	",
"	EBAY	",
"	ECL	",
"	EIX	",
"	EW	",
"	EA	",
"	LLY	",
"	EMR	",
"	ENPH	",
"	ETR	",
"	EOG	",
"	EPAM	",
"	EFX	",
"	EQIX	",
"	EQR	",
"	ESS	",
"	EL	",
"	ETSY	",
"	RE	",
"	EVRG	",
"	ES	",
"	EXC	",
"	EXPE	",
"	EXPD	",
"	EXR	",
"	XOM	",
"	FFIV	",
"	FDS	",
"	FAST	",
"	FRT	",
"	FDX	",
"	FIS	",
"	FITB	",
"	FRC	",
"	FE	",
"	FISV	",
"	FLT	",
"	FMC	",
"	F	",
"	FTNT	",
"	FTV	",
"	FBHS	",
"	FOX	",
"	FOXA	",
"	BEN	",
"	FCX	",
"	GPS	",
"	GRMN	",
"	IT	",
"	GNRC	",
"	GD	",
"	GE	",
"	GIS	",
"	GM	",
"	GPC	",
"	GILD	",
"	GPN	",
"	GL	",
"	GS	",
"	HAL	",
"	HIG	",
"	HAS	",
"	HCA	",
"	PEAK	",
"	HSIC	",
"	HES	",
"	HPE	",
"	HLT	",
"	HOLX	",
"	HD	",
"	HON	",
"	HRL	",
"	HST	",
"	HWM	",
"	HPQ	",
"	HUM	",
"	HII	",
"	IEX	",
"	IDXX	",
"	INFO	",
"	ITW	",
"	ILMN	",
"	INCY	",
"	IR	",
"	INTC	",
"	ICE	",
"	IBM	",
"	IFF	",
"	IP	",
"	IPG	",
"	INTU	",
"	ISRG	",
"	IVZ	",
"	IPGP	",
"	IQV	",
"	IRM	",
"	JBHT	",
"	SJM	",
"	JKHY	",
"	J	",
"	JNJ	",
"	JCI	",
"	JPM	",
"	JNPR	",
"	K	",
"	KEYS	",
"	KMB	",
"	KIM	",
"	KMI	",
"	KLAC	",
"	KR	",
"	LHX	",
"	LH	",
"	LRCX	",
"	LW	",
"	LVS	",
"	LDOS	",
"	LNC	",
"	LIN	",
"	LYV	",
"	LKQ	",
"	LMT	",
"	L	",
"	LOW	",
"	LUMN	",
"	LYB	",
"	MTB	",
"	MRO	",
"	MPC	",
"	MKTX	",
"	MAR	",
"	MMC	",
"	MLM	",
"	MAS	",
"	MA	",
"	MTCH	",
"	MKC	",
"	MCD	",
"	MCK	",
"	MDT	",
"	MRK	",
"	FB	",
"	MET	",
"	MTD	",
"	MGM	",
"	MCHP	",
"	MU	",
"	MSFT	",
"	MAA	",
"	MRNA	",
"	MHK	",
"	TAP	",
"	MDLZ	",
"	MPWR	",
"	MNST	",
"	MCO	",
"	MS	",
"	MOS	",
"	MSI	",
"	MSCI	",
"	NDAQ	",
"	NTAP	",
"	NFLX	",
"	NWL	",
"	NEM	",
"	NWSA	",
"	NWS	",
"	NEE	",
"	NLSN	",
"	NKE	",
"	NI	",
"	NTRS	",
"	NOC	",
"	NLOK	",
"	NCLH	",
"	NRG	",
"	NUE	",
"	NVDA	",
"	NVR	",
"	NXPI	",
"	OXY	",
"	ODFL	",
"	OMC	",
"	OKE	",
"	ORCL	",
"	ORLY	",
"	OGN	",
"	OTIS	",
"	PCAR	",
"	PKG	",
"	PH	",
"	PAYX	",
"	PAYC	",
"	PYPL	",
"	PENN	",
"	PNR	",
"	PBCT	",
"	PEP	",
"	PKI	",
"	PFE	",
"	PM	",
"	PSX	",
"	PNW	",
"	PXD	",
"	PNC	",
"	POOL	",
"	PPG	",
"	PPL	",
"	PFG	",
"	PG	",
"	PGR	",
"	PLD	",
"	PRU	",
"	PTC	",
"	PEG	",
"	PSA	",
"	PHM	",
"	PVH	",
"	QRVO	",
"	QCOM	",
"	PWR	",
"	DGX	",
"	RL	",
"	RJF	",
"	RTX	",
"	O	",
"	REG	",
"	REGN	",
"	RF	",
"	RSG	",
"	RMD	",
"	RHI	",
"	ROK	",
"	ROL	",
"	ROP	",
"	ROST	",
"	SPGI	",
"	CRM	",
"	SBAC	",
"	SLB	",
"	STX	",
"	SEE	",
"	NOW	",
"	SHW	",
"	SBNY	",
"	SPG	",
"	SWKS	",
"	SNA	",
"	SEDG	",
"	SO	",
"	LUV	",
"	SWK	",
"	SBUX	",
"	STT	",
"	STE	",
"	SYK	",
"	SIVB	",
"	SYF	",
"	SNPS	",
"	SYY	",
"	TROW	",
"	TTWO	",
"	TPR	",
"	TGT	",
"	TEL	",
"	TDY	",
"	TFX	",
"	TER	",
"	TSLA	",
"	TXN	",
"	TXT	",
"	AES	",
"	BK	",
"	COO	",
"	HSY	",
"	KHC	",
"	TRV	",
"	TMO	",
"	TJX	",
"	TMUS	",
"	TSCO	",
"	TT	",
"	TDG	",
"	TRMB	",
"	TWTR	",
"	TYL	",
"	TSN	",
"	USB	",
"	UDR	",
"	ULTA	",
"	UAA	",
"	UA	",
"	UNP	",
"	UAL	",
"	UPS	",
"	URI	",
"	UNH	",
"	UHS	",
"	VFC	",
"	VLO	",
"	VTR",
"	VRSN",
"	VRSK",
"	VZ",
"	VRTX",
"	VIAC",
"	VTRS",
"	V",
"	VNO	",
"	VMC	",
"	WRB	",
"	GWW	",
"	WBA	",
"	WMT	",
"	DIS	",
"	WM	",
"	WAT	",
"	WEC	",
"	WFC	",
"	WELL",
"	WST	",
"	WDC	",
"	WAB	",
"	WRK	",
"	WY	",
"	WHR	",
"	WMB	",
"	WLTW",
"	WYNN",
"	XEL	",
"	XLNX",
"	XYL	",
"	YUM	",
"	ZBRA",
"	ZBH	",
"	ZION",
"	ZTS	"]


test_dict = {}
counter = 0

for stock in stocks:
    counter = counter + 1
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
    stock_data = yf.Ticker(stock).info
    stockSector = stock_data.get('sector')
    stockPE = stock_data.get('forwardPE')
    
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
    
        
    import yfinance as yf

    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import datetime
    from datetime import datetime
    from datetime import timedelta
    import operator

    # Importing python package pandas datareader to import data from yahoo
    from pandas_datareader import data as pdr
    import yfinance as yf

    betalist = list()

    yf.pdr_override()
    df1 = pdr.get_data_yahoo(stock, start=datedListThirty, end=today)
    df2 = pdr.get_data_yahoo("SPY", start=datedListThirty, end=today)
    
    # We have to take the percent changes to get to returns hence we will use .pct_change()
    # We do not want the first (0th) element because it is NAN
    return_stock = df1.Close.pct_change()[1:]
    return_spy = df2.Close.pct_change()[1:]
    
    
    # Importing libraries and packages
    import statsmodels.api as sm
    from statsmodels import regression
    
    # Regression model
    X = return_spy.values
    Y = return_stock.values
    
    def linreg(x,y):
        x = sm.add_constant(x)
        model = regression.linear_model.OLS(y,x).fit()
    
        # We are removing the constant
        x = x[:, 1]
        return model.params[0], model.params[1]
    
        alpha, beta = linreg(X,Y)
        
        betalist.append(stock + " - " + str(beta))
        
        stockBeta = str(beta)
        if(stockBeta < 1.5):
            score += 5
        if(stockBeta < 1):
            score += 2
        if(stockBeta > 2):
            score -= 3
    
    score = score + closeScore + openScore + lowScore + highScore

    print("Stock " + str(counter) + " of 496")
   
    result = {**test_dict, **{stock: score}}  
    test_dict.update(result)
    
    
N = 5

res = dict(sorted(test_dict.items(), key = itemgetter(1), reverse = True)[:N])
 
# printing result
print("The top stocks are " + str(res))


