class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        kelvin = celsius + 273.15

        fahrenheit = celsius * 1.80 + 32.00
        ans = [kelvin, fahrenheit]
        return ans