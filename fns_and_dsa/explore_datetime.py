from datetime import date, time, datetime, timedelta
def display_current_datetime():
    current_date = date.today()
    current_time = datetime.now().time()
    combine = datetime.combine(current_date, current_time)
    print(combine.strftime("%Y-%m-%d %H:%M:%S"))
def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = date.today()
    future_date = timedelta(days = number_of_days) + current_date
     print("Future date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))
display_current_datetime()
calculate_future_date()
