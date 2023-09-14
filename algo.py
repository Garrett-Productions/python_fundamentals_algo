# taking in an array and we are reversing it 
# we are starting at the last position and need to end at the first position
def reverse_array(list):
    rev_list = []
    
    for i in range(len(list)-1, -1, -1):
        print(list[i])
        rev_list.append(list[i])
    return rev_list
print(reverse_array([1,2,3,4,5,6,7,8]))





#taking in a string, make an acronym of the string itself, 
#EX) Thank god it's friday and we want the output to be  TGIF



def acronym(str):
    acro = ''
    word = str.split()
    #print(word)

    for i in range(len(word)):
        temp = word[i]
        print(temp[0])
        acro = (acro + temp[0])
        print(acro)
    return acro
print(acronym("thank god its friday"))
