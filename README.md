# Explore US Bike Share Data project
Explore US Bike Share Data project - Udacity Data Analysis Professional Track.

In this project, I used Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington and write a code to import it and answer questions about it by computing descriptive statistics. Also, I wrote a script that takes in raw input to create an interactive experience in the terminal to present these statistics.


## Software used in this project:

- Python3
- NumPy
- Pandas

## Steps:

- 1- Downlaod the datasets, clean and preprocessing it.
- 2- Detect the bike share usage pattern using some descriptive statistics.
- 3- Compare the system usage between three large cities in US: Chicago, New York City, and Washington, DC and present the results to the user depending on some questions.

## Statistics Computed:

In this project, I wrote a code to provide the following information:

##### 1- Popular times of travel (i.e., occurs most often in the start time)

most common month
most common day of week
most common hour of day

##### 2- Popular stations and trip

most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)

#### 3- Trip duration

total travel time
average travel time

#### 4- User info

counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)

## An Interactive Experience:

I wrote a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, There are four questions that will change the answers:

- Would you like to see data for Chicago, New York, or Washington?
- Would you like to filter the data by month, day, or not at all?
- (If they chose month) Which month - January, February, March, April, May, or June?
- (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?
The answers to the questions above will determine the city and timeframe, After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

## The Datasets:

You will need the three city dataset files too:

- chicago.csv
- new_york_city.csv
- washington.csv

All these files are attached with the project.

Randomly selected data for the first six months of 2017 are provided for all three cities.

All three of the data files contain the same core six (6) columns:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

- Gender
- Birth Year





