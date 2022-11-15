import pandas as pd
import os
import numpy as np
os.chdir(r"C:/Users/abasa/OneDrive/Робочий стіл/Rework/DataCamp/lesson_3")
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', None)

#results of each function are on photos on github
def answer_one():
    file_energy= "energy_indicators.xls"
    energy= pd.read_excel(file_energy,skiprows=16,skipfooter=38)
    energy = energy.drop(energy.columns[[0, 1]],axis = 1)
    energy=energy.rename(columns={energy.columns[0]: "Country", energy.columns[1]: "Energy Supply", energy.columns[2]: "Energy Supply per Capita",energy.columns[3]: "% Renewable"})
    
    energy= energy.replace('...',np.NaN)
    energy['Energy Supply'] = energy['Energy Supply'][1:].apply(lambda x: x*1000000)
    def remove_digits(data):
        newData = ''.join([i for i in data if not i.isdigit()])
        i = newData.find('(')
        if i>-1: newData = newData[:i]
        return newData.strip()
    energy['Country'] = energy['Country'][1:].apply(remove_digits)
    energy['Country'] = energy['Country'].replace('Republic of Korea','South Korea')
    energy['Country'] = energy['Country'].replace('United States of America','United States')
    energy['Country'] = energy['Country'].replace('United Kingdom of Great Britain and Northern Ireland','United Kingdom')
    energy['Country'] = energy['Country'].replace('China, Hong Kong Special Administrative Region','Hong Kong')
    energy['Country'] = energy['Country'].replace('Bolivia (Plurinational State of)','Bolivia')
    energy['Country'] = energy['Country'].replace('Switzerland','Switzerland')
    
    file_gdp= "world_bank.csv"
    GDP=pd.read_csv(file_gdp,skiprows=4)
    GDP.rename(columns={'Country Name': 'Country'}, inplace=True)
    GDP.replace({"Korea, Rep.": "South Korea", 
                "Iran, Islamic Rep.": "Iran",
                "Hong Kong SAR, China": "Hong Kong"}, inplace=True)
    
    
    ScimEn=pd.read_excel("scima.xlsx")
    
    result=pd.merge(pd.merge(energy, GDP, on='Country'), ScimEn, on='Country')
    result=result.set_index('Country')
    result=result[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    result = (result.loc[result['Rank'].isin([i for i in range(1, 16)])])
    result.sort_values('Rank',inplace=True)
    return result
def answer_two():
    Top15 = answer_one()
    years = ['2006', '2007', '2008',
           '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    Top15["avgGDP"] = Top15[years].mean(axis=1)
    return Top15.sort_values("avgGDP",ascending=False)["avgGDP"]
def answer_three():
    Top15 = answer_one()
    Top15["AvgGDP"] = answer_two()
    Top15.sort_values("AvgGDP", ascending=False, inplace=True)
    gdp_2015 = Top15.iloc[5]['2015']
    gdp_2006 = Top15.iloc[5]['2006']
    
    return abs(gdp_2015-gdp_2006)
def answer_four():
    Top15 = answer_one()
    Top15['Ratio']=Top15['Self-citations']/Top15['Citations']

    return (Top15.index[Top15['Ratio'].argmax()],Top15['Ratio'].max())
def answer_five():
    Top15 = answer_one()
    Top15['Population']=Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15=Top15.sort_values("Population",ascending=False)
    
    return Top15.index[2]
def answer_six():
    Top15 = answer_one()
    Top15['Population']=Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15['Citable documents per Capita']=Top15['Citable documents']/Top15['Population']
    Top15['Citable docs per Capita']=np.float64(Top15['Citable documents per Capita'])
    Top15['Energy Supply per Capita']=np.float64(Top15['Energy Supply per Capita'])
    
    return Top15[['Citable docs per Capita','Energy Supply per Capita']].corr()
def answer_seven():
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    
    continents = pd.DataFrame(columns = ['size', 'sum', 'mean', 'std'])
    Top15['Estimate Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    for continent, frame in Top15.groupby(ContinentDict):
        continents.loc[continent] = [len(frame), frame['Estimate Population'].sum(),frame['Estimate Population'].mean(),frame['Estimate Population'].std()]
    
    return continents


