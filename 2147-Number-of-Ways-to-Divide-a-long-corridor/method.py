class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seat_indices = [i for i, char in enumerate(corridor) if char == 'S']
        num_seats = len(seat_indices)

        if num_seats % 2 or num_seats == 0:
            return 0  # Return 0 if the number of seats is odd or zero

        result = 1
        for i in range(1, num_seats - 1, 2):
            section_length = seat_indices[i + 1] - seat_indices[i]
            result *= section_length

        return result % (10**9 + 7)