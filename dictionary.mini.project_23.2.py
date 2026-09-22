dictionary = {}

while True:
    print("\n Dictionary Management System")
    print("1. add a word ")
    print("2. Search for meaning ")
    print("3. Display all words")
    print("4. Update meaning ")
    print("5. Delete Word ")
    print("6. Exit ")

    choice = input("Enter your choice :")
    
    if choice == '1':
        word = input("Enter the word :").lower()
        meaning = input("Enter the meaning :")
        dictionary[word] = meaning
        print("Word entered successfully")
    elif choice == '2':
        word = input("Enter Word :")
        if word in dictionary:
            print("Meaning :",dictionary[word])
        else:
            print("word is not found in dictionary")

    elif choice == '3':
        if dictionary :
            print("word and their meanings are :")
            for words,meaning in dictionary.items():
                print(f"{words}:{meaning}")
        else:
         print("Empty here")
    elif choice == '4':
        word = input("Enter a word for updating new mwaning :").lower()
        if word in dictionary :
           new_meaning = input("Enter the new meaning: ")
           dictionary[word] = new_meaning
           print("Meaning is updated succcessfully")
           print("Updated meaning :",dictionary[word])
        else:
            print("The given word is not found in dictionary..")

    elif choice == '5':
        word = input("Enter word to delete :").lower()
        if word in dictionary:
            del dictionary[word]
            print("Word is deleted .")
        else:
             print("word is not found in dictionary")
    elif choice == '6':
        print("Exit the code...")
        break
    else:
        print("Entered choice is incorrect!")
           








 



