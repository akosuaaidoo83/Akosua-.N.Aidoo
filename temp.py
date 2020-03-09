class Temperature:
    def __init__(self,value):
        self.value=value
    def celsius_to_farenheit(self):
        return ((self.value-32)*5/9)
    def farenheit_to_celsiuis(self):
        print ((self.value*9/5)+32)

c=Temperature(100)
   
print(c.value)
#c.celsius_to_farenheit()
print(c.celsius_to_farenheit())
