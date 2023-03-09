# Create menu
def menu():
    print("""Menu  
------------- 
1. Encode  
2. Decode  
3. Quit""")

#Encode password, add each number by 3
def encode(password):
    encoded = ""
    for num in password:
        if int(num) < 7:
            new = str(int(num)+3)
            encoded += new
        elif int(num) == 7:
            new = "0"
            encoded += new
        elif int(num) == 8:
            new = "1"
            encoded += new
        elif int(num) == 9:
            new = "2"
            encoded += new
    return(encoded)

# Take input, provide encoding / decoding
def main():
    while True:
        menu()
        option = int(input("\nPlease enter an option: "))
        #Encode
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!\n")
            continue
        #Decode
        if option == 2:
            print(f"The encoded password is {encoded}, and the original password is {password}.\n")
        #Exit
        if option == 3:
            return

if __name__ == '__main__':
    main()

