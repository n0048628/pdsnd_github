import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    improving get_filters documentation
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). 
    
    while True:
        data = input("Please select a city from --> Chicago, New York City, Washington:\n")
        city = data.lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("You did not enter a valid city")
        else:
            break


    # get user input for month (all, january, february, ... , june)
    
    while True:
        data = input("Please select a month from --> January, February, March, April, May, June, All (for all months) :\n")
        month = data.lower()
        if month not in ('january','february','march','april','may','june', 'all'):
            print("You did not enter a valid month")
        else:
            break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        data = input("Please select a day of the week from --> Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, All (for all days) :\n")
        day = data.lower()
        if day not in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
            print("You did not enter a valid day of the week")
        else:
            break



    print('-'*40)

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
        
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
# extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
# filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november']
        month = months.index(month) + 1
        
# filter by month to create the new dataframe
        df = df[df['month'] == month]
    
# filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
   # display the most common month
   # display the most common day of week
   # display the most common start hour

    common_month = df['month'].mode()[0]
    common_day_of_week = df['day_of_week'].mode()[0]
 
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]

    print("Most Common Month (in number format) --> " + str(common_month))
    print("Most Common Day of the Week          --> " + str(common_day_of_week))
    print("Most Common Start Hour               --> " + str(common_start_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
          

    # display most commonly used start station
    # display most commonly used end station
    # display most frequent combination of start station and end station trip
      
    common_start_station = df['Start Station'].mode()[0]
    common_end_station = df['End Station'].mode()[0]
    frequent_combination_station = (df['Start Station'] + " --> " + df['End Station']).mode()[0]
       
    print("Most Commonly used Start Station   --> " + str(common_start_station))
    print("Most Commonly used End Station     --> " + str(common_end_station))
    print("Most Frequent Start-->End Station  --> " + str(frequent_combination_station))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    # display mean travel time
    
    total_travel_time = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()
    
    print("Total Travel Time  --> " + str(total_travel_time))
    print("Mean Travel Time   --> " + str(mean_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    # Display counts of gender
    # Display earliest, most recent, and most common year of birth
    
    user_counts = (df['User Type'].value_counts())
    print("Total Counts of Users  --> \n" + str(user_counts))
    
    if city != 'washington':
        gender_count = df['Gender'].value_counts()
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print("Gender Counts            --> \n" + str(gender_count))
        print("Earliest Birth Year      --> " + str(earliest_birth_year))
        print("Most Recent Birth Year   --> " + str(most_recent_birth_year))
        print("Most Common Birth Year   --> " + str(most_common_birth_year))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
        
    """Displays statistics on bikeshare users."""

    print('\nViewing Data...\n')
    start_time = time.time()
    
    start_loc = 0
    keep_going = False
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    if view_data == "yes":
       keep_going = True
        
    while (keep_going):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        continue_display = input("Do you wish to continue?: ").lower()
        if continue_display == "no": 
           keep_going = False


    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Ending US bikeshare data exploration - have a great day!!!")
            break
        else:
            print("Restarting bike analysis")
            

            
            

if __name__ == "__main__":
	main()
