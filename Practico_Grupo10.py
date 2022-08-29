def is_prime(num):
    """
    Verifica si el número actual es primo. Para eso recorremos todos los números
    desde 2 hasta el número en sí, chequeando que efectivamente el número solo es divisible por sí mismo.


    Args: 
        número actual a verificar.

    Returns:
        Verificamos que el número sea mayor a 1, y a partir de la función all() podemos asegurarnos de la 
        condición de verdad del número actual.
    """

    is_num_prime = []

    for i in range(2, num):
        is_num_prime.append(num % i != 0)
        

    return num > 1 and all(is_num_prime)
    

def rotate_numbers(num):
    """
    Se encarga de la rotación del número actual. Para eso convertimos a éste en un string
    para entonces mover a los cáracteres del mismo. Una vez realizada la transformación,
    volvemos a convertirlo en número, para finalmente agregarlo a la lista.

    Args:
        el número a rotar.
    
    Returns:
        la rotación actual. Ej: 14 => [14, 41]
    """

    rotated_nums = []

    num_to_string = str(num)

    for char in num_to_string:
        rotated_nums.append(int(num_to_string))
        num_to_string = num_to_string[1:] + num_to_string[0]
    
    return rotated_nums


def get_circular_primes():
    """
    Se encarga de recorrer a la rotación actual. Para eso se crea un bucle
    desde el 1 al 100 y se verifica cada número del ciclo. De esta manera, 
    verificamos la condición de verdad de cada rotación de acuerdo a si los números
    que contiene son primos o no. Si la condición de verdad se mantiene de forma
    positiva para cada uno de ellos, entonces podemos afirmar que estamos ante
    primos circulares.

    Args:
        None
    
    Returns:
        Lista de números circulares
    """

    circular_primes = []

    for num in range(1, 101):
        current_rotation = []

        for rotated_num in rotate_numbers(num):
            current_rotation.append(is_prime(rotated_num))
        

        if all(current_rotation):
            circular_primes.append(num)
        
    
    return circular_primes


def print_circular_primes(circular_primes):
    
    for num in range(len(circular_primes)):
        print(f'El {num+1}° primo circular desde el 1 hasta el 100 es {circular_primes[num]}')
    
    print(circular_primes)
        

def main():
    circular_primes = get_circular_primes()
    print_circular_primes(circular_primes)

main()