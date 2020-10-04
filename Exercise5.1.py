import time

# Define epoch and local time
epoch = time.time()
t_time = time.localtime()

# Convert local time into hours, minutes and seconds
time = time.strftime('%H:%M:%S', t_time)
print('Current time in hours, minutes and seconds:', time)

# Calculated the days since the epoch
days_since = epoch//60//60//24
print('Number of days since the epoch:', days_since)
