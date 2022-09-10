# assume value is a decimal
def transform_to_rupiah_format(value):
    str_value = str(value)
    separate_decimal = str_value.split(".")
    after_decimal = separate_decimal[0]
    before_decimal = separate_decimal[1]

    reverse = after_decimal[::-1]
    temp_reverse_value = ""

    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value = temp_reverse_value + val + "."
        else:
            temp_reverse_value = temp_reverse_value + val

    temp_result = temp_reverse_value[::-1]

    return "Rp " + temp_result + ",0" + before_decimal


def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3:
        return 'Rp ' + y 
    else:
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + '.' + p 


# untuk menguji code diatas atau proses debugging, gunakan:
if __name__ == '__main__':
    print(formatrupiah(1000000))
