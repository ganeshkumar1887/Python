# revrese the string using the split and join
w = input("Enter a String = ")
rev_w = ' '.join(w.split()[::-1])
print(rev_w)

# revrse string using loop
s= w
words = s.split() # split means string into word 
rev_words = " "
for word in reversed(words):
    rev_words += word + " "
rev_words = rev_words.strip() # strip fn is used to remove trailling space
print(rev_words)

