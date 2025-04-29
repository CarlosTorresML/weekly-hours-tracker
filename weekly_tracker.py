import numpy as np

weeks = int(input('How many weeks do you want to track?: '))
data = []

for i in range(weeks):
    week = []
    print(f'Enter the number of hours in week {i + 1}')
    for x in range(7):
        hours_day = float(input(f'How many hours on week {i + 1}, day {x + 1}?: '))
        week.append(hours_day)
    data.append(week)

# Convert to NumPy array
hours_worked = np.array(data)

# Weekly averages
average_week = np.average(hours_worked, axis=1)

# Print result
print("\n*** WEEKLY SUMMARY TABLE ***")
for i in range(weeks):
    print(f'Average hours worked on {i + 1} week: {average_week[i]:.2f} hrs.')

# Best and worst day
best_day = np.max(hours_worked)
best_day_index = np.argmax(hours_worked)
best_day_index = np.unravel_index(best_day_index, hours_worked.shape)

worst_day = np.min(hours_worked)
worst_day_index = np.argmin(hours_worked)
worst_day_index = np.unravel_index(worst_day_index, hours_worked.shape)

# Final report
print(f"\nMost productive day: {best_day} hours (week {best_day_index[0]+1}, day {best_day_index[1]+1})")
print(f"Least productive day: {worst_day} hours (week {worst_day_index[0]+1}, day {worst_day_index[1]+1})")
