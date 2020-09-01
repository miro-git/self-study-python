def covert_to_float_and_sum_up(list):
    floats = [float(i) if isinstance(i, str) else i for i in list]
    return sum(floats)

print(covert_to_float_and_sum_up(['2.3','5.1','1.3']))