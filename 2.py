# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator = ","):
    participants1 = group1.split(separator)
    participants2 = group2.split(separator)

    common_participants = set(participants1) & set(participants2)
    sort_common_participants=sorted(common_participants)

    return sort_common_participants


participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
print(common_participants)

# TODO Провеьте работу функции с разделителем отличным от запятой
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(common_participants)