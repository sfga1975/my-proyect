def run(text):
    vowels:str = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    num_vowels = 0
    for letter in text:
        if letter in vowels:
            num_vowels += 1
    return num_vowels


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
