class Utils:
    def __init__(self, lista):
        self.lista = lista

    def __primo(self, n):
        for i in range(2,n):
            if n%i == 0:
                return False
        return True
    
    def mas_rep(self):
        result = 0
        times = 0
        for i in self.lista:
            if self.lista.count(i) > times:
                result = i
                times = self.lista.count(i)
        return f'Más repetido: {result} --> {times} veces.'
    
    def __convert_degrees(self, value, scale, transform_to):
        celsius_to_kelvin = lambda x: x + 273.15
        celsius_to_faren = lambda x: (x * (9/5)) + 32
        kelvin_to_celsius = lambda x: x - 273.15
        faren_to_celsius = lambda x: (5*(x-32))/9

        if scale == 'celsius' and transform_to == 'kelvin':
            result = celsius_to_kelvin(value)
        elif  scale == 'celsius' and transform_to == 'farenheit':
            result = celsius_to_faren(value)
        elif scale == 'kelvin' and transform_to == 'celsius':
            result = kelvin_to_celsius(value)
        elif scale == 'kelvin' and transform_to == 'farenheit': # Anido las funciones lambda; Paso primero a celsius y luego a la escala que necesite.
            result = celsius_to_faren(kelvin_to_celsius(value))
        elif scale == 'farenheit' and transform_to == 'celsius':
            result = faren_to_celsius(value)
        elif scale == 'farenheit' and transform_to == 'kelvin':# Anido las funciones lambda; Paso primero a celsius y luego a la escala que necesite.
            result = celsius_to_kelvin(faren_to_celsius(value))
        elif scale == transform_to:
            result = value
        else:
            result = 'Parámetro de origen o destino no permitido.'
        
        return f'{value} grados {scale} son {result} grados {transform_to}'
    
    def __factorial(self, n):
        if n > 1 and type(n) == int:
            n = n * self.__factorial(n-1)
        return n
    
    def factorial(self):
        for i in self.lista:
            print(self.__factorial(i))

    def convert_degrees(self, scale, descale):
        for i in self.lista:
            print(self.__convert_degrees(i,scale,descale))

    def is_prime(self):
        for i in self.lista:
            if self.__primo(i):
                print('Primo')
            else:
                print('No Primo')
