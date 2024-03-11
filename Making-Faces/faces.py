def main():
    getInput = str(input())

    convert(getInput)

def convert(inputStr):
    findIndex = inputStr.index(":")
    
    if inputStr[findIndex] == ":" and inputStr[findIndex +1] == ")":
        print(inputStr.replace(":)", "happy"))
    elif inputStr[findIndex] == ":" and inputStr[findIndex +1] == "(":
        print(inputStr.replace(":(", "sad"))
    else:
        print(inputStr)

main()