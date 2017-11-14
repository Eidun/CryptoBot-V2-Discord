def get_role(number: int):
    invites_keys = roles.keys()
    invites_keys = sorted(invites_keys, reverse=True)
    for invites_needed in invites_keys:
        if number >= invites_needed:
            return roles[invites_needed]
    return None


def get_next_role(number: int):
    invites_keys = roles.keys()
    invites_keys = sorted(invites_keys)
    for invites_needed in invites_keys:
        if number < invites_needed:
            return roles[invites_needed], invites_needed

roles = {
    100: 'Rank1',
    50: 'Rank2',
    10: 'Rank3',
    5: 'Rank4',
    3: 'Rank5',
    1: 'Rank6'
}
