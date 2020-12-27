student_base = []

def add_to_base(subject_title, number_of_hours, teacher, rating):
    infos = {
        "subject_title": subject_title,
        "number_of_hours": number_of_hours,
        "teacher": teacher,
        "rating": rating
    }
    def delett(inf):
        del student_base[inf[0]["id"]]
    if search_in_base(infos):
        search_in_base(infos, delett)
    student_base.append(infos)
    return infos


def search_in_base(data, callback=None):
    res = []
    for id in range(len(student_base)):
        flag = 1
        for param in data:
            if student_base[id][param] != data[param]:
                flag = 0
        if flag:
            inf = student_base[id].copy()
            inf.update({"id": id})
            res.append(inf)

    if callback:
        callback(res)
    else:
        return res


add_to_base("alg", 10, "Olga", 4)
add_to_base("algfd", 103, "Olga", 4)
add_to_base("algfd", 103, "Olga", 4)
add_to_base("algfd", 103, "Olga", 4)
add_to_base("algfd", 103, "Olga", 5)
search_in_base({
    "teacher": "Olga",
    "rating": 4
}, lambda data: print(data))

search_in_base({
}, lambda data: print(data))
