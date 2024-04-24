
def originalQuestion(data : list, original_cubes : dict) -> int:
    result = 0
    for line in data:
        tries = line.split(';')
        val = True
        num = int(tries[0].split(':')[0].split(' ')[-1])
        tries[0] = tries[0].split(':')[1]
        tries = [x.strip() for x in tries]
        for element in tries:
            if not val:
                break
            colors_elements = element.split(',')
            colors_elements = [x.strip() for x in colors_elements]
            for elem in colors_elements:
                values = elem.split(' ')
                if original_cubes[values[-1]] < int(values[0]):
                    val = False
                    break
        if val:
            result += num
    return result


def followUpQuestion(data : list, original_cubes : dict, temp_colors_values : dict) -> int:
    result = 0
    for line in data:
        for key in temp_colors_values.keys():
            temp_colors_values[key] = 0
        tries = line.split(';')
        tries[0] = tries[0].split(':')[1]
        tries = [x.strip() for x in tries]
        for element in tries:
            colors_elements = element.split(',')
            colors_elements = [x.strip() for x in colors_elements]
            for elem in colors_elements:
                values = elem.split(' ')
                temp_colors_values[values[-1]] = max(temp_colors_values[values[-1]], int(values[0]))
        temp_prod = 1
        for value in temp_colors_values.values():
            temp_prod *= value
        result += temp_prod
    return result



def  main() -> None:
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()

    original_cubes = {
        'red' : 12,
        'green' : 13,
        'blue' : 14
    }

    temp_colors_values = {
        'red' : 0,
        'green' : 0,
        'blue' : 0
    }

    print(f"{'Original Question Result':<28}: {originalQuestion(data, original_cubes)}")

    print(f"{'Follow up Question Result':<28}: {followUpQuestion(data, original_cubes, temp_colors_values)}")


if __name__ == "__main__":
    main()
