def correct_element_of_list(elementList):
    elementList = elementList.strip()
    elementList = elementList.lower()
    elementList = elementList.capitalize()
    elementList += '.'


    return elementList



def correct_sentence(text):
    textSplit = text.split('.')

    if textSplit[-1] == '':
        textSplit.pop(-1)

    lenTextSplit = len(textSplit)


    if lenTextSplit == 1:
        finalResult = correct_element_of_list(textSplit[0])

    else:
        finalResult = list()

        for sentence in textSplit:
            finalResult.append(correct_element_of_list(sentence)) 

        finalResult = ' '.join(finalResult)           




    return finalResult



# print(correct_sentence("Greetings, Sriends. greetings, friends."))

    
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1' 
assert correct_sentence("hello") == "Hello.", 'Test2' 
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3' 
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4' 
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5' 
print('ОК')
