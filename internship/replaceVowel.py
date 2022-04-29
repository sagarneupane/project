


def repVow(a):
    my_name_char = []
    my_name_vowel = []
    my_name_vowel_index = []
    # my_name_char.insert(index, object)
    for i in a:
        my_name_char.append(i)

    for i in range(len(a)):
        if a[i]=='a' or a[i]=='e' or a[i]=='i'or a[i]=='o' or a[i]=='u':
            my_name_vowel.append(a[i])
            my_name_vowel_index.append(i)
    
    for i in range(len(my_name_vowel_index)):
        if i == len(my_name_vowel_index)-1:
            my_name_char[my_name_vowel_index[i]]=my_name_vowel[i-len(my_name_vowel_index)+1]
            
        else:
            my_name_char[int(my_name_vowel_index[i])] =  my_name_vowel[i+1]
    name = "".join(my_name_char)
    return name
                
    
a = input()
b = repVow(a)
print(b)