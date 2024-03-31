import requests

mytoken = 'ppo_10_15261'
headers = {
    "X-Auth-Token": mytoken
}


def extract_floor_number(floor_name):
    return int(floor_name.split("_")[1])


def get_info(day, month, year):
    url = f"https://dt.miet.ru/ppo_it_final?day={day}&month={month}&year={year}"
    sp = []
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            response_json = response.json()
            print(response_json["message"]["windows"]["data"])
            print(response_json["message"]["flats_count"]["data"])
            floors = response_json["message"]["windows"]["data"]
            count = response_json["message"]["flats_count"]["data"]
            floor_to_und = response_json["message"]["windows"]["data"]["floor_1"]
            print(floor_to_und)
            count_room = len(floor_to_und) // int(count)
            print(count_room)

            sorted_floors = sorted(floors.items(), key=lambda x: extract_floor_number(x[0]))
            fin_l = ''
            for floor, people in sorted_floors:
                for i in people:
                    k = ''
                    if i == True:
                        k += '1'
                    else:
                        k += '0'
                    fin_l += k
                fin_l += ' '
            light = fin_l[::-1]
            q22 = fin_l.split(" ")
            print(len(q22))
            pl = fin_l.split(' ')
            print(pl)
            q1 = 0
            for j in pl:
                q1 += len(str(j))

            con = q1 // count_room
            rooms = ['1' * con] * len(floors)
            return light, light.replace('0', '1')

            #with open('lights.csv', 'w') as f:
            #    f.write(fin_l[::-1])

            # with open('rooms.csv', 'w') as f:
            #     f.write(fin_r)

        except ValueError:
            print("Response is not a valid JSON")


print(get_info('25','01','23'))