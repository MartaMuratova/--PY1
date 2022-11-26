import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter, new_line) -> list[dict]:
    with open(filename) as f:
        f.readline()
        ll = []
        for pos, line_ in enumerate(f):
            column = line_.strip(new_line).split(delimiter)
            if pos == 0:
                title = column
                continue

            ll.append({})

            for a, b in enumerate(title):

                ll[-1][title[a]] = column[a]

    return ll


print(json.dumps(csv_to_list_dict(INPUT_FILE, ",", "\n"), indent=4))
