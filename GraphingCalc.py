def plot(fx, inv="no", coefficient=1, constant=0, range_x=1):
    x = []
    y = []

    for i in range(range_x + 1):
        x.append(i)
        match fx:
            case "linear":
                y.append(coefficient * i + constant)
            case "quadratic":
                y.append(coefficient * (i ** 2) + constant)
            case "cubic":
                y.append(coefficient * (i ** 3) + constant)
            case _:
                y.append(coefficient * (i ** 2) + constant)

    if inv == "yes":
        switch = y
        y = x
        x = switch

    return [x, y]


