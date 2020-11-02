import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'])

# Clean data
percent=df['value'].max()
df = df.loc[(df['value']<df['value'].quantile(.975)) & 
     (df['value']>df['value'].quantile(.025))]

def draw_line_plot():
    # Draw line plot
    df_plot=df.copy()

    fig,ax=plt.subplots()

    df_plot.plot(x='date',y='value', kind='line',color='red',figsize=(18,10),ax=ax)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=14)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Page Views', fontsize=14)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    #populating year column
    df_bar['Year']=df_bar['date'].map(lambda x: x.strftime('%Y')                )
    #populating month column
    df_bar['Month']=df_bar['date'].map(lambda x: x.strftime('%m'))
    # group by month and year and find average value of views
    df_bar=df_bar.groupby(by=['Year','Month'])[['value']].mean()
    # converting months groups into columns
    df_bar=df_bar.unstack(level=-1)

    # Draw bar plot

    fig,ax=plt.subplots()
    df_bar.plot(y='value', kind='bar',figsize=(18,10),ax=ax)

    plt.xlabel('Years', fontsize=14)
    plt.ylabel('Average Page Views', fontsize=14)
    ax.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
    'October', 'November', 'December'],title='Months')

    

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    #for sorting dataframe by Months
    df_box['month_num']=[d.strftime('%m') for d in df_box.date]
    df_box.sort_values(by='month_num',inplace=True)
    # Draw box plots (using Seaborn)

    fig,(ax1,ax2) = plt.subplots(1,2,figsize=(25,10))
    sns.boxplot(ax=ax1,x='year',y='value',data=df_box)
    sns.boxplot(ax=ax2,x='month',y='value',data=df_box)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    


    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
