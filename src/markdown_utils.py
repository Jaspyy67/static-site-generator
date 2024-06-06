

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith('# '):  # This finds the h1 header
            return line[2:]  # Extracts the title text after '# '
    raise Exception("No h1 header found")
