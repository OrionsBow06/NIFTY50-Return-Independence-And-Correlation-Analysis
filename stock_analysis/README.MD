# Objective 
The Primary objective of the analysis is to check if on any day, the closing price of a stoke is independent of it's opening price.

more objectives might be added later

# Detailed Summary 

The analysis consider companies in the NIFTY50 index. For each stock in teh index, it looks at the pricing data between 2020-2025 and from that data will try to determine if the closing price for each day was independent of the opeing price. 

For the above objective, for any stock $s$ on a date $i$, I define two random variables

> $O_{i}^{s}$ : The opening price of the stock $s$ on date $i$
> $C_{i}^{s}$ : The closing price of the stock $s$ on date $i$

Thus to determine independence, I will first look at the correlation between the two random variables and then will try to test independence by using emperical probability and the defination of independence.