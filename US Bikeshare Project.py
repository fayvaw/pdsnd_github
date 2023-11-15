# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 18:14:52 2023

@
"""

# Importing necessary modules and libraries (ed)
import time
import pandas as pd
#no need to import numpy


# Importing my different datasets
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
    
    # Get user input for city
    while True:
        city = input("Enter the name of the city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city name. Please enter a valid city name.")

    # Get user input for month
    while True:
        month = input("Enter the month (january, february, ... , june) or 'all' for no filter: ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Invalid month. Please enter a valid month or 'all'.")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter the day of the week (monday, tuesday, ... sunday) or 'all' for no filter: ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Invalid day. Please enter a valid day or 'all'.")

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
    # importing the data for our 3 cities
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.strftime('%B')
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')

    # Filter by month if applicable
    if month != 'all':
        month_num = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['Start Time'].dt.month == month_num]

    # Filter by day of the week if applicable
    if day != 'all':
        df = df[df['Start Time'].dt.strftime('%A') == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['month'].mode()[0]
    print(f"Most common month: {common_month}")

    # Display the most common day of the week
    common_day = df['day_of_week'].mode()[0]
    print(f"Most common day of the week: {common_day}")


    # Extract the hour from 'Start Time' and display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f"Most common start hour: {common_hour}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"Most commonly used start station: {common_start_station}")

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"Most commonly used end station: {common_end_station}")

    # Display most frequent combination of start station and end station trip
    common_trip = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print(f"Most frequent combination of start station and end station trip: {common_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:")
    print(user_types)

    # Display counts of gender if 'Gender' column exists in the DataFrame
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of gender:")
        print(gender_counts)
    else:
        print("\nGender information not available for this dataset.")


    # Display earliest, most recent, and most common year of birth if 'Birth Year' column exists
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])
        print("\nBirth Year statistics:")
        print(f"Earliest birth year: {earliest_birth_year}")
        print(f"Most recent birth year: {most_recent_birth_year}")
        print(f"Most common birth year: {common_birth_year}")
    else:
        print("\nBirth year information not available for this dataset.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# to display raw data
def display_data(df):
    #asks the user to specify whether or not user wants to see rows of the raw data
    
    show_data = input('\n Do you want to see the first five rows of data? Enter yes or no\n').lower()
    if show_data == 'yes':
        start_loc = 0
        ask_again = True
        while (ask_again):
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            see_next = input("Do you want to see the next five rows of data? Enter yes or no\n").lower()
            if see_next != "no" and see_next != "yes":
                #for when user makes an invalid input
                print("Oops! You made an invalid input!")
                start_loc -= 5
            elif see_next == "no":
                ask_again = False
    else:
        print("\n Thank you for your response!\n")
    
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()