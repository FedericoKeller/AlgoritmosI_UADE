from datetime import date

class InputIsEmpty(Exception):
    pass

def get_binary_data(n, rest = []):

    if (n == 0): return ''.join(map(str, rest[::-1]))

    next_number, remainder = divmod(n, 2)
    rest.append(remainder)

    return get_binary_data(next_number, rest)


def add_to_logs(username, param, isError):
    with open("logs.txt", "a", encoding = 'utf-8') as f:
        result = f"Error: ({username}): {param}" if isError else f"({username})"
        
        f.write(f"{date.today()}: {result}\n")
        




def print_result(binary_data):
    print(binary_data)


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
        print_result(binary_data)
        add_to_logs(username, None, False)
        
    except ValueError:
        e = "El número ingresado no es natural."
        add_to_logs(username, e, True)
        raise SystemExit(e)
    except Exception as e:
        add_to_logs("Vacío", e, True)
        raise SystemExit(e)


main()