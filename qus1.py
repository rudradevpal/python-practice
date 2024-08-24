"""
Qus 1. Given a String S, reverse the string without reversing its individual words. Words are separated by dots.
"""

# Method 1
# Define the input
S = "i.like.this.program.very.much"

# Split words by dot and convert to list
word_list = S.split(".")

# Reverse the word list
word_list.reverse()

# Convert reversed list to dot separated string
output1 = ".".join(word_list)

print(output1)


# Method 2
# Define the input
S = "i.like.this.program.very.much"

# Split words by dot and convert to list
word_list = S.split(".")

# Define the output
output2 = ""

# Reverse using for loop which reads list from end
for i in range(len(word_list) - 1, -1, -1):
    output2 += (word_list[i]) + "."

# Remove end dot
output2 = output2.rstrip(".")

print(output2)
