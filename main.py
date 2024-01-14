import readfile as rf
import modificationvariable as mv
import output as out


def main():
    content = rf.read_txt("results_RUN.txt")
    content = mv.set_result_time(content)
    result_list = content
    dict_json = rf.get_dict_json("competitors2.json")
    result_list = mv.append_info_from_json(dict_json, result_list)
    head = ["Занятое место", "Нагрудный номер", "Имя", "Фамилия", "Результат"]

    out.print_table([head] + result_list)
    out.write_to_json_file("final_results.json", result_list)


if __name__ == "__main__":
    main()
