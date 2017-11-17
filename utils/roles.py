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


def get_previous_role(number: int):
    invites_keys = roles.keys()
    invites_keys = sorted(invites_keys)
    previous = 0
    for invites_needed in invites_keys:
        if number < invites_needed:
            return roles[previous], previous
        previous = invites_needed

roles = {
    0: 'Free',
    2: 'Noob',
    10: 'CryptoNoob',
    25: 'Beginner',
    50: 'CryptoNova',
    80: 'CryptoMaster',
    150: 'CryptoExpert'
}
