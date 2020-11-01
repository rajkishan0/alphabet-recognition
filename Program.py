alphabet= {}
number={}
symbol={}
    
data=input("Enter any character")
choice=input("If the character represents Alphabet enter 1, \n If the character represents Number enter 2, \n if the character represents Symbol enter 3 \n")
if (choice == '1'):
    unicode=ord(data)
    alphabet[data]=unicode
    print(alphabet)
if (choice == '2'):
    unicode=ord(data)
    number[data]=unicode
    print(number)
if (choice == '3'):
    unicode=ord(data)
    symbol[data]=unicode
    print(symbol)    
show=input("To show what the machine learnt enter True  if not False ")
if(show=='true'):
    for key in alphabet :
        print("The Alphabets are",key)
    for key in number :
        print("The Numbers are",key)
    for key in symbol :
        print("The Symbol are",key)
