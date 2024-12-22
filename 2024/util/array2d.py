def array_2d_create(w, h, value=None):
    return [[value for _ in range(w)] for _ in range(h)]

def array_2d_create_from_string(str):
    map = [[c for c in line.strip()] for line in str.splitlines() if line != ""]
    w, h = len(map[0]), len(map)
    return map, w, h
    
def array_2d_get_or_default(array, w, h, x, y, default = None):
    if 0 <= x < w and 0 <= y < h:
        return array[y][x]
    return default

def array_2d_index_of(array, element):
    h = len(array)
    w = len(array[0])
    for y in range(h):
        for x in range(w):
            if array[y][x] == element:
                return (x, y)
    return None

def array_2d_print(array, column_divider=""):
    # Calculate the maximum width of each column
    col_widths = [max(len(str(item)) for item in col) for col in zip(*array)]

    for row in array:
        formatted_row = column_divider.join(f"{str(item).ljust(col_widths[i])}" for i, item in enumerate(row))
        print(formatted_row)
