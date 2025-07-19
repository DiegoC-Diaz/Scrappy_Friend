import re


def find_file_named(target_text,files):
    found_files=[]
    pattern = re.compile(r'\b' + re.escape(target_text) + r'\b', re.IGNORECASE)
    for file in files:
        if pattern.search(file):
            found_files.append(file)
    return found_files
         
def extrac_file_id(html_body):
    # This regex pattern finds all occurrences of the data-api-endpoint that match the Canvas API file structure.
    # It uses a capture group `(\d+)` to extract the numerical file ID from the URL.
    pattern = re.compile(r'data-api-endpoint="[^"]*?/api/v1/courses/\d+/files/(\d+)"')
    # re.findall returns a list of all the captured groups.
    ids = pattern.findall(html_body)
    return ids
