def is_palindrome(word):
    word = word.replace(" ","")  # Remove spaces from the word
    word = word.lower()  # Convert the word to lowercase
    reversed_word = word[::-1]  # Create a reversed version of the word using slicing
    if word == reversed_word:  # Check if the word is equal to its reversed version
        return True
    else:
        return False


def run():
    word = input("Write the word: ")  
    check_palindrome = is_palindrome(word)  # Check if the word is a palindrome
    if check_palindrome == True: 
        print("is palindrome")
    else:
        print("is not palindrome")  


if __name__ == "__main__":
    run() 
