
def print_table(data: list[list]) -> None:
    """
    Выводит список списков в виде таблицы.

    Args:
        data: 'Место, номер, имя, фамилия и результат'
        как названия колонок и значения для них
    """
    col_width = [max(len(str(x)) for x in col) for col in zip(*data)]
    for row in data:
        print("  ".join(str(x).ljust(width) for x, width in zip(
            row, col_width)))


def write_to_json_file(path_to_file: str, result_list: list) -> None:
    """
    Записывает Место, номер, имя, фамилия и результат в JSON файл.

    Args:
        path_to_file: Путь к файлу.
        result_list: Место, номер, имя, фамилия и результат.
    """
    dict_json = dict((str(item[0]), {'Нагрудный номер': str(item[1]),
                                     'Имя': item[2],
                                     'Фамилия': item[3],
                                     'Результат': item[4]})
                     for item in result_list)
    dict_json = str(dict_json).replace("'", "\"").replace('{', '{\n\t')
    dict_json = dict_json.replace("}, ", "\n\t},\n\t").replace(", ", ",\n\t\t")
    dict_json = dict_json.replace(": {\n", ": {\n\t").replace("}}", "\n\t}\n}")
    with open(path_to_file, "w", encoding="utf-8-sig") as file:
        file.write(dict_json)
