class Utils:
    def __init__(self, lista): 
        '''
        Ahora se verifica que al momento de crear el objeto se pase una lista como parametro.
        De no ser así entonces que salte un error.
        '''
        if type(lista) != list:
            self.lista = None
            raise ValueError('Se espera una lista como parámetro de entrada.')
        else:
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
        
        return result #f'{value} grados {scale} son {result} grados {transform_to}'
    
    def __factorial(self, n):
        if n > 1 and type(n) == int:
            n = n * self.__factorial(n-1)
        return n
    
    def factorial(self):
        lista_factoriales = [self.__factorial(i) for i in self.lista]
        return lista_factoriales

    def convert_degrees(self, scale, descale):
        if scale not in ['celsius', 'farenheit', 'kelvin']:
            print(scale, 'no está dentro de los parámetros esperados.')
            print('Los parámetros esperados son:', ['celsius', 'farenheit', 'kelvin'])
            return []
        if descale not in ['celsius', 'farenheit', 'kelvin']:
            print(descale, 'no está dentro de los parámetros esperados.')
            print('Los parámetros esperados son:', ['celsius', 'farenheit', 'kelvin'])
            return []
        cambio = [self.__convert_degrees(value, scale, descale) for value in self.lista]
        return cambio

    def is_prime(self):
        lista_primos = [self.__primo(numero) for numero in self.lista]
        return lista_primos
