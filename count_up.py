def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    x = range(start, stop)
    for n in x:
        print(n)
    print(stop)


count_up(5, 7)
