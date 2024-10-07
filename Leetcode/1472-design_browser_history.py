from collections import deque


class BrowserHistory:
    def __init__(self, homepage: str):
        self.container = deque()
        self.container.append(homepage)
        self.back_buffer = deque()

    def visit(self, url: str) -> None:
        self.container.append(url)

    def peek(self):
        peek = self.container[-1]
        return peek

    def print_stack(self):
        print(self.container)

    def size(self):
        return len(self.container)

    def back(self, steps: int) -> str:
        s = self.size()
        if steps > s:
            for _ in range(s - 1):
                back = self.container.pop()
                self.back_buffer.append(back)
            curr = self.peek()
            return curr
        else:
            for _ in range(steps):
                b = self.container.pop()
                print(f" Going backwards {b}")
                self.back_buffer.append(b)
            curr = self.peek()
            return curr

    def forward(self, steps: int) -> str:
        if steps > len(self.back_buffer):
            curr = self.peek()
            return curr
            # for _ in range(len(self.back_buffer)):
            #     forward = self.back_buffer.pop()
            #     self.container.append(forward)
            # curr = self.peek()
            # return curr
        else:
            for _ in range(steps):
                forward = self.back_buffer.pop()
                print(f"Going forward {forward}")
                self.container.append(forward)
            curr = self.peek()
            return curr


if __name__ == "__main__":
    # browserHistory = BrowserHistory("leetcode.com")
    # browserHistory.visit("google.com")
    # browserHistory.visit("facebook.com")
    # browserHistory.visit("youtube.com")
    # browserHistory.back(1)
    # browserHistory.back(1)
    # browserHistory.forward(1)

    browserHistory = BrowserHistory("zav.com")
    browserHistory.visit("kni.com")

    browserHistory.back(7)
    browserHistory.back(7)
    browserHistory.forward(5)
    browserHistory.forward(5)
    browserHistory.print_stack()
