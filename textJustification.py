def textJustification(words, L):

    words_joined = " ".join(words)

    total_len = len(words_joined)

    to_return = ""
    while len(to_return) < L:
        for word in words:
            to_return += (word + " ")


    to_return.rstrip(" ")

#     if len(words_joined) % L == 0:
#         return_lst = []
#         while words_joined:
#             return_lst.append(words_joined[:L + 1])
#             words_joined = words_joined[L + 1:]

#     else:
#         print "len(words_joined): ", len(words_joined)
#         print "len(words_joined) / L: ", len(words_joined) / L


#     return return_lst

# words = ["This", "is", "an", "example", "of", "text", "justification."] L = 16
["This    is    an",
 "example  of text",
 "justification.  "]


This is an example of text justification.

lines = []
words_in_line = []
word_count = 0
line = ""
for word in words:
    if len(line) + len(word) + 1 <= L:
        line += (word + " ")
        word_count += 1
    else:
        line.rstrip(" ")
        lines.append(line)
        line = ""
        words_in_line.append(word_count)
        word_count = 0

for i, line in enumerate(lines):
    if len(line) < L:

        spaces_to_add = L - len(line)
        remainder_spaces = spaces_to_add % (words_in_line[i] - 1)

        if spaces_to_add == 0:
        # move on to the next line
            pass

        elif words_in_line[i] == 1 or i == len(lines) - 1:
        # For the last line of text and lines with one word only, the words should be left justified with no extra space inserted between them
            line += (" " * spaces_to_add)

        elif remainder_spaces == 0:
        # distribute evenly the number of spaces to be put if there is an equal number of spaces to be added between the words
            (" " * (spaces_to_add / (words_in_line[i] - 1))).join(line.split(" "))

        # elif spaces_to_add == 1:
            # add a space after only the first word

        elif remainder_spaces != 0:
        # distribute evenly the number of spaces to be put if there is an equal number of spaces to be added between the words
            # line_copy = line
            # change line_copy = len(line_copy[first_word_i:]) + first_word_i
            first_word_i = len(line.index(" "))
            # find some way to find the second word i and so on by string slicing
            second_word_i = len(line[first_word_i + 1:].index(" ")) + first_word_i
            for space in range(remainder_spaces + 1):
            # find the index of the space after the first word, by adding the space after the length of the first word

            while spaces_to_add:
                (" " * (spaces_to_add / (words_in_line[i] - 1))).join(line.split(" "))
                line = line[:first_word_i] + " " + line[first_word_i:]
                spaces_to_add -= 1
