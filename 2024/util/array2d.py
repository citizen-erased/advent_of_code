def array_2d_get_or_default(array, w, h, x, y, default = None):
    if 0 <= x < w and 0 <= y < h:
        return array[y][x]
    return default


def array_2d_print(array, column_divider=""):
    # Calculate the maximum width of each column
    col_widths = [max(len(str(item)) for item in col) for col in zip(*array)]

    for row in array:
        formatted_row = column_divider.join(f"{str(item).ljust(col_widths[i])}" for i, item in enumerate(row))
        print(formatted_row)
