seconds = int(input('Enter a number of seconds:'))
day = str(seconds // 60 // 60 // 24)
hour = str((seconds // 60 // 60) % 24) 
min = str((seconds // 60) % 60)
sec = str(seconds % 60)
print(f'{day}:{hour.zfill(2)}:{min.zfill(2)}:{sec.zfill(2)}')