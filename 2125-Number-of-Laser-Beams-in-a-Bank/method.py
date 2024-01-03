from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # Count the number of devices in each row
        device_counts = [row.count('1') for row in bank if row.count('1')]
        
        # Pair adjacent device counts and calculate the total number of beams
        total_beams = sum(x * y for x, y in zip(device_counts[1:], device_counts[:-1]))
        
        return total_beams
