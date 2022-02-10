# pretend like this is an external package containing the logic we want to wrap
import typing as t


def sum_inputs(input_data: t.List[int]) -> int:
    return sum(input_data)


def sum_input_nested(input_data: t.List[t.Dict]) -> int:
    result = 0
    for data in input_data:
        print("data label", data["label"], "value", data["value"])
        result += data["value"]
    return result
