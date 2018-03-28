# Assignment 1
# ICS3U
# <Nicholas Sprott>
# March 28, 2018

#1
def CtoF (C):
    """the purpose of this function is to convert the temperature from
       degrees celsius to degree fahrenheit
    """

    C = (1.8*C)+32

    if C <= -459:
        return 'it impossible to calculate'
    else:
        return round(C)


#2
def FtoC (F):
    """the pupose of this function is to convert F degreees to c degrees
    """

    if F <= -459.4:
        return 'it is impossible to calculate'
    else:
        F = (0.55556)*(F-32)
        return round(F)


#this variable wil decide weather the conversion is CtoF, or FtoC
CorF = int(input('input 1 for celsius to fahrenheit, or 2 for  fahrenheit  to celsius: '))

#this is the code that will print the answer depending on the selected value of CorF

if CorF == 1:
    temperatureC = -273
    while temperatureC < -272:
      temperature = int(input('Enter your temperature in Celsius: '))
      print(str(CtoF(temperature)) + ' degrees fahrenheit')
      temperatureC = temperature


      
elif CorF == 2:
    temperatureF = -459
    while temperatureF < -458:
        temperature = int(input('Enter your temperature in Fahrenheit: '))
        print(str(FtoC(temperature)) + ' degrees celsius')
        temperatureF = temperature

    
elif CorF != 1 and CorF != 2:
    print('you stupid or something? i said 1 or 2, not whatever you think a 1 or 2 is. jk you smrt i only kid')















