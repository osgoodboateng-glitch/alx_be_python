# daily_reminder.py

# Ask the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
for i in range(3):
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task."
        case "medium":
            reminder = f"'{task}' is a medium priority task."
        case "low":
            reminder = f"'{task}' is a low priority task."
        case _:
            reminder = f"'{task}' has an unspecified priority."
    if time_bound == "yes":
        reminder += " It requires immediate attention today!"
    else:
        reminder += " Consider completing it when you have free time."
    print(f"Reminder: {i+1}: {reminder}")
