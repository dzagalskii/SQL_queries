def check_len_of_rows(len_row, len_new_row):
    if len_row > len_new_row:
        return 1
    elif len_row < len_new_row:
        return -1
    else:
        return 0


def find_error(rows, new_rows):
    check_len_res = check_len_of_rows(len(rows), len(new_rows))
    if check_len_res == 1:
        print('Not enough data')
        return
    elif check_len_res == -1:
        print('Too much data')
        return
    else:
        print('Unknown error')
        return


    print('{} in rows, {} in new_rows'.format(len(rows), len(new_rows)))
