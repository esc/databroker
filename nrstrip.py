# this is the python file used to genarete
# a quotes file for Afreet from the Database

file = open('Database/Proteus.set')

quotes = list()
multiline = False
buff = str()
for l in file.readlines():
    #l = l.rstrip()
    if multiline :
        if ']]' in l:
            buff += l[:l.index(']')]
            quotes.append(buff)
            multiline = False
            buff = str()
        else :
            buff += l
    elif 'flavor' in l:        
        temp = str()
        if '[[' in l and ']]' in l:
            temp = l[l.rindex('[')+1:l.index(']')]
            if len(temp) > 0 : quotes.append(temp)
        else :
            multiline = True
            buff = l[l.rindex('[')+1:]            
    else :
        pass

for q in quotes:
    print '"' + q.replace('"','\\"') + '"'
    
            
             

