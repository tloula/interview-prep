def power_of_two(num):
    bin_str = "{0:b}".format(num)
    return bin_str.count("1") == 1

print(power_of_two(8))