def findmethod(*datatypes, method) -> None:
    for datatype in datatypes:
        if hasattr(datatype, method):
            print(f"{datatype.__name__} \t-> {method}()")


findmethod(str, list, tuple, dict, set, method='__iter__')