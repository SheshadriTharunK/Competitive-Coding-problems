n = int(input())
appointments = []
for i in range(n):
    appointment = input().strip()
    appointments.append(appointment)


def time_to_minutes(time_str):
    time, am_pm = time_str.split()
    hour, minute = map(int, time.split(':'))
    if am_pm == 'p.m.' and hour != 12:
        hour += 12
    elif am_pm == 'a.m.' and hour == 12:
        hour = 0
    return hour * 60 + minute


sorted_appointments = sorted(appointments, key=time_to_minutes)


for appointment in sorted_appointments:
    print(appointment)
