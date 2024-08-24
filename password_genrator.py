import string
import random
print("----Welcome to password genrator----")
def main():
    length = int(input("Enter the number of length you want to enter: "))
    lowerD = string.ascii_lowercase
    upperD = string.ascii_uppercase
    digitD = string.digits
    symbD = string.punctuation
    combine = lowerD+upperD+digitD+symbD
    X = random.sample(combine,length)
    PASSWORD = "".join(X)
    print(PASSWORD)
    main()
main()    
