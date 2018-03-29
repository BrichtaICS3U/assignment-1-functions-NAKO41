# Assignment 1
# ICS3U
# <Nicholas Sprott>
# March 28, 2018

#1 conversion of celsius to fahrenheit
def CtoF (C):#C for celsius
    """the purpose of this function is to convert the temperature from
       degrees celsius to degree fahrenheit
    """

    C = (1.8*C)+32

    if C <= -459: #this will determine if the temperature is below or above absolute zer0
        return 'it impossible to calculate' 
    else:
        return round(C)


#2 coversion of fahrenheit to celsius
def FtoC (F):#F for fahrenheit
    """the pupose of this function is to convert F degreees to C degrees
    """

    if F <= -459.4: #this will determine if the temperature is below or above absolute zer0
        return 'it is impossible to calculate'
    else:
        F = (0.55556)*(F-32)
        return round(F)


#this variable wil decide weather the conversion is CtoF, or FtoC
CorF = int(input('input 1 for celsius to fahrenheit, or 2 for fahrenheit to celsius: '))

#this is the code that will print the answer depending on the selected value of CorF
while CorF != 0:
  if CorF == 1:
      temperatureC = -273#this variable is here so the while loop is able to begin
      while temperatureC < -272:#while the temperature doesn't prduce a real answer
        temperature = int(input('Enter your temperature in Celsius: '))#enter the temperature that will be converted
        print(str(CtoF(temperature)) + ' degrees fahrenheit')#and print it if its input is above asolute 0
        temperatureC = temperature
    


      
  elif CorF == 2:
      temperatureF = -459#this variable is here so the while loop is able to begin
      while temperatureF < -458:#while the temperature doesn't prduce a real answer
          temperature = int(input('Enter your temperature in Fahrenheit: '))#enter the temperature that will be converted
          print(str(FtoC(temperature)) + ' degrees celsius')#and print it if its input is above asolute 0
          temperatureF = temperature
    
        
  elif CorF != 1 and CorF != 2:
      print("sorry, that's an improper input.")


  CorF = int(input("wanna try again, same inputs from before. or input 0 to kill the code: "))#this bit of code checks to if the user wants to run a conversion again or not
                    











