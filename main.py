
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()

pytrend = TrendReq()
# Get realtime Google Trends data
df = pytrend.trending_searches(pn='philippines')
df.head()
data = df.head()

print(data)

trends.build_payload(kw_list=["Leni Robredo"])
data = trends.interest_by_region()
data = data.sort_values(by="Leni Robredo", ascending=False)
data = data.head(10)
print(data)

data.reset_index().plot(x="geoName", y="Leni Robredo",
                        figsize=(20,15), kind="bar")
plt.style.use('fivethirtyeight')


data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=['Machine Learning'])
data = data.interest_over_time()
fig, ax = plt.subplots(figsize=(20, 15))
data['Machine Learning'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches for Leni Robredo', fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()