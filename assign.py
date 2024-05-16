class assignment1():
  def subfields():
        print("sub fields in AI are:")
        List=['Machine learning','Neural networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        for temp in List:
              print(temp)

  def oddEven():
       num=int(input("Enter a number:"))
       if(num%2==0):
           print(num,"is even number")
        else:
           print("odd number")
        
  def elegible():
        gender=input("your gender:")
        age=int(input("your age"))
        if(gender=='male'):
            if(age>=21):
                print('eligible')
            else:
                print('not eligible')
        elif(gender=='female'):
            if(age<=18):
                 print('eligible')
            else:
                 print('not eligible')
        else:
             print('invalid')

  def percentage():
         subject1=int(input('subject1='))
         subject2=int(input('subject2='))
         subject3=int(input('subject3='))
         subject4=int(input('subject4='))
         subject5=int(input('subject5='))
         total=subject1+subject2+subject3+subject4+subject5
         print('total',total)
         percentage=total/500*100
         print('percentage',percentage)

  def triangle():
         Height=int(input('Height:'))
         Breadth=int(input('Breadth:'))
         areaformula=((Height*Breadth)/2)
         print("Area formula:(Height*Breadth)/2")
         print("Area of Triangle:",areaformula)
         Height1=int(input('Height1:'))
         Height2=int(input('Height2:'))
         Breadth=int(input('Breadth:'))
         formula=Height1+Height2+Breadth
         print("perimeter formula:Height1+Height2+Breadth")
         print("perimeter of triangle:",formula)