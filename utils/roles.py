def get_role(number: int):
    for rank, invites in roles.items():
        if number >= invites:
            return rank
    return None


def get_next_role(invites: int):
    if invites < 1:
        return 'Rank6', 1
    if invites < 3:
        return 'Rank5', 3
    if invites < 5:
        return 'Rank4', 5
    if invites < 10:
        return 'Rank3', 10
    if invites < 50:
        return 'Rank2', 50
    if invites < 100:
        return 'Rank1', 100
    return 'Maximum rank', 0


roles = {
    'Rank1': 100,
    'Rank2': 50,
    'Rank3': 10,
    'Rank4': 5,
    'Rank5': 3,
    'Rank6': 1
}
