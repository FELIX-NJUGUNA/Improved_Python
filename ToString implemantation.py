class MLType:
    def __init__(self, type_var=None, arg_type=None, result_type=None):
        self.type_var = type_var
        self.arg_type = arg_type
        self.result_type = result_type

    def toString(self):
        if self.type_var is not None:
            return self.type_var
        elif self.arg_type is not None and self.result_type is not None:
            return f"({self.arg_type.toString()} -> {self.result_type.toString()})"
        else:
            raise Exception("Invalid type expression")


# Example usage
t1 = MLType(type_var="t1")
t2 = MLType(type_var="t2")
t3 = MLType(type_var="t3")

print(t1.toString())  # Output: t1
print(t2.toString())  # Output: t2
print(t3.toString())  # Output: t3
print(MLType(arg_type=t1, result_type=t2).toString())  # Output: (t1 -> t2)
print(MLType(arg_type=t3, result_type=t1).toString())  # Output: (t3 -> t1)
