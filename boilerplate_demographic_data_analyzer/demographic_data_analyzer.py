import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv("adult.data.csv")

  # How many of each race are represented in this dataset?This should be a Pandas series with race names as the index labels.    
  dict={}

  for race in df['race']:
    if race in dict.keys():
      dict[race]+=1
    else:
      dict[race]=1
  race_count = pd.Series(dict)
    

  # What is the average age of men?
  average_age_men = (df.loc[df['sex']=='Male',['age']]).mean().iloc[-1].round(1)
  
  

  # What is the percentage of people who have a Bachelor's degree?
    
  percentage_bachelors = round(df.loc[df['education']=='Bachelors','age'].count()*100/df.shape[0],1)

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  # What percentage of people without advanced education make more than 50K?

  # with and without `Bachelors`, `Masters`, or `Doctorate`
  higher_education = df.loc[df['education'].isin (['Bachelors','Masters', 'Doctorate'])]
  lower_education = df.loc[(df['education']!='Bachelors') & (df['education']!='Masters') & (df['education']!='Doctorate')]
    
  higher_education_rich = round((((higher_education[higher_education['salary']=='>50K'].shape[0])*100)/higher_education.shape[0]),1)
  lower_education_rich = round((((lower_education[lower_education['salary']=='>50K'].shape[0])*100)/lower_education.shape[0]),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  num_min_workers = df.loc[(df['hours-per-week']==min_work_hours)].shape[0]

  rich_percentage=(df.loc[(df['hours-per-week']==min_work_hours) & (df['salary']=='>50K')].shape[0]*100)/num_min_workers


    # What country has the highest percentage of people that earn >50K?
  salary_greater = df.loc[df['salary']=='>50K']

  #count of people having salary >50K
  rich_nations = salary_greater.groupby(by=['native-country'],as_index=False)[['age']].count()

  #people count by country
  total_nations_count= df.groupby(by=['native-country'] ,as_index=False)[['age']].count()

  rich_nations['percent']=None

  for index_r,row_r in rich_nations.iterrows():
    for index_t,row_t in total_nations_count.iterrows():
        if row_r['native-country']==row_t['native-country']:
            rich_nations.loc[index_r,'percent']=(row_r['age']*100)/row_t['age']
            
    

  highest_earning = rich_nations.loc[rich_nations['percent']==rich_nations['percent'].max()]
  
  highest_earning_country=highest_earning['native-country'].iloc[-1]
    
    
  highest_earning_country_percentage=round(highest_earning['percent'].iloc[-1],1)
  
  # Identify the most popular occupation for those who earn >50K in India.
  occupation=df[(df['native-country']=='India') & (df['salary']=='>50K')].groupby(by='occupation',as_index=False)[['age']].count()

  top_IN_occupation = (occupation.loc[occupation['age']==occupation['age'].max()])['occupation'].iloc[-1]



    # DO NOT MODIFY BELOW THIS LINE

  if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

  return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
