import time
import pandas as pd
import numpy as np

cities = {'chicago', 'ny city', 'washington'}
CITY_DATA = {'chicago': 'chicago.csv',
             'ny city': 'new_york_city.csv',
             'washington': 'washington.csv'}
months = {
    'january', 'february', 'march', 'april', 'may', 'june', 'all'

}
days = {
    'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all'
}

# Read Data from user

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        try:
            
# get user input for city (chicago, new york city, washington).
            while True:
                city = str(input("Enter the city Name you want to explore its data [Chicago/NY City/Washington]\n")).lower()
                print('\nYou Entered: {}\n'.format(city).title())
                confirm_city=str(input("Are you sure? [Yes/No]")).lower()
                while confirm_city =='no':
                    city = str(input("Enter the city Name you want to explore its data [Chicago/NY City/Washington]\n")).lower()
                    print('\nYou Entered: {}\n'.format(city).title())
                    confirm_city=str(input("Are you sure? [Yes/No]\n")).lower()
                if city in cities:
                    break
                else:
                    print("Please Check Your Input Value!")
                    continue
                
    # get user input for month (all, january, february, ... , june)
            while True:
                month = str(input("Enter month name [January/February/March/April/May/June/All)\n")).lower()
                print('\nYou Entered: {}\n'.format(month).title())
                confirm_month=str(input("Are you sure? [Yes/No]\n")).lower()
                while confirm_month =='no':
                    month = str(input("Enter month name [January/February/March/April/May/June/All)\n")).lower()
                    print('\nYou Entered: {}\n'.format(month).title())
                    confirm_month=str(input("Are you sure? [Yes/No]")).lower()
                if month in months:
                    break
                else:
                    print("Please Check Your Input Value!")
                    continue
            

# get user input for day of week (all, monday, tuesday, ... sunday)
            while True:
                day = str(input("Enter day of week [Saturday/Sunday/Monday/Tuesday/Wednesday/Thursday/Friday/All)\n")).lower()
                print('\nYou Entered: {}\n'.format(day).title())
                confirm_day=str(input("Are you sure? [Yes/No]\n")).lower()
                while confirm_day =='no':
                    day = str(input("Enter day of week [Saturday/Sunday/Monday/Tuesday/Wednesday/Thursday/Friday/All)\n")).lower()
                    print('\nYou Entered: {}\n'.format(day).title())
                    confirm_day=str(input("Are you sure? [Yes/No]\n")).lower()
                if day in days:
                    break
                else:
                    print("Please Check Your Input Value!")
                    continue
            


        except ValueError:
            print("Please enter a valid value")
        except KeyboardInterrupt:
            print("Wrong Keyboard Input!")
        if city in cities and month in months and day in days:
            break
            

            
    print('-' * 40)
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
    #try:
    
    print("Getting ready")
    df = pd.read_csv(CITY_DATA.get(city), parse_dates=["Start Time", "End Time"])
    
# Get Start Month
    df["Start Month"], df["Start Day"], df["Start Hour"] = (
        df["Start Time"].dt.month_name(),
        df["Start Time"].dt.day_name(),
        df["Start Time"].dt.hour,
    )
   
# Filter Month
    if month != 'all':
        df = df[df["Start Month"] == month.title()]
    if day != 'all':
        df = df[df["Start Day"] == day.title()]
            
        #except Exception as error:
            #print("Exception occurred: {}".format(error))
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    #try:

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == 'all':
        most_common_month = (df["Start Month"].dropna())
        most_common_month = most_common_month.mode()[0]
        print('Most popular month is: {}'.format(most_common_month))
    else:
        print("This option isn't available for choosen filter!\nPlease Select (All) months to get most popular month")
        
    # display the most common day of week
    if day == 'all':
        most_common_day = (df["Start Day"].dropna())
        most_common_day = most_common_day.mode()[0]
        print('Most popular day is: {}'.format(most_common_day))
    else:
        print("This option isn't available for choosen filter!\nPlease Select (all) days to get most popular day")
        
    # display the most common start hour
    most_common_hour = df["Start Hour"].dropna()
    if most_common_hour.empty:
        print("Nothing Found please filter your data again")
    else:
        most_common_hour = most_common_hour.mode()[0]
        print("Most popular hour is: {}".format(most_common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    
    #except Exception as error:
        #print("Exception occurred: {}".format(error))



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    #try:
        

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    most_commonly_start_station = df["Start Station"]
    if most_commonly_start_station.empty:
        print("no most commonly used start station please re-filter your date")
    else:
        most_commonly_start_station = most_commonly_start_station.mode()[0]
        print("Most commonly used start station is: {}".format(most_commonly_start_station))

    # display most commonly used end station

    most_commonly_end_station = df["End Station"]
    if most_commonly_end_station.empty:
        print("no most commonly used end station please re-filter your date")
    else:
        most_commonly_end_station = most_commonly_end_station.mode()[0]
        print("Most commonly used end station is: {}".format(most_commonly_end_station))
    # display most frequent combination of start station and end station trip

    most_frequent_combination_s_e_station = df[["Start Station", "End Station"]].dropna()
    if most_frequent_combination_s_e_station.empty:
        print("No most common start end stations re-filter your data")
    else:
        most_frequent_combination_s_e_station = (most_frequent_combination_s_e_station
        .groupby(["Start Station", "End Station"]).size().sort_values(ascending=False))
        count_of_trips = most_frequent_combination_s_e_station.iloc[0]
        stations = most_frequent_combination_s_e_station[most_frequent_combination_s_e_station == count_of_trips].index[0]
        Start, Destination = stations
        print("Most commonly used start station is: {} and their destination was: {} ,this number of times: {}"
        .format(Start, Destination, count_of_trips))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
        
    #except Exception as error:
        #print("Exception occurred: {}".format(error))



def trip_duration_stats(df, day):
    """Displays statistics on the total and average trip duration."""
    #try:
        
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df["Trip Duration"].dropna()
    #sum_total_time = total_time.sum().round()
    sum_total_time = pd.to_timedelta(total_time.sum().round(), unit='s')
    print("\nTotal Time Traveled for {} day(s) is: {} or {} in seconds".format(day, sum_total_time, total_time.sum()))

    # display mean travel time
        #mean_total_time = total_time.mean()
    mean_total_time = pd.to_timedelta(total_time.mean(), unit='s')
    print("\nMean of Travel Time of {} day(s) is: {} or {} in seconds".format(day, mean_total_time, total_time.mean()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
        
    #except Exception as error:
        #print("Exception occurred: {}".format(error))



def user_stats(df):
    """Displays statistics on bikeshare users."""
    #try:
        
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
        #user_types = df["User Type"].dropna()
    user_types = (df["User Type"].dropna()).value_counts().reset_index()
    print("User Types Count: {}".format(user_types))#.to_string(header=None, index=None))
    # Display counts of gender
    if "Gender" in df:
        count_gender = df["Gender"].dropna()
        if count_gender.empty:
            print("Please choose another filter for your data! This filtered data doesn't contain information about gender count")
        else:
            count_gender = count_gender.value_counts().reset_index()
            print("User Genders Count: {}".format(count_gender.to_string(header=None, index=None)))
    else:
        print("This dataset does not have any gender field")
    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        birth_year = df["Birth Year"].dropna()
        if birth_year.empty:
            print("No Birth Year Found to calculate! Re-filter your data")

        else:
            # Filtered Oldest person as the oldest person on the dataset was 1885 what was not making any sense
            earliest_user = birth_year[birth_year > 1980].min()
            print("Earliest birth date: {}".format(int(earliest_user)))
            most_recent_user = birth_year.max()
            print("Most recent birth date: {}".format(int(most_recent_user)))
            most_common_birthdate = birth_year.mode()[0]
            print("Most common birth date is: {}".format(most_common_birthdate))
    else:
        print("No Birth Year in this dataset")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
        
    #except Exception as error:
        #print("Exception occurred: {}".format(error))



def raw_data(df):
    #try:
        
    restart = 'yes'
    start = 0
    while restart == 'yes':
        try:
            end = start + 5
            dff = df.iloc[start:end]
            print(dff.to_json(orient="records", lines=True))
            start = end
            restart = str(input("\nDo you wish to continue? (Yes/No)")).lower()
                
        except ValueError:
            print("Please enter a valid values")
                
    #except Exception as error:
        #print("Exception occurred: {}".format(error))



def main():
    #try:
    while True:
        city, month, day = get_filters()
        print("Done Filtering")
        # testing input
        print("\nYour filter is based on: City: {}\t Month: {}\tDay: {}\n".format(city.title(), month.title(), day.title()))
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df, day)
        user_stats(df)
        raw = input("\nDo you like to see the details of this data? [Yes/No])").lower()
        if raw == 'yes':
            raw_data(df)
        restart = input('\nWould you like to restart the application? [Yes/No].\n')
        if restart.lower() != 'yes':
            break
            #except ValueError:
                #print("{lease check your input again! Enter Yes or No"])
            #except KeyboardInterrupt:
                #print("Wrong Keyboard Input!")
                



if __name__ == "__main__":
    main()
