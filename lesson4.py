def format_name(s):
    return s[:1].upper() + s[1:].lower()

def format_name2(s):
    return s.title()

print map(format_name2, ['adam', 'LISA', 'barT'])