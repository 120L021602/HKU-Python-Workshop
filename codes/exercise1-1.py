# Write a program that convert time period (in seconds) to the long format represented by the pattern ?h ?m ?s. You
# can refer to the notes for example inputs/outputs.

total_seconds = int(input("Enter total seconds: "))
hours = total_seconds // 3600
remain_seconds_1 = total_seconds - hours * 3600
minutes = remain_seconds_1 // 60
remain_seconds_2 = remain_seconds_1 - minutes * 60
seconds = remain_seconds_2
print(f"{hours}h", f"{minutes}m", f"{seconds}s")