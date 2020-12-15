def palindromeChecker(phrase):
    if len(phrase) < 1:
        return "palindrome"
    else:
        if phrase[0] == phrase[-1].lower():
            return palindromeChecker(phrase[1:-1])
        else:
            return "not palidrome"

def main(): 
  phrase = input("type a word here to check if it is palindrome: ")
  response = palindromeChecker(phrase.lower())
  print("the word " +phrase+ " is " + response)

main()