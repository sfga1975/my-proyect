# TODO


def run(func, func_args, func_kwargs):
    return assert_positive(func)(*func_args, **func_kwargs)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
