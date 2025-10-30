from datetime import datetime, timedelta

# Display the current date and time
current_time = datetime.now()
print("Current date and time:", current_time)

# Format the date nicely
print("Formatted:", current_time.strftime("%A, %B %d, %Y at %I:%M %p"))

# Calculate a date 10 days from now
future_date = current_time + timedelta(days=10)
print("Date 10 days from now:", future_date.strftime("%A, %B %d, %Y"))

# Calculate a date 30 days ago
past_date = current_time - timedelta(days=30)
print("Date 30 days ago:", past_date.strftime("%A, %B %d, %Y"))
