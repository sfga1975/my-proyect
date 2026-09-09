def run(input_date: str, base_year: int) -> str:
    month, day, year = input_date.split('/')
    return '-'.join((day.zfill(2), month.zfill(2), str(base_year + int(year)).zfill(4)))


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
