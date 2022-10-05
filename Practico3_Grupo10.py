class InputContainsLetters(ValueError):
    pass

class InputAllLetters(ValueError):
    pass

def is_input_valid(n: str):
    is_valid = True
    try:
        if(n.isalpha()): raise InputAllLetters("Solo se ingresaron letras.")
        if(not n.isdigit() and "." not in n): raise InputContainsLetters("Se ingresaron letras además de números.")

    except (InputAllLetters, InputContainsLetters) as err:
        is_valid = False
        print(err)
    
    return is_valid




def get_numeric_str():
    num = input("Cargue un número\n")

    while(not is_input_valid(num)):
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


    
    return num_substr


def check_substr(num_substr):
    divisors = list(filter(lambda divisor: (divisor % 3 == 0 and divisor != 0),  num_substr))

    
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