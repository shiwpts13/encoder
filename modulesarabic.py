from colorama import Fore
import os
def compilea():
    #text = input('please enter your file name: ')
    temp = input(Fore.GREEN+'please enter your text: ')
    #space
    for space in temp:
        temp = temp.replace(" ", "'")
    
    #for indent in temp:
        #temp.replace('','"')
    #ا
    for a in temp:
        temp = temp.replace('ا', '_&_')
    #ب
    for b in temp:
        temp = temp.replace('ب', '$@76?') 
    #ت
    for  t in temp:
        temp = temp.replace('ت', '[=/)7')
    #ث
    for ths in temp:
    	temp = temp.replace('ث', '80+#*')
    
    #ج
    for j in temp:
        temp = temp.replace('ج', '12&$_!')
    #ح
    for h in temp:
        temp = temp.replace('ح', '?($-8')
    #خ
    for kh in temp:
        temp = temp.replace('خ', '[{=8+-$')
    #د
    for d in temp:
        temp = temp.replace('د', '6_#$-/')
    #ذ
    for thz in temp:
        temp = temp.replace('ذ', '[}{\×÷+8')
    #ر
    for r in temp:
        temp = temp.replace('ر', '_&$34')
    #ز
    for z in temp:
        temp = temp.replace('ز' ,'!!#+83;')
    #س
    for s in temp:
        temp = temp.replace('س', '#@$62')
    #ش
    for sh in temp:
        temp = temp.replace('ش', ':&$+(8')
    #ص
    for ss in temp:
        temp = temp.replace('ص', '&@(=}')
    #ض
    for  sz in temp:
        temp = temp.replace('ض', '+?*;8')
    #ط
    for  tt in temp:
    	temp = temp.replace('ط', '+&#$5')
    
    #ظ
    for tz in temp:
        temp = temp.replace('ظ', '_$+97')
    #ع
    for aa in temp:
        temp = temp.replace('ع', '$&+73')
    #غ
    for agh in temp:
        temp = temp.replace('غ', '&&#(#4')
    #ف
    for  f in temp:
        temp = temp.replace('ف', '&&#(8')
    #ق
    for gh in temp:
        temp = temp.replace('ق', '$$#(8')
    #ک
    for k in temp:
        temp = temp.replace('ک', '87748+-')
     #ل
    for l in temp:
        temp = temp.replace('ل', '878+-')          #م
    for m  in temp:
        temp = temp.replace('م', '819#48+-')
    #ن
    for n in temp:
        temp = temp.replace('ن', '87#&+-') 
    #و
    for v in temp:
        temp = temp.replace('و', '»«7#-+')
    #ه
    for h in temp:
        temp = temp.replace('ه', '88؟!48+-')
                                                   #ی
    for y in temp:
        temp = temp.replace('ی', '8$£π×-')
                                                                         
    print(Fore.CYAN+temp)
    input('back to menu')
    os.system('clear')
    return temp

def decompilea():
    #text = input('please enter your file name: ')
    temp = input(Fore.GREEN+'please enter your code: ')
    #space
    for space in temp:
        temp = temp.replace("'", " ")
    
    #for indent in temp:
        #temp
    #ا
    for a in temp:
        temp = temp.replace('_&_',"ا")
    #ب
    for b in temp:
        temp = temp.replace( '$@76?',"ب") 
    #پ
    for  p in temp:
        temp = temp.replace( "78:*!","پ")
    #ت
    for t in temp:
        temp = temp.replace( '[=/)7',"ت")
    #ث
    for th in temp:
        temp = temp.replace('80+#×',"ث")
    
    #ج
    for j in temp:
        temp = temp.replace('12&$_!',"ج")
    #چ
    for ch in temp:
        temp = temp.replace( ':+#75','چ') 
    #ح
    for  h in temp:
        temp = temp.replace('?($-8','ح')
    #خ
    for kh in temp:
        temp = temp.replace('[{=8+-$','خ')
    #د
    for d in temp:
        temp = temp.replace('6_#$-/','د')
    #ذ
    for thz in temp:
      temp = temp.replace('[}{\×÷+8',"ذ")
    #ر
    for r in temp:
        temp = temp.replace('_&$34','ر')
    #ز
    for z in temp:
        temp = temp.replace('!!#+83;','ز')
    #ژ
    for zh in temp:
        temp = temp.replace('65+-$8','ژ')
    #س
    for s in temp:
        temp = temp.replace( '#@$62','س')
    #ش
    for sh in temp:
        temp = temp.replace(':&$+(8','ش')
    #ص
    for  ss in temp:
        temp = temp.replace('&@(=}','ص')
    #ض
    for sz in temp:
        temp = temp.replace('+?*;8','ض')
    #ط
    for tt in temp:
    	temp = temp.replace( '+&#$5',"ط")
    
    #ظ
    for tz in temp:
        temp = temp.replace('_$+97','ظ')
    #ع
    for aa in temp:
        temp = temp.replace('$&+73',"ع")
    #غ
    for  agh in temp:
        temp = temp.replace('&&#(#4',"غ")
    #ف
    for  f in temp:
        temp = temp.replace('&&#(8',"ف")
    #ق
    for gh in temp:
        temp = temp.replace('$$#(8',"ق")
    #ک
    for  k in temp:
        temp = temp.replace('87748+-',"ک")
    #گ
    for  kg in temp:
        temp = temp.replace('&&#($7',"گ")
     #ل
    for l in temp:
        temp = temp.replace('878+-',"ل")          #م
    for m in temp:
        temp = temp.replace('819#48+-',"م")
    #ن
    for n in temp:
        temp = temp.replace('87#&+-',"ن") 
    #و
    for v in temp:
        temp = temp.replace( '»«7#-+',"و")
    #ه
    for h in temp:
        temp = temp.replace('88؟!48+-',"ه")
                                                   #ی
    for y in temp:
        temp = temp.replace( '8$£π×-',"ی")
                                              
    print(Fore.CYAN+temp)
    input('back to menu')
    os.system('clear')
    return temp
