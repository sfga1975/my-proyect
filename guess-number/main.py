def run(target_number: int) -> None:
    num_intent = 0

    while True:
        print("Introduzca número:")
        give_number = int(input())
        num_intent += 1

        if give_number < target_number:
            print("Menor")
        elif give_number > target_number:
            print("Mayor")
        else:
            break

    print(f"Enhorabuena has encontrado el número en {num_intent} intentos")



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
