class Stack:
    def _init_(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
class Queue:
    def _init_(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
def find_longest_word(words):
    if not words:
        return "List is empty"
    longest_word = max(words, key=len)
    return (longest_word, len(longest_word))
words = ["python", "development", "AI", "data"]
print(find_longest_word(words))
def filter_long_words(words, n):
    return [word for word in words if len(word) > n]
words = ["python", "development", "AI", "data"]
n = 3
print(filter_long_words(words, n))
