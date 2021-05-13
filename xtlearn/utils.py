def dump_pickle(variable, file_path: str, verbose: int = 0) -> None:
    """[summary]

    :param variable: [description]
    :type variable: [type]
    :param file_path: [description]
    :type file_path: str
    :return: [description]
    :rtype: [type]
    """
    result = False
    try:
        pickle.dump(variable, open(file_path, "wb"))
        if verbose > 0:
            print("[info] Variable successfully dumped!")
        result = True

    except Exception as err:
        print("[error]", err)

    return result


def load_pickle(file_path: str, verbose: int = 0):
    """[summary]

    :param file_path: [description]
    :type file_path: str
    :return: [description]
    :rtype: [type]
    """
    result = None
    try:
        result = pickle.load(open(file_path, "rb"))
        if verbose > 0:
            print("[info] Variable successfully load!")

    except Exception as err:
        print("[error]", err)

    return result
