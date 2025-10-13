import os


def get_cats_info(path: str):
    is_exist_file = os.path.isfile(path)
    if not is_exist_file:
        return []
    
    result = []

    with open(path, 'r', encoding="utf-8") as file:
        for i, line in enumerate(file):
            line = line.strip()
            if not line:
                continue
            try:
               id, name, age_str = line.split(',')
            except ValueError:
               pass

            result.append({
                "id": id,
                "name": name,
                "age": age_str
            })

    return result


cats_info = get_cats_info("test2File.txt")
print(cats_info)