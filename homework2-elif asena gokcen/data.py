

import wbdata

#get relevant indicators
#wbdata.search_indicators("gdp per capita") #NY.GDP.PCAP.CD
#wbdata.search_indicators("education" and "duration") #SE.COM.DURS 
#wbdata.search_indicators("Government expenditure on education") #UIS.X.USCONST.FSGOV

import datetime
data_date = datetime.datetime(2017, 1, 1)
indicators = {"NY.GDP.PCAP.CD": "gdppc","SE.COM.DURS": "compulsory education", "UIS.X.US.FSGOV": "goverment exp. on education"}

#create dataframe with indicators
df = wbdata.get_dataframe(indicators,data_date=data_date)


#save the data
df.to_csv('data.csv')
df.describe()

import regression

data = pd.read_csv("data.csv")

print(reg([data["compulsory education"],data["goverment exp. on education"]], data["gdppc"]))


