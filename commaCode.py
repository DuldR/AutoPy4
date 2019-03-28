def commaChameleon(comeAndGo):

    # Defining the end item in a list regardless of size.
    endItem = comeAndGo[len(comeAndGo) - 1 ]
    print(endItem)

    # Adding And to the End item in the list.
    comeAndGo[len(comeAndGo) - 1] = "and " + endItem
    print(comeAndGo)

    # Adding comma to the final list.
    print(", ".join(comeAndGo))

spam = ['apples', 'bananas', 'tofu', 'cats', 'dasfasdf', 'Nani?!?!?', 'Omai wa mou, shindeiru']

# Calling the function
commaChameleon(spam)
