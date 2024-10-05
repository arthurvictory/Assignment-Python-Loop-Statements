# Objective: The aim of this assignment is to practice using nested loops in Python.

# Task 1: Your Mood Tracker Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) 
# for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate 
# over the times of the day. For each time, randomly select a mood from a predefined list and print it. Use the random module again to randomly select the mood.

import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_of_day = ["morning", "afternoon", "evening"]

for day in range(len(day_of_week)):
    for time in range(len(time_of_day)):
        mood_day = random.choice(moods)
        print(f"On {day_of_week[day]} {time_of_day[time]}, you were feeling {mood_day}")