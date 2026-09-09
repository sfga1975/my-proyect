def run(text: str) -> bool:
    seen = set()
    for char in text.lower():
        if char != '-':
            if char in seen:
                return False
            seen.add(char)
    return True


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
