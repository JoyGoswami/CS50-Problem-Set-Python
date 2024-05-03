# get the word from user
get_greeting = input("greeting: ").lower()
print(get_greeting)
# get first word from greeting if there is "," remove it
first_word = get_greeting.split(" ")[0].strip(",")
# check if the word is hello => $0
# check if the sentence starts with hello => $0
# check if the word starts with "h" but not hello => $20
# else everyone gets $100
if first_word == "hello":
    print("$0")
elif first_word[0] == "h":
    print("$20")
else:
    print("$100")
