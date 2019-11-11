import secrets
from urllib.request import urlopen

fiveof50=[]
twoof10=[]
freq = []
#Webseite = 'https://www.lotto-hessen.de/eurojackpot/gewinnzahlen-quoten/statistiken'

for i in range(5):
    num1 = secrets.randbelow(50)+1
    while num1 in fiveof50:
        num1 = secrets.randbelow(50)+1
    fiveof50.append(num1)

for i in range(2):
    num2 = secrets.randbelow(10)+1
    while num2 in twoof10:
        num2 = secrets.randbelow(10)+1
    twoof10.append(num2)



#t = urlopen(Webseite)
#raw_data = t.readlines()

#total = str(raw_data[636]).split(' ')[3]

#for line in raw_data:
#    if 'data-index' in str(line):
#        freq.append(str(line).split('t="')[1].rsplit('"')[0])

print('5 out of 50:\n')
for i in range(len(fiveof50)):
    print('Number:', fiveof50[i])

print('\n2 out of 10:\n')
for i in range(len(twoof10)):
    print('Number:', twoof10[i])

#print('\nThe statistic is based on ' + total +' drawings of lots.')
print('\nSave the data? [j/n]:')
in1=input()

if 'j' in in1:
    file1 = open("Data.txt","w")
    output=['5 out of 50:\n']
    for i in range(len(fiveof50)):
        output.append('Number: '+str(fiveof50[i])+'\n')
    output.append('\n2 out of 10:\n')
    for i in range(len(twoof10)):
        output.append('Number: '+str(twoof10[i])+'\n')
    #output.append('\nThe statistic is based on ' + total +' drawings of lots.')
    file1.writelines(output)
    file1.close()
