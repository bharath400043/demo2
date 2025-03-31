import csv
import re

def _update_num(mob_num):
    upd_num = '(%s) %s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', mob_num))
    return upd_num

def _get_user_data(user_data):
    is_num = any(char.isdigit() for char in user_data[2])
    if is_num:
        if user_data[2].isnumeric():
            num_format = _update_num(user_data[2])
            user_data[2] = num_format
        user_data[2], user_data[3] = user_data[3], user_data[2]
    return user_data

def _write_to_out_file(fname, phone_data, out_file):
    heading = "Matching for: " + fname
    out_file.write(heading)
    row_no = 1
    for data in phone_data.values():
        if fname in (data[0], data[1]):
            res_rec = "Result " + str(row_no) + ": {},{},{},{}".format(data[0], data[1],data[2], data[3])
            out_file.write('\n')
            out_file.write(res_rec)
            row_no += 1
    if row_no == 1:
        out_file.write('\n')
        out_file.write("No results found")
    out_file.write('\n')

def read_data_from_csv():
    phone_data = {}
    with open("phone_dataset.csv") as f:
        reader = csv.reader(f)
        counter = 1
        for row in reader:
            phone_data[counter] = _get_user_data(row[0].split(', '))
            counter += 1
    return phone_data

def write_data_to_txt(p_data):
    with open("query.txt") as in_data:
        names = in_data.readlines()
        content = [x.rstrip() for x in names]
        out_file = open("output.txt", 'w')
        for first_name in content:
            _write_to_out_file(first_name, p_data, out_file)

if __name__ == '__main__':
    phone_data = read_data_from_csv()

    write_data_to_txt(phone_data)
    print("Success")