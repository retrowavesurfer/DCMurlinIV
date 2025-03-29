list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
num_of_players = len(list_players)
mid = num_of_players // 2

team1 = list_players[:mid]
team2 = list_players[mid:]

print(team1)
print(team2)
