class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Max diff is 24*60=1440 minutes 
        min_diff = 1440  
        time_in_minutes = []
        for t in timePoints:
            hour, minute = map(int, t.split(":"))
            time_in_minutes.append(hour * 60 + minute)
            
        # Sorting minute values
        time_in_minutes.sort()
        # Find min_diff
        for i in range(len(time_in_minutes)):
            # Get two following minute values
            time1 = time_in_minutes[i-1]
            time2 = time_in_minutes[i]

            # Calculate the difference - % 1440 to account for 00:00
            diff = (time2 - time1) % 1440

            # Update minimum difference
            min_diff = min(min_diff, diff, 1440 - diff)
            # if min_diff = 0 stop the loop and return 0
            if min_diff == 0:
                return 0
        return min_diff
         