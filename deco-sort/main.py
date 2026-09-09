# TODO


# DO NOT TOUCH THE CODE BELOW
def run(asc, func, func_args) -> list:
    if isinstance(func_args, dict):
        return sort(asc)(func)(**func_args)
    return sort(asc)(func)(*func_args)


if __name__ == '__main__':
    import vendor

    vendor.launch(run)
