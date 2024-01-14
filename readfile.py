def read_txt(path_to_file: str) -> list[str]:
    """
    Читаем файл, разбиваем на список и возвращаем

    Args:
        path_to_file: Путь к файлу

    Returns:
        Возвращаем список
    """
    with open(path_to_file, "r", encoding="utf-8-sig") as file:
        content = file.read()
    content = content.replace('\ufeff', '')
    content = content.rstrip('\n')
    content = content.split('\n')
    return content


def get_dict_json(path_to_file: str) -> dict:
    """
    Заполняем словарь из json'a

    Args:
        path_to_file: Путь к файлу

    Returns:
        Словарь из данными из json'a
    """
    with open(path_to_file, "r", encoding="utf-8-sig") as file:
        content = file.read()
    content = content.replace('\ufeff', '')
    dict_json = eval(content)
    return dict_json
