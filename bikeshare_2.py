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
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    while True:
        city = input("Choose City From (chicago, new york city, washington) ")
        if city != "chicago" and city != "new york city" and city != "washington":
            print('Invalid Input, Please Try Again.')
        else:
            break
            
    # get user input for month (all, january, february, ... , june)
    month = ""
    while True:
        month = input("Choose month From (all, january, february, march, april, may, june) ")
        if (month != "all" and month != "january" and month != "february" and
           month != "march" and month != "april" and month != "may" and month != "june"):
            print('Invalid Input, Please Try Again.')
        else:
            break

    # get user input for day of week (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)
    day = ""
    while True:
        day = input("Choose Day From (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday) ")
        if (day != "all" and day != "monday" and day != "tuesday" and day != "wednesday" and 
           day != "thursday" and day != "friday" and day != "saturday" and day != "sunday"):
            print('Invalid Input, Please Try Again.')
        else:
            break

    print('-'*60)
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
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(df['month'].mode()[0])

    # display the most common day of week
    print(df['day_of_week'].mode()[0])

    # display the most common start hour
    print(df['Start Time'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(df['Start Station'].mode()[0])

    # display most commonly used end station
    print(df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print(df.groupby(['Start Station','End Station']).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Difference'] = pd.to_datetime(df["End Time"]) - pd.to_datetime(df["Start Time"])
    print(pd.Series(df['Difference']).sum())

    # display mean travel time
    print(df['Difference'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df.index:
        print(df['Gender'].value_counts())

    # Display earliest year of birth
    if 'Birth Year' in df.index:
        print(df['Birth Year'].min())
        # Display most recent year of birth
        print(df['Birth Year'].max())
        # Display most common year of birth
        print(df['Birth Year'].mode()[0])

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
