n = int(input())
word = []

for _ in range(n) :
    word.append(input())

set_word = list(set(word))
print(set_word)
sort_word = []
for i in set_word :
    sort_word.append((len(i), i))

result = sorted(sort_word)
for len_word, words in result :
    print(words)