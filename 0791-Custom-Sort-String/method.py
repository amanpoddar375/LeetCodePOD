class Solution:
  def customSortString(self, order: str, s: str) -> str:

    char_order = {char: i for i, char in enumerate(order)}
    return ''.join(sorted(s, key=lambda char: char_order.get(char, float('inf'))))
