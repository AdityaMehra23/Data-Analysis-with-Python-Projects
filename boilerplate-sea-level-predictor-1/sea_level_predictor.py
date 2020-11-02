import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df= pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig,ax=plt.subplots()
    df.plot.scatter(x='Year',y='CSIRO Adjusted Sea Level',ax=ax,figsize=(15,7))
    

    # Create first line of best fit
    df_second=pd.DataFrame([],columns=["Year","CSIRO Adjusted Sea Level"])
    #list of Years
    listT=(list(range(df['Year'].min(),2050)))

    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    index=0
    for ele in listT:
      df_second.loc[index,'Year']=ele
      df_second.loc[index,'CSIRO Adjusted Sea Level']=ele*slope+intercept
      index+=1
    ax.plot(df_second['Year'], df_second['CSIRO Adjusted Sea Level'])

    # Create second line of best fit
    df_lim=df.loc[df['Year']>=2000]
    
    df_third=pd.DataFrame([],columns=["Year","CSIRO Adjusted Sea Level"])
    #list of Years
    listT1=(list(range(2000,2050)))

    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df_lim['Year'], df_lim['CSIRO Adjusted Sea Level'])
    index=0
    for ele in listT1:
      df_third.loc[index,'Year']=ele
      df_third.loc[index,'CSIRO Adjusted Sea Level']=ele*slope1+intercept1
      index+=1

    ax.plot(df_third['Year'], df_third['CSIRO Adjusted Sea Level'])

    # Add labels and title
    x=[1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075]
    plt.ylabel("Sea Level (inches)")
    plt.title('Rise in Sea Level')
    ax.set_xticks(x)
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()