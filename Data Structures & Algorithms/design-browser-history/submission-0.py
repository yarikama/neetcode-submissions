class Page:

    def __init__(
        self, 
        url: str | None = None,
        prev: str | None = None,
        next: str | None = None,
    ):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Page()
        self.tail = Page()
        self.curr = Page(homepage, self.head, self.tail)
        self.head.next = self.curr
        self.tail.prev = self.curr
        
    def visit(self, url: str) -> None:
        page = Page(url, self.curr, self.tail)
        self.curr.next = page
        self.curr = self.curr.next
        self.tail.prev = page

    def back(self, steps: int) -> str:
        print(f"from {self.curr.url} ")
        while steps > 0:
            if self.curr.prev is self.head:
                return self.curr.url
            self.curr = self.curr.prev
            steps -= 1
        print(f"to {self.curr.url}")
        return self.curr.url

    def forward(self, steps: int) -> str:
        while steps > 0:
            if self.curr.next is self.tail:
                return self.curr.url
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url

    def printAll(self) -> None:
        curr = self.head
        print("-----------------")
        while curr:
            if curr.url:
                print(curr.url)
            curr = curr.next
        print("")



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)