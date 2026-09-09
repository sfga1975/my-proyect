def run(items: list[int]) -> list[int]:
    if not items:
        return []

    paso = items[len(items) // 2]
    return items[::paso][::-1]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
