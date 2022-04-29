

def checkAnagram(str1,str2):
    val=""
    count = 0
    if len(str1) == len(str2):
        
        for i in range(len(str1)):
            # str2 = str2
            for j in range(len(str1)):
                if str1[i] == str2[j]:
                    count +=1
                    str2 = str2[:j] + " " + str2[j+1:]
                    break   
        return count,len(str1)
    else:
        return count,len(str1)
    
    
# name = "sagar"
# name = name[:1] + " " + name[2:]
# print(name)  
    
        

a,length = checkAnagram("brainly", "braiynl")
if a == length:
    print("The strings are anagram")
else:
    print("The Strings are not Anagram")        