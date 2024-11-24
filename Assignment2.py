def find_longest_word(words):
    if not words:
        return "List is empty"
    longest_word = max(words, key=len)
    return (longest_word, len(longest_word))
words = ["python", "development", "AI", "data"]
print(find_longest_word(words))