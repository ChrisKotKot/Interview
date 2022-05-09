import datetime

get_input = True
dateformat = ('%Y,%m,%d,%H,%M')


def date_count(date_from, date_to):
    date_time_from = date_from
    result_date_time = date_time_from - date_to
    seconds = result_date_time.total_seconds()
    days = abs(seconds/60/60/24)
    #months = abs(days/30) # Przyjmuje ze kazdy miesiac ma 30 dni
    full_days = abs(int(days))
    hours = ((days - full_days) * 24)
    full_hours = abs(int(hours))
    minutes = (hours - int(hours)) * 60
    full_minutes = abs(int(minutes))

    date_in_future = result_date_time.total_seconds() >= 0
    if date_in_future:
        print(f"\tZdarzenie odbędzie się za {full_days} dni {full_hours} godzin {full_minutes} minut.")
    else:
        print(f"\tZdarzenie odbyło się {full_days} dni {full_hours} godzin {full_minutes} minut temu.")


def date_check(user_input=None):
    try:
        valid_time = datetime.datetime.strptime(user_input, dateformat)
        return valid_time

    except ValueError:
        return False


print("---\taby wyjść wpisz exit--")
if __name__ == '__main__':
    while get_input:
        user_date_from = input("Podaj datę początkową w formacie yyyy,m,d,H,M:")
        if user_date_from == 'exit':
            exit()
        else:
            date_from_valid = date_check(user_input=user_date_from)

            if date_from_valid:
                date_from = datetime.datetime.strptime(user_date_from, '%Y,%m,%d,%H,%M')
                print("---Poprawny format daty początkowej---")
            else:
                print("Niepoprawna data początkowa")
                continue

        user_date_to = input("Podaj datę końcową w formacie yyyy,m,d,H,M albo kliknij enter, aby pobrać datę aktualną! ")
        if user_date_to == '':
            date_to_valid = True
            date_to = datetime.datetime.now()
        elif user_date_to == 'exit':
            exit()
        else:
            date_to_valid = date_check(user_input=user_date_to)

            if date_to_valid:
                date_to = datetime.datetime.strptime(user_date_to, '%Y,%m,%d,%H,%M')
                print("---Poprawny format daty końcowej---")
            else:
                print("Niepoprawna data końcowa")

        if date_from_valid and date_to_valid:
            get_input = False

            date_count(date_from, date_to)


