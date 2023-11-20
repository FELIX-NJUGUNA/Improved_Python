class TypeExpr:
    def __init__(self):
        self.type_var = None
        self.arg_type = None
        self.result_type = None

    def __str__(self):
        if self.type_var is not None:
            return self.type_var
        elif self.arg_type is not None:
            return f"({self.arg_type} -> {self.result_type})"
        else:
            raise Exception("Invalid type expression")

    @staticmethod
    def new_type_var():
        count = 1
        while True:
            type_var = f"t{count}"
            if type_var not in used_type_vars:
                used_type_vars.add(type_var)
                return TypeExpr(type_var=type_var)
            count += 1


used_type_vars = set()

t1 = TypeExpr.new_type_var()
t2 = TypeExpr.new_type_var()
t3 = TypeExpr.new_type_var()

print(t1)  # Output: t1
print(t2)  # Output: t2
print(t3)  # Output: t3
print(TypeExpr(arg_type=t1, result_type=t2))  # Output: (t1 -> t2)
print(TypeExpr(arg_type=t3, result_type=t1))  # Output: (t3 -> t1)
