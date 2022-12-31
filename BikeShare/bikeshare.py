import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

city = ['chicago', 'new york city', 'washington']
month = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
day = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input("What city are looking to filter by:\n Chicago, New York City, Washington\n")
        if city not in ('Chicago', 'New York City', 'Washington'):
            print("Oops! Your selection is not valid. Please try again.")
            continue
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("Month needed to filter by:\n January, February, March, April, May, June, type 'All' for no filtered month\n")
        if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
            print("Oops! Please select a valid month fitler.")
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("What day would you like to see:\n Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, type 'All' \n")
        if day not in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All'):
            print("Oops! Please select a valid day of the week.")
            continue
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
    print(df)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
#    df['hour'] = df['Start Time'].dt.hour

     # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

 # extract month and day of the week from Start Time and create a new column
        df['month'] = df['Start Time'].dt.month
        df['day_of_the_week'] = df['Start Time'].dt.day_name()

# filter by month to create the new dataframe
        df = df[df['month'] == month]

    print(df)
    df['day_of_the_week'] = df['Start Time'].dt.weekday_name
 # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
 # filter by day of the week if applicable
    if day != 'All':
        # filter by day of the week to create the dataframe
        df = df[df['day_of_the_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print('Most Common Month:', popular_month)


    # TO DO: display the most common day of week
    popular_day=df['day_of_the_week'].mode()[0]
    print('Most common dayof the week:',popular_day)


    # TO DO: display the most common start hour
    popular_hour=df['hour'].mode()[0]
    print('Most common start hour:',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('Most common Start Station:',popular_start_station)

    # TO DO: display most commonly used end station
    popular_used_end_station=df['End Station'].mode()[0]
    print('Most common used end station:',popular_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = (df['Start Station'] + ',' + df['End Station']).mode()
#     print('combo', Combination_Station)
    start_station = Combination_Station[0].split(',')[0]
    end_station = Combination_Station[0].split(',')[1]
    print('\nMost Commonly used combination of start station and end station trip:', start_station, '&', end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time=df['Trip Duration'].sum()
    print('Total travel time:', Total_Travel_Time/86400, "days")


    # TO DO: display mean travel time
    Mean_Travel_Time=df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, "Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print('Counts of each user type:', user_types)

    # TO DO: Display counts of gender
    gender_counts=df['Gender'].value_counts()
    print('counts of each gender:',gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest=df['Birth Year'].min()
    print('Earliest:', earliest)
    most_recent=df['Birth Year'].max()
    print('Most recent:', most_recent)
    most_common=df['Birth Year'].mode()
    print('Most common:', most_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
