def is_input_valid(n):
    try:
        is_valid = int(n)
    except ValueError:
        print('El valor ingresado no corresponde a un número natural.')
        is_valid = False
    except Exception as e:
        raise SystemExit('Hubo un error en la entrada del número.', e)

    
    return is_valid


def get_numeric_str():
    num = input("Cargue un número\n")

    while(is_input_valid(num) is False):
        num = input("Cargue un número\n")

    return num


def get_substr(numeric_str):
    num_substr = []
    

    for i in range(len(numeric_str)):
        for j in range(i + 1, len(numeric_str) + 1):
            try:
                num_substr.append(int(numeric_str[i:j]))
            except ValueError: 
                pass
            except Exception as e:
                raise SystemExit('Hubo un problema generando las subcadenas del número ingresado.', e)


    
    return num_substr


def check_substr(num_substr):
    try:
        divisors = list(filter(lambda divisor: (divisor % 3 == 0 and divisor != 0),  num_substr))
    except Exception as e:
        raise SystemExit('Hubo un problema generando los divisores del número ingresado.', e)
    
    return divisors

def print_result(divisors):
    result = f"El numero tiene al menos tres subcadenas que son divisibles por 3: {divisors}" if len(divisors) >= 3 else "No se encontraron resultados."
    print(result)


def main():
    numeric_str = get_numeric_str()
    num_substr = get_substr(numeric_str)
    divisors = check_substr(num_substr)
    print_result(divisors)


main()