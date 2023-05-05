n = int(input())
appointments = []
for i in range(n):
    appointment = input()
    appointments.append(appointment)
def time_to_minutes_seconds(time_str):
    time, am_pm = time_str.split(' ')
    hour, minute,seconds = map(int, time.split(':'))
    if am_pm == 'pm' and hour != 12:
        hour += 12
    elif am_pm == 'am' and hour == 12:
        hour = 0
    return hour*3600+minute*60+seconds
sorted_appointments = sorted(appointments, key=time_to_minutes_seconds)
for appointment in sorted_appointments:
    print(appointment)

