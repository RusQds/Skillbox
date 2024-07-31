def new_base(players):
    new_players = list(tuple(i_player + i_point) for i_player, i_point in players.items())
    return new_players

players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

print(new_base(players))

# Принято
