#Damion Waltermeyer 11/13/2017
def fizzbuzz():
    #Since Fizzbuzz is what makes people happy, why not eliminate extra checks that will occur by using an iterator as mod?
    for i in range(5,101,5):
        if ((i%3==0) and (i%5==0)):
            print("FizzBuzz! at: ",i)
        elif (i%3==0):
            print("Fizz only never happens now")
        elif (i%5==0):
            print("Buzz only :  ",i)
        
fizzbuzz()
