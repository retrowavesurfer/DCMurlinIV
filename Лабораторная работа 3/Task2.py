def find_common_participants(gr1, gr2):
    f = gr1.split("|")
    s = gr2.split("|")
    first = set(f)
    second = set(s)
    print(first.intersection(second))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
find_common_participants(participants_first_group, participants_second_group)
