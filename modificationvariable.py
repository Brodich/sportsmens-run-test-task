def append_info_from_json(dict_json: dict, result_list: list) -> list[str]:
    """
    Добавление информации из словаря-из-джейзона в список,
    путем сопоставления индексов

    Args:
        dict_json: Словарь из джейсона
        result_list: Лист, номером и временем

    Returns:
        Список в котором теперь есть: Место, номер, имя, фамилия и результат
    """
    for sublist in result_list:
        number = str(sublist[0])
        if number in dict_json:
            sublist.append(dict_json[number]['Name'])
            sublist.append(dict_json[number]['Surname'])
    result_list.sort(key=lambda x: x[1])
    for index, element in enumerate(result_list):
        element.insert(0, index + 1)
        time = element.pop(2)
        element.append(time)
    return result_list


def get_result_time(start_time: str, finish_time: str) -> str:
    """
    Вычисляем разницу во времени между стартом и финишем

    Args:
        start_time: Время старта
        finish_time: Время финиша

    Returns:
        Результат в виде строки (MM:CC:мс)
    """
    sec_hours, sec_minuts, seconds, milisec = map(
        int, start_time.replace(',', ':').split(':'))
    sec_hours2, sec_minuts2, seconds2, milisec2 = map(
        int, finish_time.replace(',', ':').split(':'))

    total = (sec_hours * 3600 + sec_minuts * 60 + seconds) * 1000000 + milisec
    total2 = (sec_hours2 * 3600 + sec_minuts2 * 60 + seconds2) * 1000000 + milisec2
    diff_time = total2 - total

    seconds, milisec = divmod(diff_time, 1000000)
    minuts, seconds = divmod(seconds, 60)
    milisec = int(milisec / 10000)

    result_time = str(minuts).zfill(2) + ":" + str(
        seconds).zfill(2) + "," + str(milisec).zfill(2)
    return result_time


def set_result_time(content: list) -> list:
    """
    Удаляются start, finish, строчки с одинаковым номером.
    Заносится результат времени в список.

    Args:
        content: С номером, start/finish, временем.
    Returns:
        content: С номером и результатом времени.
    """
    for index, element in enumerate(content):
        content[index] = element.split()

    for index in range(0, len(content) - 1, 2):
        start_time = content[index][2]
        finish_time = content[index + 1][2]
        result_time = get_result_time(start_time, finish_time)
        content[index].append(result_time)
        content[index].pop(1)
        content[index].pop(1)
    del content[1::2]
    return content
