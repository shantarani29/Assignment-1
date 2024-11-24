def filter_long_words(words, n):
    return [word for word in words if len(word) > n]
words = ["python", "development", "AI", "data"]
n = 3
print(filter_long_words(words, n))