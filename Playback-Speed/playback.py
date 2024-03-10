def main():
    inputStr = str(input("What do you have to say? "))

    controlPlayback(inputStr)

def controlPlayback(str):
    print(str.replace(" ", "..."))

main()