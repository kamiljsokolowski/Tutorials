def is_reverse(i, j):
    """
    Convert 2-digit numbers to strings and check if they are palindromic.
    If one of the numbers has less then 2 digits, fill with zeros.
    """
    str_i = str(i)
    str_j = str(j)
    if len(str_i) < 2:
        str_i = str_i.zfill(2)
    if len(str_j) < 2:
        str_j = str_j.zfill(2)
    return str_j[::-1] == str_i

age_diff = 15
d_age = 0

while age_diff <= 50:
    reversible = 0
    for d_age in range(0,80):
        m_age = d_age + age_diff
        if is_reverse(d_age, m_age):
            reversible += 1
            if reversible == 6:
                print 'The daughter is', d_age, 'years old'
            if reversible == 8:
                print 'At the 8th time the daughter will be', d_age, 'years old and the mother will be', m_age, 'years old'
                break
        d_age += 1
    age_diff += 1


