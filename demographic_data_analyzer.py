import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    
    # What is the average age of men?
    df_mens = df[df['sex'] == "Male"]
    average_age_men = float(str(round(df_mens['age'].mean(), 1)))

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_count = df[df['education'] == "Bachelors"]
    percentage_bachelors =  float(str(round((100 * bachelors_count.shape[0]) / df.shape[0], 1)))
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    people_advanced = df[df['education'].isin(["Bachelors", "Masters", "Doctorate"])]
    people_over_50k = people_advanced[(people_advanced['salary'] == ">50K") ]

    people_wo_advanced = df[(~df['education'].isin(["Bachelors", "Masters", "Doctorate"]))]
    people_wo_over_50k = people_wo_advanced[people_wo_advanced['salary'] == ">50K"]
    higher_education_rich = round((100 * people_over_50k.shape[0]) / people_advanced.shape[0], 1)
    lower_education_rich = round((100 * people_wo_over_50k.shape[0]) / people_wo_advanced.shape[0], 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    people_w_num_min_workers =  df[(df['hours-per-week'] == min_work_hours)]
    people_min_ric =  df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == ">50K") ]
    rich_percentage = round((100 * people_min_ric.shape[0]) / people_w_num_min_workers.shape[0], 0)

    # What country has the highest percentage of people that earn >50K?
    rich_countries = df[df.salary=='>50K']['native-country'].value_counts()
    dataframe_countries = df['native-country'].value_counts()
    min_salary_df =(100*rich_countries)/dataframe_countries
    
    highest_earning_country = min_salary_df.idxmax()
    
    highest_earning_country_percentage =  round(min_salary_df[highest_earning_country], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    indian_occupation =  df[df['native-country']=='India']
    top_IN_occupation = indian_occupation[indian_occupation['salary']=='>50K']['occupation'].value_counts().idxmax()
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
