from colorama import Fore
import os
def compile():
    
    temp = input(Fore.GREEN+'please enter your text: ')
    #space
    for space in temp:
        temp = temp.replace(" ", "'")
    
    #a
    for a in temp:
        temp = temp.replace('a', '_&_')
    #b
    for b in temp:
        temp = temp.replace('b', '$@76?') 
    #c
    for c in temp:
        temp = temp.replace("c", "78:*!")
    #d
    for d in temp:
        temp = temp.replace('d', '[=/)7')
    #e
    for e in temp:
        temp = temp.replace('e', '80+#×')
    
    #f
    for f in temp:
        temp = temp.replace('f', '12&$_!')
    #g
    for g in temp:
        temp = temp.replace('g', ':+#75') 
    #h
    for h in temp:
        temp = temp.replace('h', '?($-8')
    #i
    for i in temp:
        temp = temp.replace('i', '[{=8+-$')
    #j
    for j in temp:
        temp = temp.replace('j', '6_#$-/')
    #k
    for k in temp:
        temp = temp.replace('k', '[}{\×÷+8')
    #l
    for l in temp:
        temp = temp.replace('l', '_&$34')
    #m
    for m in temp:
        temp = temp.replace('m' ,'!!#+83;')
    #n
    for n in temp:
        temp = temp.replace('n', '65+-$8')
    #o
    for o in temp:
        temp = temp.replace('o', '#@$62')
    #p
    for p in temp:
        temp = temp.replace('p', ':&$+(8')
    #q
    for q in temp:
        temp = temp.replace('q', '&@(=}')
    #r
    for r in temp:
        temp = temp.replace('r', '+?*;8')
    #s
    for s in temp:
    	temp = temp.replace('s', '+&#$5')
    
    #t
    for t in temp:
        temp = temp.replace('t', '_$+97')
    #u
    for u in temp:
        temp = temp.replace('u', '$&+73')
    #v
    for v in temp:
        temp = temp.replace('v', '&&#(#4')
    #w
    for w in temp:
        temp = temp.replace('w', '&&#(8')
    #x
    for x in temp:
        temp = temp.replace('x', '$$#(8')
    #y
    for y in temp:
        temp = temp.replace('y', '_0&')
    #z
    for z in temp:
        temp = temp.replace('z', '&#($')

    #1
    for one in temp:
        temp = temp.replace('1', '$*_')

    for two in temp:
        temp = temp.replace('2', ':~#')

    for three in temp:
        temp = temp.replace('3', '9!*')

    for four in temp:
        temp = temp.replace('4', '[--]')

    for five in temp:
        temp = temp.replace('5', '(;')

    

    

    print(Fore.CYAN+temp)
    input('back to menu')
    os.system('clear')
    return temp

def decompile():
    #text = input('please enter your file name: ')
    temp = input(Fore.GREEN+'please enter your code: ')
    #space
    for space in temp:
        temp = temp.replace("'", " ")
  
    #a
    for a in temp:
        temp = temp.replace('_&_', 'a')
    #b
    for b in temp:
        temp = temp.replace('$@76?', 'b') 
    #c
    for c in temp:
        temp = temp.replace("78:*!", 'c')
    #d
    for d in temp:
        temp = temp.replace('[=/)7', 'd')
    #e
    for e in temp:
        temp = temp.replace('80+#×', 'e')
    
    #f
    for f in temp:
        temp = temp.replace('12&$_!', 'f')
    #g
    for g in temp:
        temp = temp.replace(':+#75', 'g') 
    #h
    for h in temp:
        temp = temp.replace('?($-8', 'h')
    #i
    for i in temp:
        temp = temp.replace('[{=8+-$', 'i')
    #j
    for j in temp:
        temp = temp.replace('6_#$-/', 'j')
    #k
    for k in temp:
        temp = temp.replace('[}{\×÷+8', 'k')
    #l
    for l in temp:
        temp = temp.replace('_&$34', 'l')
    #m
    for m in temp:
        temp = temp.replace('!!#+83;', 'm')
    #n
    for n in temp:
        temp = temp.replace('65+-$8', 'n')
    #o
    for o in temp:
        temp = temp.replace('#@$62', 'o')
    #p
    for p in temp:
        temp = temp.replace(':&$+(8', 'p')
    #q
    for q in temp:
        temp = temp.replace('&@(=}', 'q')
    #r
    for r in temp:
        temp = temp.replace('+?*;8', 'r')
    #s
    for s in temp:
    	temp = temp.replace('+&#$5', 's')
    #t
    for t in temp:
        temp = temp.replace('_$+97', 't')
    #u
    for u in temp:
        temp = temp.replace('$&+73', 'u')
    #v
    for v in temp:
        temp = temp.replace('&&#(#4', 'v')
    #w
    for w in temp:
        temp = temp.replace('&&#(8', 'w')
    #x
    for x in temp:
        temp = temp.replace('$$#(8', 'x')
    #y
    for y in temp:
        temp = temp.replace('87748+-', 'y')
    #z
    for z in temp:
        temp = temp.replace('&&#($7', 'z')
    print(Fore.CYAN+temp)
    input('back to menu')
    os.system('clear')
    return temp
