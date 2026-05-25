import re

def clean_filename(name):

    name = name.strip()

    name = re.sub( r'[\\/*?:"<>|]','', name )

    name = re.sub( r'\s+', '_', name )

    return name[:40]