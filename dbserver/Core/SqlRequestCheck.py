def check_len_of_rows(len_row, len_new_row):
    if len_row > len_new_row:
        return 1
    elif len_row < len_new_row:
        return -1
    else:
        return 0


def check_null(row, new_row):
    row_flag, new_row_flag = False, False
    for i in row:
        if None in i:
            row_flag = True
    for i in new_row:
        if None in i:
            new_row_flag = True
    if row_flag != new_row_flag:
        return -1
    return 0


def check_attributes(row, new_row):
    for i in range(0, len(row)):
        if len(row[i]) < len(new_row[i]):
            return -1
        elif len(row[i]) > len(new_row[i]):
            return 1
    return 0


def find_error(rows, new_rows):
    check_len_res = check_len_of_rows(len(rows), len(new_rows))
    if check_len_res == 1:
        return 'Недостаточно данных'
    elif check_len_res == -1:
        return 'Слишком много данных'
    else:
        check_atr_res = check_attributes(rows, new_rows)
        if check_atr_res == -1:
            return 'Недостаточно данных в атрибутах'
        elif check_atr_res == -1:
            return 'Недостаточно данных в атрибутах'
        else:
            return 'Неверный результат'
