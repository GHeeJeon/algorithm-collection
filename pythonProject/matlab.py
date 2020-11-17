from utility import *


def dump_function_xy(function, x_range, x_name="", y_name=""):
    """
    :param function: (Int) -> Int
    :param x_range: Int range
    :param x_name:
    :param y_name:
    :return:
    """

    x = list(x_range)
    y = list(map(function, x_range))

    if x_name != "":
        print(x_name + " = " + str(x))

    if y_name != "":
        print(y_name + " = " + str(y))


def dump_sorting_function(name, sorting_function, x_range):
    print(name)

    dump_function_xy(
        lambda size_of_collection: elapsed_time(lambda: sorting_function(random_list(size_of_collection))),
        x_range,
        "number_of_samples",
        "elapsed_time_on_random_list"
    )

    dump_function_xy(
        lambda size_of_collection: elapsed_time(lambda: sorting_function(ordered_list(size_of_collection))),
        x_range,
        "",
        "elapsed_time_on_ordered_list"
    )

    dump_function_xy(
        lambda size_of_collection: elapsed_time(lambda: sorting_function(reverse_ordered_list(size_of_collection))),
        x_range,
        "",
        "elapsed_time_on_reverse_ordered_list"
    )

    print("plot(number_of_samples, smoothdata(elapsed_time_on_random_list), number_of_samples, smoothdata(elapsed_time_on_ordered_list), number_of_samples, smoothdata(elapsed_time_on_reverse_ordered_list))")
