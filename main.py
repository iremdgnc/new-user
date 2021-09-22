import json


def get_user_details():
    details_list = []
    a = int(input("Kaç kullanıcı girilecek ?" + "\n"))
    count = 0
    while True:
        details = input("UserID:"), input("Name:"), input("Age:")
        details_list.append(details)
        count += 1
        if count == a:
            return details_list


def get_user_details_json_file_read():
    with open('listfile.txt', 'r') as file:
        return json.load(file)


def save_data(input_values):
    array = get_user_details_json_file_read()
    for i in input_values:
        array.append(i)

    with open('listfile.txt', 'w') as file:
        return json.dump(array, file)


def run_script():
    users_details = get_user_details()
    save_data(users_details)

    for input in get_user_details_json_file_read():
        user_id = input[0]
        name = input[1]
        age = input[2]
        print("Kullanıcıların bilgileri başarı ile kaydedildi\n" + "UserId:" + user_id + "\n", "Name: " + name + "\n",
              "Age: " + age + "\n")

    # kullanıcadan bilgileri al tamam
    # alınan bilgileri listeye yaz tamam
    # yazılan bilgileri oku tamam
    # return txt dosyasındaki bilgileri terminal ekrana basarak verecek


if __name__ == "__main__":
    # run_script()
    save_data(get_user_details())
