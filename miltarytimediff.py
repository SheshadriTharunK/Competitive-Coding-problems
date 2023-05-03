
start_time=input().strip()
end_time=input().strip()

start_h,start_m,start_s=map(int, start_time.split(':'))
end_h,end_m,end_s=map(int, end_time.split(':'))

if end_time<start_time:
    end_h += 24

total_seconds=(end_h - start_h)*3600+(end_m - start_m)*60+(end_s - start_s)

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print("{:02d}:{:02d}:{:02d}".format(hours,minutes,seconds))
