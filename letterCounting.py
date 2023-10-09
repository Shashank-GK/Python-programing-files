# This program will count the upper case and lower case characters in given sentence


def count(Phrase):
    lower = 0
    upper = 0
    for l in Phrase:
        if l.islower():
            lower += 1
            # return "The Total number of lower case letters are ", lower
        elif l.upper():
            upper += 1
            # return "The Total number of upper case letters are ", upper
    return (
        "The Total number of lower and upper case letters are ",
        lower,
        " and ",
        upper,
    )


phrase = input(
    "Enter the sentence to count the number of upper and lower case letters in it: "
)
phrase = phrase.replace(" ", "")
print(count(phrase))
