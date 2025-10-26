

def make_full_name(given_name, family_name):
     return f"{family_name}; {given_name}"

def extract_family_name(full_name):
    parts = full_name.split("; ")
    return parts[0].strip()

def extract_given_name(full_name):
    parts = full_name.split("; ")
    return parts[1].strip()
