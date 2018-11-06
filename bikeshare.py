import time
import pandas as pd
import numpy as np
import datetime
import calendar
#set city data filenames for use later
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = [ 'chicago', 'new york city', 'washington' ]

#set info for use in the date field sort_values
MONTH_DATA = { 'january': '01',
               'february': '02',
               'march': '03',
               'april': '04',
               'may': '05',
               'june' : '06' }

MONTHS = [ 'january', 'february', 'march', 'april', 'may', 'june' ]

DAY_DATA = { 'monday': 0,
             'tuesday': 1,
             'wednesday': 2,
             'thursday': 3,
             'friday': 4,
             'saturday': 5,
             'sunday': 6}

DAYS_OF_WEEK = [ 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]

"""    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


def get_city():
    while True:
        city = input('Would you like to explore data for Chicago, New York City, or Washington?\nPlease type the city name in and hit enter.\n> ').lower()
        if (city in CITIES) or (city == 'all'):
            return city
            break
        print('Sorry, but ' + city + ' does not appear to be a valid input.  Please re-enter.')
        return get_city()
    # TO DO: get user input for month (all, january, february, ... , june)
def get_month():
    while True:
        month = input('Would you like to explore data for January, February, March, April, May, June, or enter ALL for no month filter?\nPlease type the month name in and hit enter.\n> ').lower()
        if (month in MONTHS) or (month == 'all'):
            return month
            break
        print('Sorry, but ' + month + ' does not appear to be a valid input.  Please re-enter.')
        return get_month()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
def get_day():
    while True:
        day = input('Would you like to explore data for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or enter ALL for no day filter?\nPlease type the day name in and hit enter.\n> ').lower()
        if (day in DAYS_OF_WEEK) or (day == 'all'):
            return day
            break
        print('Sorry, but ' + day + ' does not appear to be a valid input.  Please re-enter.')
        return get_day()

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
    df = pd.read_csv(CITY_DATA.get(city))

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    popular_month = MONTHS[popular_month - 1]
    print('\nMost Popular Start Month:', popular_month)

    # TO DO: display the most common day of week
    df['weekday'] = df['Start Time'].dt.weekday
    popular_weekday = df['weekday'].mode()[0]
    popular_weekday = DAYS_OF_WEEK[popular_weekday - 1]
    print('\nMost Popular Start Weekday:', popular_weekday)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nMost Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nMost Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    grouped_trips_count = df.groupby(['Start Station', 'End Station'])['Start Time'].count()
    sorted_trip_startend = grouped_trips_count.sort_values(ascending=False)
    popular_startend_stations = 'From ' + sorted_trip_startend.index[0][0] + ' to ' + sorted_trip_startend.index[0][1]
    print('\nMost Popular Start-End Station Combo:', popular_startend_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal Time Traveled in Seconds:', total_travel_time)
    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('\nAverage Time Traveled in Seconds:', avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df.groupby('User Type')['User Type'].count()
    print('\nDisplay of Counts by ', user_type_count)

    # TO DO: Display counts of gender
    gender_type_count = df.groupby('Gender')['Gender'].count()
    print('\nDisplay of Counts by ', gender_type_count)


    # TO DO: Display earliest, most recent, and most common year of birth

    birthyear_earliest = int(df['Birth Year'].min())
    birthyear_latest = int(df['Birth Year'].max())
    birthyear_avg = int(df['Birth Year'].mode())
    print('\nEarliest birth year ', birthyear_earliest)
    print('\nLatest birth year ', birthyear_latest)
    print('\nMost common birth year ', birthyear_avg)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal Time Traveled in Seconds:', total_travel_time)

def main():
    """Get user input to set the data filters"""
    city = get_city()
    month = get_month()
    day = get_day()
    print(city, month, day)
    """Loads data into dataframe per user input"""
    while True:
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city == 'washington':
            print('Sorry, there are no user specific stats available for ' + city + ".")
        else:
            user_stats(df)

        cnt=0
        while True:
            show_data = input('\nWould you like to see 5 (more) rows of raw data for your selected time\location? Enter yes or no.\n')
            print('Raw trip data show is filtered by ' + day + ' day(s), ' + month + ' month(s), is from the city of ' + city + '.')
            if show_data.lower() == 'yes':
                print(df[cnt:cnt+5])
                cnt +=5
            else:
                break


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            exit()
        else:
            main()

if __name__ == "__main__":
    main()
