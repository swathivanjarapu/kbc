question_list=["how many continents are there","what is the capital of india","ng na kon kon corse padhey"]
option_list=[['four','nine','seven','eight'],
            ['chatishgarh','bhopal','chennai','delhi'],
            ['softwareengineer','counseling','tourism','agriculture',]]
fiftyfifty=[['four','seven'],['delhi','bhopal'],['chennai','delhi']]
solutions=[2,1,2]
solution_list=[3,4,1]
print('welcome to kbc game program')
print('your first question on screen')
i=0
c=0
while i<len(question_list):
    print("your question is")
    print(i+1,question_list[i])
    a=0
    while a<=len(option_list):
        print(a+1,option_list[i][a])
        a+=1
    j=int(input("enter the number"))
    if j==solution_list[i]:
        print("congrulations")
    elif j==5050:
        if c==0:
            m=0
            while m<len(fiftyfifty[i]):
                print(m+1,fiftyfifty[i][m])
                m=m+1
            c=c+1
            num=int(input('enter the solution')) 
            if num==solutions[i]:
                print('correct')
            else:
                print("your option is wrong")
                print("quit")
            
        else:
            print('you already used 5050 lifeline')
            num=int(input("enter option"))
            if num==solution_list[i]:
                print("congratulations")
                break
            else:
                
                print("your wronr")
                break
    else:
        print("wrong")
        print("quit")
        break
    
    i=i+1  
