def run(text: str) -> tuple[int, int]:
    num_letters = 0
    num_digits = 0

    for char in text:
        n = ord(char)

        match n:
            case _ if 65 <= n <= 90:      # A-Z
                num_letters += 1
            case _ if 97 <= n <= 122:     # a-z
                num_letters += 1
            case _ if 48 <= n <= 57:      # 0-9
                num_digits += 1

    return num_letters, num_digits


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
