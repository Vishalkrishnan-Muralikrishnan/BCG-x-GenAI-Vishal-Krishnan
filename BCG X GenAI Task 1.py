#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('C:/Users/mvish/Downloads/BCGXGenAITask1-ExtractData-Copy.csv')


cols_to_clean = [
    'Total Revenue (In Millions)',
    'NET INCOME (In Millions)',
    'TOTAL ASSETS (In Millions)',
    'Total Liabilities (In Millions)',
    'Cash Flows from Operating Activities (In Millions)'
]

for col in cols_to_clean:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(',', '', regex=False)
        .str.replace('$', '', regex=False)
        .str.strip()
    )
    df[col] = pd.to_numeric(df[col], errors='coerce')


df = df.sort_values(by=['Company', 'Year'])


df[cols_to_clean] = df.groupby('Company')[cols_to_clean].transform(lambda group: group.ffill().bfill())


for col in cols_to_clean:
    growth_col = col.replace('(In Millions)', 'YoY Growth (%)').strip()
    df[growth_col] = df.groupby('Company')[col].pct_change(fill_method=None) * 100


summary_cols = ['Company', 'Year'] + cols_to_clean + [col.replace('(In Millions)', 'YoY Growth (%)').strip() for col in cols_to_clean]
print(df[summary_cols].to_string(index=False))


for col in cols_to_clean:
    growth_col = col.replace('(In Millions)', 'YoY Growth (%)').strip()
    plt.figure(figsize=(10, 6))
    for company in df['Company'].unique():
        company_data = df[df['Company'] == company]
        plt.plot(company_data['Year'], company_data[growth_col], marker='o', label=company)
    plt.title(f'{growth_col} by Company Over Time')
    plt.xlabel('Year')
    plt.ylabel('Growth (%)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()








# After Collecting Data from 10-K files from SEC EDGAR Website and Creating graphs from this data using python coding(After formatting it into excel). I have analyzed the following:-
# 
# 1.In The Total Revenue YoY growth % was steadily increasing in Microsoft between the years 2023 and 2024 before a small dip between 2024 and 2025. This 3 fiscal years. Show Microsoft's steady development without falling financially low in revenue. (Showcased progress)
# 
# 2.In The Total Revenue YoY growth % has increased in Apple between the years 2023 and 2024, but sufficient data wasn't present in the 10-K file for Apple,hence the data for 2024 and 2025 can't be analyzed. (Showcased Progress)
# 
# 3.In The Total Revenue YoY growth % has decreased in tesla between 2023 and 2024 showcasing that the Revenue has not increased from previous year ,but just like Apple, there was no data in the 10-K file for Tesla for the year 2025. (Stagnant)
# 
# 4.In The Net Income YoY growth % has been nearly constant growth in Microsoft lying between 0 and 15%.There is Constant growth showcasing Microsoft taking strides to increase their net income in those 3 years.  (Constant Growth)
# 
# 5.In The Net Income YoY growth % has increased in Apple showing Apple's growth in getting Net Income, from having lower Net Income than the previous year. It has now started to get Back to it's old Income. (Slight Growth)
# 
# 6.In The Net Income YoY growth % has decreased in Tesla losing nearly half of it's Previous years Net Income, Indicating large amounts of Money Burn in the year 2023-2024. (Major Decrease)
# 
# 7.In The Total Assets YoY growth % has increased in Microsoft in the year 2024-2025, indicating the Company started to acquire major assets from the previous year, Maybe buying Some Companies. (Major Growth)
# 
# 8.In The Total Assets YoY growth % has increased in Apple as well as in Tesla. This marks that many companies starting taking strides to own assets in the year 2023-2024 Exceptions being Microsoft and hence resulted in Microsoft Acquiring large scale next year(growth)
# 
# 9.In the all the years, Microsoft,Apple and Tesla showed an increase in the Liabilities from the previous year, showcasing the amount of loans or compensation these companies owe increase year own year to meet financial needs. (growth) (Downfall for Companies)
# 
# 10.Both Apple and Tesla had an increase in the Cash flow from operating Activities in the year 2023-24. Showcasing that their operational activities are able to bring the money into the company. (Growth)
# 
# 11.Microsoft is having a growth in the Increase of Cash Flow from operating Activities but the amount it increases from Previous year is slowly Decreasing. This shows that, Microsoft is slowly reaching the limit of how much money can be brought in only from Operating activities, which also hints why they spent so much money in acquiring new Assets. (Slight Decrease)
