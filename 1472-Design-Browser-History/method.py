class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.curr + 1]
        self.history.append(url)
        self.curr += 1

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(len(self.history) - 1, self.curr + steps)
        return self.history[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


'''# TC : O(1), O(1), O(steps), O(steps) respectively to the given methods. TC for back and forward is O(steps) 
since we need to traverse the history linked list until we reach the desired node'''

'''# SC of all methods : O(1) since we are only storing pointers to the previous and next nodes and not creating any new data structures.'''
