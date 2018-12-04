# https://adventofcode.com/2018/day/4

import sys

INPUT = "input4.txt" if len(sys.argv) == 1 else sys.argv[1]
print(f'Using input file "{INPUT}"')


with open(INPUT, "r") as f:
    data = f.read() # str
    lines = data.splitlines()
    lines = sorted(lines)

    # [1518-06-18 00:02] Guard #2789 begins shift
    # [1518-04-15 00:56] wakes up
    # [1518-08-16 00:29] falls asleep"""

    guard_id = None
    guard_dict = dict() # total nap time
    sleep_dict = dict() # times asleep for every minute
    sleeps = None

    for line in lines:
        if "Guard" in line:
            guard_id = line.split("#")[1].split()[0]
            guard_id = int(guard_id)

        elif "falls asleep" in line:
            sleep_start = line.split("]")[0][1:]
            sleeps = int(sleep_start.split(":")[1]) # only the minute portion (00 - 59) is relevant for those events

        else: # wakes up
            wake_start = line.split("]")[0][1:]
            awakes = int(wake_start.split(":")[1])

            total = awakes - sleeps
            guard_dict[guard_id] = guard_dict.get(guard_id, 0) + total # add to the total time

            if guard_id not in sleep_dict:
                sleep_dict[guard_id] = dict()

            for i in range(sleeps, awakes):
                sleep_dict[guard_id][i] = sleep_dict[guard_id].get(i, 0) + 1 # increase the nap time


    most_sleep = 0

    # find the sleepiest guard in the dictionary of total naps
    for guard in guard_dict.keys():
        if guard_dict[guard] > most_sleep:
            sleepiest_guard = guard
            most_sleep = guard_dict[guard]

    # find the sleepiest minute for the sleepiest guard
    times_asleep = 0
    sleepiest_minute = 0

    for minute in sleep_dict[sleepiest_guard]:
        if sleep_dict[sleepiest_guard][minute] > times_asleep:
            times_asleep = sleep_dict[sleepiest_guard][minute]
            sleepiest_minute = minute

    print(sleepiest_minute * sleepiest_guard)
 
 
    print('\n---------- PT 2 --------------')
    top_guard, top_minute, top_count = None, None, 0

    for guard in guard_dict.keys():
        # most_common is a tuple (minute, count)
        most_common = max(
            (kv for kv in sleep_dict[guard].items()),
            key=lambda kv: kv[1] # kv == (minute, count)
        )
        if most_common[1] > top_count:
            top_guard, (top_minute, top_count) = guard, most_common

    print(f'guard: {top_guard}, minute: {top_minute}, total: {top_count}')
    print(f'sol: {top_guard * top_minute}')


