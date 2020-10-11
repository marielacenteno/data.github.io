import json
import matplotlib.pyplot as plt
import os
'''
#CURRENCY BAR GRAPH
#input dictionary of exchange rates in different countries
rates= {}
with open ('USD.json', 'r') as f1:
    text1 = f1.read()
rates = json.loads(text1)
print(rates)

# x = values = countries, y = keys = exchange rate
fig, ax = plt.subplots()
ax.set(
    xlabel='currency',
    ylabel='exchange rate from USD',
    )
x = list((sorted(rates.keys())) )
# heights = sorted(rates.values())
heights = []
for label in x:
    heights.append(rates[label])

print('heights=',heights)

ax.bar( x , heights )
#set a limit of what currencies you want to focus on
ax.set_xlim([30, 36])
ax.set_ylim(0, 50)
plt.show()

# .keys() is non-deterministic
# sorted(counts.keys()) is deterministic
print('rates.keys()=',sorted(rates.keys()))
'''


#RELATIONSHIP BETWEEN TEMPERATURE INCREASES AND ANOMALIES
#load data on climate
climate = []
with open ('climate.json', 'r') as f2:
    text2 = f2.read()
climate = json.loads(text2)
#print(climate)

#create y variable as temp 
value = []
yr = climate['data']
yr1 = climate['2009']
yr1v = yr1['value']
value.append(yr1v)
yr2 = climate['2010']
yr2v = yr2['value']
value.append(yr2v)
yr3 = climate['2011']
yr3v = yr3['value']
value.append(yr3v)
yr4 = climate['2012']
yr4v = yr4['value']
value.append(yr4v)
yr5 = climate['2013']
yr5v = yr5['value']
value.append(yr5v)
yr6 = climate['2014']
yr6v = yr6['value']
value.append(yr2v)
yr7 = climate['2015']
yr7v = yr7['value']
value.append(yr7v)
yr8 = climate['2016']
yr8v = yr2['value']
value.append(yr8v)
print(value)

#create second y variable as climate anomalies
anomaly = []
yr = climate['data']
yr1 = climate['2009']
yr1v = yr1['anomaly']
anomaly.append(yr1v)
yr2 = climate['2010']
yr2v = yr2['anomaly']
anomaly.append(yr2v)
yr3 = climate['2011']
yr3v = yr3['anomaly']
anomaly.append(yr3v)
yr4 = climate['2012']
yr4v = yr4['anomaly']
anomaly.append(yr4v)
yr5 = climate['2013']
yr5v = yr5['anomaly']
anomaly.append(yr5v)
yr6 = climate['2014']
yr6v = yr6['anomaly']
anomaly.append(yr2v)
yr7 = climate['2015']
yr7v = yr7['anomaly']
anomaly.append(yr7v)
yr8 = climate['2016']
yr8v = yr2['anomaly']
anomaly.append(yr8v)
print(anomaly)



fig, ax = plt.subplots()
ax.set(xlabel='year')
ax.set(ylabel='degrees fahrenheit')
ax.set_xlim([-8, -1])
ax.plot( climate.keys(), anomaly, label = 'Anomaly')
ax.plot( climate.keys() , value, label = 'Temperature' )
ax.legend()
plt.show()

'''
fig, ax = plt.subplots()
ax.set(
    xlabel='years',
    ylabel='degrees farenheit',
    )

x = list((climate.keys()) )
# heights = sorted(rates.values())
heights = value

ax.plot( x , heights )
#set a limit of what currencies you want to focus on
plt.show()
'''

'''

fig, [ax1, ax2] = plt.subplots(2)
ax1.set(xlabel='year')
ax1.set(ylabel='degrees farenheit')
ax1.line( climate.keys() , climate.values() )
ax2.line( [1,2,3], [4,3,2] )
plt.show()
'''

'''
anomalies = {}
for year in [2009,2010,2011,2012,2013,2014,2015,2016]:
    climate[year]=0
for data in climate:
    year = climate.keys
    print(year)
'''
'''
    year = climate ["data"]
    data = year['2009']
    anomaly1 = data['anomaly']
    year = climate ["data"]
    data = year['2010']
    anomaly2 = data['anomaly']
    year = climate ["data"]
    data = year['2011']
    anomaly3 = data['anomaly']
    year = climate ["data"]
    data = year['2012']
    anomaly4 = data['anomaly']
    year = climate ["data"]
    data = year['2013']
    anomaly5 = data['anomaly']
    year = climate ["data"]
    data = year['2014']
    anomaly6 = data['anomaly']
    year = climate ["data"]
    data = year['2014']
    anomaly7 = data['anomaly']
    year = climate ["data"]
    data = year['2015']
    anomaly8 = data['anomaly']
    year = climate ["data"]
    data = year['2016']
    anomaly9 = data['anomaly']
    keys = anomaly1 + anomaly2 + anomaly3 + anomaly4 + anomaly5 + anomaly6 + anomaly7 + anomaly8 + anomaly9
    print(anomalies)
'''

'''
# x = years, y = degrees farenheit
# one plot shows temperature over the years, other plot displays temperature anamolies over the years
fig, [ax1, ax2] = plt.subplots(1,2)
ax1.set()
'''












'''

# load data for different rates
rates = []
for filename in filenames:
    with open(filename, 'r') as f:
        file_rates = json.loads(f.read())
        rates += file_rates

# the exchange rate from a US dollar for other rates

print('len(rates)=', len(rates))




exchange = {} # x = keys = currency, y = values = rate
for currency in ['USD.json']:
    exchange[currency] = 0
for rate in rates:
    currency = list(rates.keys) [16:]
    print('currency=' , currency)
'''


