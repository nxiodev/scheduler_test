from datetime import timedelta, time


def is_overlapping(slot, interval):
    start1, end1 = slot
    start2, end2 = interval
    return start1 < end2 and start2 < end1


def find_available_spots(schedule: list, meeting_duration: timedelta) -> list:
    sorted_schedule = sorted(schedule, key=lambda x: x[0])

    day = [(time(hour=x, minute=0), time(hour=0 if x + 1 == 24 else x + 1, minute=0)) for x in range(9, 17)]

    if meeting_duration == timedelta(minutes=30):
        # day = [(time(hour=x // 2, minute=(x % 2) * 30),
        #                    time(hour=((x + 1) // 2) % 24, minute=((x + 1) % 2) * 30))
        #                   for x in range(48)]
        day = [(time(hour=9 + x // 2, minute=(x % 2) * 30),
                time(hour=9 + (x + 1) // 2, minute=((x + 1) % 2) * 30))
               for x in range(16)]

    iter_day = day.copy()

    # delete all the time slots that are already taken
    for time_slot in sorted_schedule:
        for slot in day:
            if is_overlapping(slot, time_slot):
                iter_day.remove(slot)
        # for i in range(len(thirty_min_day)):
        #     if thirty_min_day[i][0] <= time_slot[0] < thirty_min_day[i][1]:
        #         iter_day.pop(i)
        #         break

    available_spots = [(t[0].strftime("%H:%M"), t[1].strftime("%H:%M")) for t in iter_day]

    return available_spots


if __name__ == '__main__':
    th_1 = timedelta(hours=1)
    print(find_available_spots([(time(9, 0), time(10, 30)), (time(12, 0), time(13, 0)), (time(15, 0), time(16, 0))],
                               th_1))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
