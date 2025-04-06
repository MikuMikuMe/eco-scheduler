Certainly! Below is a simplified Python program for a smart scheduling application named "Eco-Scheduler". This program optimizes resource use and energy savings for office buildings by scheduling times when resources (like heating, cooling, and lighting) are needed based on occupancy. The program includes comments and error handling for better understanding and robustness.

For this example, we'll define a basic structure that analyzes when rooms in an office building are used and schedules resources accordingly. Please note, a real-world application would be more complex and might integrate with IoT systems, energy management software, or building management systems.

```python
import datetime
from collections import defaultdict

# Simulating room booking data for simplicity.
booking_data = {
    "Room A": [("2023-10-03 09:00", "2023-10-03 11:00"), ("2023-10-03 14:00", "2023-10-03 16:00")],
    "Room B": [("2023-10-03 10:00", "2023-10-03 12:00"), ("2023-10-03 15:00", "2023-10-03 17:00")],
}

class Scheduler:
    def __init__(self, booking_data):
        """
        Initializes the Scheduler with the given booking data.

        :param booking_data: Dictionary with rooms as keys and lists of tuples as booking times.
        """
        self.booking_data = booking_data
        self.schedule = defaultdict(list)

    def optimize_schedule(self):
        """
        Main function to optimize resource usage based on room occupancy.
        """
        try:
            for room, times in self.booking_data.items():
                for start_str, end_str in times:
                    # Convert strings to datetime objects
                    start_time = datetime.datetime.strptime(start_str, "%Y-%m-%d %H:%M")
                    end_time = datetime.datetime.strptime(end_str, "%Y-%m-%d %H:%M")

                    # Calculate pre-occupation and post-occupation periods (e.g., 30 min before and after usage)
                    pre_occupation = start_time - datetime.timedelta(minutes=30)
                    post_occupation = end_time + datetime.timedelta(minutes=30)

                    self.schedule[room].append((pre_occupation, post_occupation))
        except Exception as e:
            print(f"An error occurred while optimizing the schedule: {e}")

    def display_schedule(self):
        """
        Display the optimized schedule.
        """
        try:
            for room, periods in self.schedule.items():
                print(f"\nOptimized schedule for {room}:")
                for start, end in periods:
                    print(f"Resource active from {start.strftime('%Y-%m-%d %H:%M')} to {end.strftime('%Y-%m-%d %H:%M')}")
        except Exception as e:
            print(f"An error occurred while displaying the schedule: {e}")

if __name__ == "__main__":
    scheduler = Scheduler(booking_data)
    scheduler.optimize_schedule()
    scheduler.display_schedule()
```

### How the Code Works:

1. **Booking Data**: Simulated data to represent room bookings.
2. **Scheduler Class**: Responsible for analyzing booking times and scheduling resources.
   - `optimize_schedule()`: Calculates active periods for resources, adding extra time before and after each meeting to prepare and efficiently shut down systems.
   - `display_schedule()`: Outputs the discovered optimal schedule.
3. **Error Handling**: The `try-except` blocks capture and print potential errors during schedule computation and display.

### Future Enhancements:

For a real-world application, or to extend this demonstration:
- Integrate with real booking systems (like Google Calendar, Outlook, etc.)
- Implement machine learning models to predict occupancy patterns.
- Connect with building management systems for direct resource control.
- Use external APIs for real-time weather data to optimize HVAC use.