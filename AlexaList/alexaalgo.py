def add_chores(list):
    chore = input("what do you want to add? ")
    list.append(chore)
    print("chore added")
    
    more = input("Do you want me to add another chore?, yes or no? ")
    while more == "yes":
        chore = input("what do you want to add? ")
        list.append(chore)
        print("chore added")
        more = input("Do you want me to add another chore?, yes or no?" )
    print("Done adding chores")
    return list

def remove_chores(list):
    if len(list) == 0:
        print("ya done fucked up, you got no chores to do")
        return

    removal = input("what can I remove for you?" )

    for chore in list:
        if chore == removal:
            list.remove(chore)
            print(chore + "has been removed")
    
    print("chores removed")

def list_chores(list):
    if len(list) == 0:
        print("ye got no chores to do ya lazy schmuck")
    else:
        print(len(list))
        for chore in list:
            print(chore + '\n')
    
def identify_words():
    print("BRUUUUUUH")


def main():
    print("I am Alexa")
    chore_list = []
    while input != "fuck off":
        start_Alexa = input('What can I do for you bruh: ')
        if start_Alexa == "add":
            chore_list = add_chores(chore_list)
        if start_Alexa == "remove":
            chore_list = remove_chores(chore_list)
        if start_Alexa == "list":
            list_chores(chore_list)

if __name__=="__main__":
    main()
    

