from datetime import date

class InputIsEmpty(Exception):
    pass

def get_binary_data(n, rest = []):

    if (n == 0): return ''.join(map(str, rest[::-1]))

    next_number, remainder = divmod(n, 2)
    rest.append(remainder)

    return get_binary_data(next_number, rest)


def add_to_logs(username, param = None, isError = False):
    with open("logs.txt", "a", encoding = 'utf-8') as f:
        result = f"Error: ({username}): {param}" if isError else f"({username})"
        
        f.write(f"{date.today()}: {result}\n")
        

def print_result(natural_number, binary_data):
    print(f"El número {natural_number} es igual a {binary_data} en binario.")


def get_username():
    username = input("Ingrese nombre de usuario: \n")
        
    if(len(username) == 0):
            raise InputIsEmpty("El nombre de usuario no puede estar vacío.")

    return username



def main():
    try:
        username = get_username()
        natural_number = int(input("Ingrese un número natural: \n"))

        binary_data = get_binary_data(natural_number)
        print_result(natural_number, binary_data)
        add_to_logs(username)
        
    except ValueError:
        add_to_logs(username, "El número ingresado no es natural.", True)
        raise SystemExit(e)
    except Exception as e:
        add_to_logs("Vacío", e, True)
        raise SystemExit(e)


main()