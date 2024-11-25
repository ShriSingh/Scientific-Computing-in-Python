def add_time(start: str, duration: str, day=None):
    """
    Adds a start time and a duration time and returns the result.
    
    Parameters: 
    start : str
        The start time composed of hours, minutes, and meridian 
        in a 12-hour format
    duration : str
        Hours and minutes needed to be added to the start time
    day : str, optional
    """

    # Constants
    HOURS_IN_A_DAY = 24
    HOURS_IN_HALF_A_DAY = 12
    MINUTES_IN_AN_HOUR = 60
    DAYS_OF_THE_WEEK = [
        'Sunday',
        'Monday', 
        'Tuesday', 
        'Wednesday', 
        'Thursday', 
        'Friday', 
        'Saturday' 
    ]
    NUMBER_OF_DAYS_IN_A_WEEK = 7
    DAYS_PASSED = 0
    HOURS_PASSED = 0
    MIDNIGHT_TIME = 0

    # Extracting the numbers from the start and duration
    start_hrs = int(start.split(':')[0]) # Starting time hours
    start_mins = int(start.split(':')[1][:2]) # Starting time minutes
    start_meridian = start.split(':')[1][3:] # Starting time meridian

    duration_hrs = int(duration.split(':')[0]) # Duration time hours
    duration_mins = int(duration.split(':')[1]) # Duration time minutes

    # Converting to 24-hour format for easier calculation
    if start_meridian == 'PM' and start_hrs != HOURS_IN_HALF_A_DAY: # For evening and night times
        start_hrs += HOURS_IN_HALF_A_DAY
    elif start_meridian == 'AM' and start_hrs == HOURS_IN_HALF_A_DAY: # For midnight time
        start_hrs = MIDNIGHT_TIME

    # Adding duration hours and minutes to start hours and minutes
    total_hrs = start_hrs + duration_hrs
    total_mins = start_mins + duration_mins

    # Handling overflow of minutes
    if total_mins >= MINUTES_IN_AN_HOUR:
        total_hrs += 1 # Incrementing the hours --> 60 mins = 1 hour
        total_mins %= MINUTES_IN_AN_HOUR

    # Handling overflow of hours
    DAYS_PASSED = total_hrs // HOURS_IN_A_DAY # Carryforwarding extra hours into days

    # Handling overflow of minutes
    HOURS_PASSED = total_hrs % HOURS_IN_A_DAY # Storing the remaining minutes after handling hours overflow

    # Converting back to 12-hour format
    if HOURS_PASSED == 0: # If it's midnight
        HOURS_PASSED = HOURS_IN_HALF_A_DAY
        start_meridian = 'AM'
    elif HOURS_PASSED < HOURS_IN_HALF_A_DAY: # If it's before afternoon
        start_meridian = 'AM'
    elif HOURS_PASSED == HOURS_IN_HALF_A_DAY: # If it's exactly afternoon
        start_meridian = 'PM'
    else: # If it's evening or night time
        HOURS_PASSED -= HOURS_IN_HALF_A_DAY
        start_meridian = 'PM'

    # Handling the days of the week
    if day is not None: # Checking if the optional parameter is entered
        # Making the 1st letter upper case and the rest lower
        day_entered = day.capitalize()
        # Finding the position of the day entered in the week list
        day_on_the_week_index = DAYS_OF_THE_WEEK.index(day_entered)
        # Finding the new position after accounting for days passed in the week list
        new_day_index = (day_on_the_week_index + DAYS_PASSED) % NUMBER_OF_DAYS_IN_A_WEEK
        # Storing the day at the new position
        new_day = DAYS_OF_THE_WEEK[new_day_index]
    else: # If the optional parameter's empty
        new_day = None

    # Bringing in final calculated hours and minutes
    new_time = f"{HOURS_PASSED}:{total_mins:02d} {start_meridian}" # ':02d' adds in leading zeros whenever needed
    if new_day:
        new_time += f", {new_day}" 

    # Handle next day or days later message
    if DAYS_PASSED == 1:
        new_time += " (next day)"
    elif DAYS_PASSED > 1:
        new_time += f" ({DAYS_PASSED} days later)"

    # Returning the result
    return new_time
