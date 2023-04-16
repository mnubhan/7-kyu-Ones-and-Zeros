def binary_array_to_number(arr):
  s = [str(i) for i in arr]
  return int("".join(s), 2)

def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)
