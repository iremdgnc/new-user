import json


def get_user_details():
    details_list = []
    count = 0
    while True:
        details = input("UserID:"), input("Name:"), input("Age:")
        details_list.append(details)
        count += 1
        if count == 2:
            return details_list


def get_user_details_json_file_write():
    with open('listfile.txt', 'w') as file:
        return json.dump(get_user_details(), file)


def get_user_details_json_file_read():
    with open('listfile.txt', 'r') as file:
        return json.load(file)


def run_script():
    for input in get_user_details_json_file_read():
        user_id = input[0]
        user_name = input[1]
        age = input[2]
        print (("User ID:" + user_id), ("Name:" + user_name), ("Age:" + age))


if __name__ == "__main__":
    get_user_details_json_file_write()
    print(get_user_details_json_file_read())

