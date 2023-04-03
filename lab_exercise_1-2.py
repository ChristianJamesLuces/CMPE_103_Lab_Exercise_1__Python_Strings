import pyfiglet

# Define variables
intro = pyfiglet.figlet_format("WELCOME".center(39, "="), font = "digital")
no_option = ("No", "no", "NO", "n", "N")
yes_option = ("Yes", "yes","YES","y","Y")
character_susbsitute = "\t'a' = *\n\t'e' = &\n\t'i' = #\n\t'o' = +\n\t'u' = !\n"
special_characters = "*", "&", "#", "+", "!"
gratitude = "\033[42m" + "(: Thank you for using this program! :)" + "\033[0m"

# Display welcome message and its function
while True:
    print(intro)
    print("\033[45;1m" + "This program will decrypt your encrypted input using the following character substitute:\n" + "\033[0m") # Explains the function of the program
    print("\033[93m" + character_susbsitute + "\033[0m")
    print("-" * 100)

    ask = str(input("\033[1m" + "Enter a string to decrypt: " + "\033[0m")) # ask the user for input
    output = ""

    for i in range(len(ask)):   # check each character
        if ask[i] not in special_characters:
            output += "\033[94;1m" + ask[i] + "\033[0m" 
        elif ask[i] == "*":   # if *, change it to a 
            output += "\033[91;4;1m" + "a" + "\033[0m" 
        elif ask[i] == "&":   # if &, change it to e
            output += "\033[91;4;1m" + "e" + "\033[0m" 
        elif ask[i] == "#":   # if #, change it to i
            output += "\033[91;4;1m" + "i" + "\033[0m" 
        elif ask[i] == "+":   # if +, change it to o
            output += "\033[91;4;1m" + "o" + "\033[0m" 
        elif ask[i] == "!":   # if !, change it to u
            output += "\033[91;4;1m" + "u" + "\033[0m"
        else:
            output += ask[i]

    print("\033[1m" + "The decrypted input is: " + "\033[1m" + output )    # print the output 

     #Asking the user if they want to try it again
    answer = str(input("\nDo you want to try it again? (Yes or No): "))
    if answer in yes_option:    #If the user want to try it again 
        print("\n\n")
    elif answer in no_option:   #If the user do not want to try it again
        print("\n" + "<" * 100) 
        print(gratitude.center(100))
        print(">" * 100)
        break
    while answer not in no_option+yes_option:
        print ("Invalid Input")
        answer = str(input("\nDo you want to try it again? (Yes or No): ")) #If the user did not input a valid answer
        if answer in no_option:
            print("\n" + "<" * 100)
            print(gratitude.center(100))
            print(">" * 100)
            exit()  # Exit the loop after a valid input is given
        if answer in yes_option:
            continue    # Go back to the start of the loop
    