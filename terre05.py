# Divisions

def division(a, b):
    try:
        a = int(a)
        b = int(b)
        result = a / b
        result = int(round(result, 1))
        remainder = a % b

        if result != 0:
            print(f"réslutat: {result} \n"
                  f"reste: {remainder}")
        else:
            print("erreur.")

    except ZeroDivisionError:
        print("erreur.")


number_one, number_two = input().split()

division(number_one, number_two)
