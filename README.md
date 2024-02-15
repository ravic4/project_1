# What the Fed Project 1 # 
## Presenters:##
RAVI CHAILERTBORISUTH
ADITYA GUPTA
ANTONIO MEDINA
## Objective: To create a financial analysis tool using Python Coding to develop a time series analysis and compare different asset types against the Fed Funds Rate to determine trends, performance and risk analytics. 
The Jupyter Notebook with the code can be found in the Github repository under file name master_notebook_final.ipynb

## What are the questions we hope to answer##
How asset classes perform during shrinking or expanding money supply through fed-fund rate?
Are there periods of heightened risk associated with specific interest rate environments?
Does the fed fund rate have a significant impact to be considered when building a portfolio?

## Fed Fund Rate and Asset Types:##
The Fed Funds Rate is the benchmark rate at which financial institutions lend to each other. It is determined by the Federal Reserve Committee and its goal is to promote financial stability and full employment.  As we will see more in detail in the Fed Fund timeline, the 2019 to 2023 period we are evaluating experienced the highest increase in the Target Federal Funds Rate  from 0% to 5.5% which is the  highest level in 15 years in a span of just 15 months.   For our evaluation, we will be using the Effective Fed Fund Rate (EFFR) which may change daily and takes into account the volume of transactions between the Fed and financial institutions but is set within the target rate. 
A traditional investment approach tells us to, “Don’t Fight the Fed,” meaning it would be wise to align your investment choices with the actions of the Fed.  However, not all assets are expected to react in the same way after a fed fund rate change.  

### Relationship between the Fed Fund Rate and Different asset types:###
The following are some of the expected behaviors of different assets with a Fed Fund Rate Change:
Stocks: When the Fed raises rates, the cost of borrowing increases consumers and businesses which translates in higher costs and cutbacks on capital expenditures and lower profits which would lead to reduced stock prices. However, equity investors may also still welcome a Fed Rate hike if it’s meant to combat the strong headwind of rising inflation.
Bonds: The market values of bonds typically decline as rates go up and vice versa.  This is especially true for short maturity treasury Bonds.  
Crypto:  Although Crypto investors see a safe haven in crypto in times of U.S market Volatility, low rates, or anything that ails the U.S economic performance. In general, high interest rates scare investors away from riskier investments like crypto, and the lowering of rates will be seen as a positive by the crypto investor community.”  It is used as a store of value, medium of exchange, and hedge against inflation, providing users with complete financial autonomy.(1)(5)
##Python Libraries, Data import and Cleaning##

### Libraries ###
The python code in our Jupyter notebook starts by importing all the libraries to be used for our Financial Analysis tool. Please note that besides the regular libraries used so far, we have added a new library, sklearn.linear_model,  to be used  for our linear regression calculation.

### Data Import ###
All data is for daily prices or rates from Jan 1st 2019 to December 31st 2023. The code then begins by importing the data of the assets we will analyze as follows:
1.   ARKK:( High Risk ETF-Stocks), SPY: (S&P 500-Benchmark) and IWM: (Bonds)”  The code uses an .env file with the Keys to obtain the data through an Alpaca API object.
A blank dataframe is created where all 3 assets are then concatenated and setting the date column as index.  Daily returns are also calculated and nulls are dropped.
2.  BITCOIN: (Crypto) Data is obtained for the date range  using the .env and CoinGecko API object
3. FGRTX (Balanced Mutual Fund 50% Stocks and 50%S-T and Bonds) and EFFR (Effective Fed Fund Rate): Data obtained through downloaded CSV files from  https://finance.yahoo.com/quote/FGRTX/history/ and https://www.newyorkfed.org/markets/reference-rates/effr .  For EFFR, the rate are presented as changed from the percent nomenclature to their decimal equivalent.(2)(3)
The code creates a  csvpath to read the files, sort by date (ascending), convert the date into datetime, drop unnecessary columns, count and drop nulls and then recheck if any nulls remain.  The code also checks the data types to make sure they are a float as numerical calculations will be based on the data.
###Data Concatenation###
The code concatenates all the assets dataframes (for Prices and Daily returns) by setting the time as index for all. 
###Data Analysis and further cleaning###
We visualize the Effective Fed Fund Rate plot to determine historical dates that explain the changes and overall trend.  We also Draw the assets returns against the EFFR to discover if high periods of volatility are similar to periods where the EFFR changed from 2019 to 2023.

![EFFR Rate between 2019 to 2023]("/../UCB_FinTech/Project_1/Images/EFFR_RATE.png")

#### EFFR A timeline of the Fed's interest rate hikes 2022–2023####
March-2020: Fed takes action as a response of COVID impact in the U>S Market as a global pandemic.  The Fed Fund rate is reduced gradually from approximately 1.75% to 0% this month. Dow falls 37%
April-2020: Unemployment reaches 14.7%
July 2021: Rates maintained at 0 with some inflation present.
January-2022:  Maximum employment levels and Fed signals Fed Rate increases to come.
February 2022: Russia invades Ukraine
March 2022-July 2023:  Fed applies steady increases (every 1 to 2 months) of approximately 0.25% to 0.75%. The Fed Fund Rate increases from 0% to almost 5.50%.  Inflation rises to almost approximately 9.1%% (June 2022) to almost 4% by the end of 2023. Also, high interest rates are present at the end of  this period which slowed borrowing and capital expenditures. (Source: (4)
The code calculates the daily return for all assets. We also drop all nulls and rename any column to identify the specific assets as needed.
The code also calculates the daily standard deviation of all assets to determine which portfolios are riskier than the S&P 500.
FGRTX    0.013636
SPY      0.013064
ARKK     0.029431
IWM      0.016828
BTC      0.038438

We determine that the balanced portfolio FGRTX appears to have almost an  identical risk as the SP500 and that Bitcoin is the riskiest of all assets. 
The python code we use will then calculate and Plot the correlation

![Heatmap Correlation]["/UCB_FinTech/Project_1/Images/heatmap seaborne.png"]

All assets we evaluated have a positive correlation with the SP500. The balanced Mutual Fund FGRTX has a high correlation with the SP500 and a significant one with the bond portfolio IWM. FGRTX and IWM also have a significant correlation. Bitcoin has the least correlation with all other assets and the SP500.

To further understand the relationship between he assets, the code also  calculates and visualizes the rolling standard deviation for all portfolios using a 30-day window

![Rolling Standard Deviation]["/UCB_FinTech/Project_1/Images/Rolling_STD_30_Day.png"]

Bitcoin has the biggest fluctuations, ARKK appears to have periods of high and low  STD.  FGRTX and  IWM appear to behave closest to the  SP500.

Our code next calculates the Covariance of all the assets with the SP500 and beta which measures the volatility of  the assets compared to the market as a whole.  ARKK and IWM have higher betas and FGRTX and BTC appear to be as volatile as the market’s systematic risk.
FGRTX Beta: 0.9937811717021082 
ARKK Beta: 1.585034812758589 
IWM Beta: 1.1301737359320354 
BTC Beta: 0.9428292586449628 
Our analysis tool  next calculated and visualized  the rolling beta for 60 days:

![Rolling Beta for 60 days]["/UCB_FinTech/Project_1/Images/All_asset_portfolio_beta.png"]
Beta determines the correlation between asset classes and the market (S&P500). FGRTX follows the S&P500 the most, ARKK and BTC are more outliers.

## Linear Regression using the SKLR library ##
### Linear Regression comparing the S&P500 to other asset classes
 
The Linear Regression bar chart above is the Linear Regression  between the S&P 500 against the other assets. The library used was the SKLearn. To obtain the data, we took in the original data frame that contained the daily returns of all assets, converted the column heads into .numpy and reshaped the array into a (-1,1). The (-1,1) allows the data to be converted into 2-dimensions to prepare it for Linear Regression. Once completed, we call in the LinearRegression().fit() functions to obtain the R2 Linear Regression. To compare the two variables the following line of code was called (example only):
Linear_regression = LinearRegression().fit(main, compare) 
![Linear Regression SPY]["/UCB_FinTech/Project_1/Images/Linear_regression_SPY.png"]
### Linear Regression comparing the Fed Fund rate to other asset classes 
![Linear Regression Fed Fund Rate]["UCB_FinTech/Project_1/Images/Linear_regression_SPY.png"]
Above is the correlation between the Fed-Fund rate vs. all other asset classes for over 1200 trading days. 

![EFFR vs. Asset]["/UCB_FinTech/Project_1/Images/Linear_regression_FED.png"]
## Treynor Measure Ratio= (PR−RFR) β##
Our code will calculate and bar plot the Treynor Ratio ​where:
PR=portfolio return
RFR=risk-free rate (EFFR for as the proxy for our calculation for the 2019-2023)
β=beta (relative volatility between the portfolio and the market)
Treynor Ratio reward-to-volatility ratio is a  ratio that combines risk and return performance into a single value to measure portfolio performance that also includes  risk.  The higher the Treynor measure, the better the portfolio. This ratio measure only uses systematic risk, it assumes that the investor already has an adequately diversified portfolio and, therefore, unsystematic risk (also known as diversifiable risk) is not considered.
FGRTX Treynor Ratio: 0.14245397017557215 
ARKK Treynor Ratio: 0.07627358513774643 
IWM Treynor Ratio: 0.060960583345678186 
BTC Treynor Ratio: 0.6042496262784204
Although BTC appears to have the better Treynor ratio by far, it is only one asset and is not diversified.  Next would  FGRTX which is already a diversified mutual fund portfolio and appears to be the best choice. (6)

![Treynor Ratio of Asset Classes]["UCB_FinTech/Project_1/Images/Treynor_Ratio_Asset.png"]


###Sharpe Ratio###
We then  calculate the Sharpe ratio, by assuming a 0 risk-free rate from the portfolio’s rate of return.  Then, they divide the result by the standard deviation of the portfolio’s excess return.
The Sharpe ratio can be helpful only when used to compare very similar investments, like mutual funds and ETFs that track the same underlying index. Still, investors should keep in mind that those investments with a higher Sharpe ratio can be more volatile than those with a lower rate. (investopedia)
ARKK     0.298479
IWM      0.327374
SPY      0.638117
FGRTX    0.739702
BTC      0.964063
BTC although having the highest sharpe ratio, investors may need to consider its high volatility. Surprisingly, FGRTX has a higher ratio than SP500.  The lowest Sharpe ratio is for ARKK.(6)

![Asset Classes Sharpe Ratio]["/UCB_FinTech/Project_1/Images/Sharpe_ratio_.png"]

### Conclusion & Answering Research Question ### 
* How asset classes perform during shrinking or expanding money supply through fed-fund rate?

During contracting or expanding money supply, in the short term daily returns can be impacted by sudden changes by the federal reserve. However, in the long term, it was observed that Federal Reserve Rates did not have a substantial impact on the performance of stocks. 

* Are there periods of heightened risk associated with specific interest rate environments?

In periods where the federal reserve announces a rate hike, asset class prices can fluctuate many fold. This was true when the Federal Reserve drove up rates rapidly (or declined them rapidly) where we saw stock prices run from 2020 till the end of 2021. 

* Does the fed fund rate have a significant impact to be considered when building a portfolio?

The Fed Fund rate does not have a significant as a standalone metric, howeover, when used with other formulas such as Sharpe Ratio (where the Risk-Free Rate is used), the Fed Fund Rate is appropriate. 

### Future Questions to Ask ### 
* What forecasting modelling would fit to determine future performance of these assets? 
* To what extent does valuation metrics play a role in stock performance over time? 
* What trading strategy can be employed from looking at company fundamentals and valuation? Are there other appropriate benchmarks other than the S&P 500 in a more tech-centric world. 



### Resources ###
1.https://www.bankrate.com/investing/federal-reserve-impact-on-stocks-crypto-other-investments
2.https://finance.yahoo.com/quote/FGRTX/history/  
3.https://www.newyorkfed.org/markets/reference-rates/effr
4.https://www.thestreet.com/fed/fed-rate-hikes-2022-2023-timeline-discussion#a-timeline-of-fed-rate-hikes-2022-2023)
5.https://www.nasdaq.com/articles/what-happens-after-a-fed-rate-hike-or-pause
6.Investopedia
7.Fintech Bootcamp Class Materials
8.Fintech Bootcamp Tutor Session (Overall Review)
9.https://numpy.org/doc/stable/reference/generated/numpy.reshape.html
10.https://realpython.com/linear-regression-in-python/
11.Python Tutor: Edward Rees: https://www.edwardrees.info/
12.https://stackoverflow.com/questions/35432378/python-reshape-list-to-ndim-array 
13.https://hvplot.holoviz.org









