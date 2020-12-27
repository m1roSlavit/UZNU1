import datetime
base = []


def add_to_base(last_name, first_name, patronymic, year_of_birth, type_of_crime, term_of_punishment):
    infos = {
        "last_name": last_name,
        "first_name": first_name,
        "patronymic": patronymic,
        "year_of_birth": year_of_birth,
        "type_of_crime": type_of_crime,
        "term_of_punishment": term_of_punishment,
        "__date_of_update": datetime.date.today(),
        "__date_of_create": datetime.date.today()
    }
    def delete_and_upd(inf):
        del base[inf[0]["__id"]]
        infos["__date_of_create"] = inf[0]["__date_of_create"]

    if search_in_base(infos):
        search_in_base(infos, delete_and_upd)
    base.append(infos)
    return infos


def search_in_base(data, callback=None):
    res = []
    for id in range(len(base)):
        flag = 1
        for param in data:
            if base[id][param] != data[param]:
                flag = 0
        if flag:
            inf = base[id].copy()
            inf.update({"__id": id})
            res.append(inf)

    if callback:
        callback(res)
    else:
        return res


add_to_base("alg", 10, "Olga", 4, "Olga", 4)
add_to_base("algfd", 103, "Olga", 4, "Olga", 4)
add_to_base("algfd", 103, "Olga", 4, "Olga", 4)
add_to_base("algfd", 103, "Olga", 4, "Olga", 4)
add_to_base("algfd", 103, "Olga", 5, "Olga", 4)
search_in_base({
    "patronymic": "Olga",
    "year_of_birth": 4
}, lambda data: print(data))

search_in_base({
}, lambda data: print(data))


# як оновити данні
# search_in_base({нараметри пошуку}, lambda data: add_to_base(змінений об'єкт))
