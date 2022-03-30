print("Как тебя зовут?")
name=input()
print("Привет",name,"!Твой первый вопрос!")
q=["Москва-столица России?","На свете существуют единороги?","Гарри Поттера играл Питер Паркер?"]
answer=["да","нет","нет"]
for i in q:
 print(i)
 answer1=str(input())
 for j in answer:
      if answer1==str(j):
          print("правильный ответ")
      else:
         print("неправильный ответ")