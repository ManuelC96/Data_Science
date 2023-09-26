# TATTY
# BRITT

# grey
# yellow
# green





user = list("TRTIT")
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
                
                    # eliminate from dict every el that is not in green status
                    for key in keys:
                        if statuses[key] != "green":
                            del occurencies[key]
                            statuses[key] = "grey"#put every status in stat list in grey but green ones
                    print(f"Keys        -> {keys}")
                    print(f"Values      -> {values}")
                    print(f"Occurencies -> {occurencies}")
                    values.remove(j)# remove from val list the values that have direct correspnding letters
                    #relate keys with remaining values, if keys are more then values don't consider them
                    for index in range(len(values)):#count len values
                        key = keys[index]#extract the first free key
                        if values[index] not in occurencies.values():#if value not present in arleady associeted values
                            occurencies[key] = values[index]#insert key value cuple in dict
                            statuses[key] = "yellow"#set status to yellow


                occurencies[i] = j #key is index day word letter, val is index letter user word, if letter are equal
                break
            # if letters are equals but not in the same position
            if i not in occurencies.keys() and j not in occurencies.values():#if index user word and index day word not in dict
                status = "orange"#set status letter to orange 
                occurencies[i] = j
    
    statuses.append(status)#append status to statuses list                 
                

print(occurencies)
print(statuses)