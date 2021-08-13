f=open("Text.txt",'r')
t=f.read()
t=t.replace(","," ")
#print(t)
#l=len(t)       
l1=t.split()
f.close()
#print(l1)
l_char=[]
l_digi=[]
l_char_digit=l1[::]
for i in l1:
    c=0
    for j in i:
        if(j.isdigit()== True):
            pass
        else:
            c=1
    if(c==0):
        l_digi.append(i)
for i in l1:
    d=0
    for j in i:
        if(j.isalpha()== True):
            pass
        else:
            d=1
    if(d==0):
        l_char.append(i)              
for i in l_char:
    l_char_digit.remove(i)
for i in l_digi:
    l_char_digit.remove(i) 
#print(l_char)
#print(l_digi)
#print(l_char_digit)
'''for i in l_char:
    print(i,end=" ")
print()
for i in l_digi:
    print(i,end=" ")
print()
for i in l_char_digit:
    print(i,end=" ")
print()'''
#f_out=open("output_File.txt","x")
#f_out.close()
f_out=open("output_File.txt","a")

for i in l_char:
    f_out.write(i)
    f_out.write(" ")
    
f_out.write("\n")

for i in l_digi:
    f_out.write(i)
    f_out.write(" ")
    
f_out.write("\n")

for i in l_char_digit:
    f_out.write(i)
    f_out.write(" ")
#f_out.write("\n")     
f_out.close()



