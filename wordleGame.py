# TATTY
# BRITT

# grey
# yellow
# green

# T A T T Y

# B R I T T



user = list("TATTY")
word = list("BRITT")
occurencies = {}# association dict
statuses = []
# for x user letter check word
for i in range(len(user)):#extract user word index
    u = user[i]#extract user letter
    status = "grey"#assign letter status grey
   
    for j in range(len(word)):#extract day word index
        w = word[j]#extract day word letter
        if u == w:# if letters are equals
            if i == j:# if letters indexies are equals
                status = "green"#assign letter status green
                values = list(occurencies.values())#create a lst of dict vals

                if j in values:
                    #if index j in values extract all the occurencies keys associated with value 
                    keys = [ k for k, v in occurencies.items() if v in values ]# key list
                
                    
                    for key in keys:
                        if statuses[key] != "green":
                            del occurencies[key]
                            statuses[key] = "grey"
                    print("Keys -> ", keys)
                    print("Values -> ", values)
                    print("Occurencies ->", occurencies)
                    values.remove(j)
                    for index in range(len(values)):
                        key = keys[index]
                        if values[index] not in occurencies.values():
                            occurencies[key] = values[index]
                            statuses[key] = "yellow"


                occurencies[i] = j #key is index day word letter, val is index letter user word, if letter are equal
                break
            # if letters are equals but not in the same position
            if i not in occurencies.keys() and j not in occurencies.values():#if index user word and index day word not in dict
                status = "orange"#set status letter to orange 
                occurencies[i] = j
    
    statuses.append(status)#append status to statuses list                 
                





            


    statuses.append(status)

print(occurencies)
print(statuses)