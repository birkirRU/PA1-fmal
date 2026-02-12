import sys

class SInterpreter:
    def __init__(self):
        self.values_dict = {}
        self.stack = []


    def cycle(self):
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            operator = parts[0]

            if operator == "PUSH":
                if len(parts) != 2:
                    self.error("PUSH")

                operand = parts[1]

                if operand.isdigit():
                    self.stack.append(int(operand))
                else:
                    self.stack.append(operand)

            elif operator == "ADD":
                self.add()

            elif operator == "SUB":
                self.sub()

            elif operator == "MULT":
                self.mult()

            elif operator == "ASSIGN":
                self.assign()

            elif operator == "PRINT":
                self.do_print()

            else:
                self.error(operator)


    def get_value(self, item):
        if isinstance(item, int):
            return item
        return self.values_dict.get(item, 0)


    def add(self):
        if len(self.stack) < 2:
            self.error("ADD")

        a = self.get_value(self.stack.pop())
        b = self.get_value(self.stack.pop())

        self.stack.append(b + a)


    def sub(self):
        if len(self.stack) < 2:
            self.error("SUB")

        a = self.get_value(self.stack.pop())
        b = self.get_value(self.stack.pop())

        self.stack.append(b - a)


    def mult(self):
        if len(self.stack) < 2:
            self.error("MULT")

        a = self.get_value(self.stack.pop())
        b = self.get_value(self.stack.pop())

        self.stack.append(b * a)


    def assign(self):
        if len(self.stack) < 2:
            self.error("ASSIGN")

        value = self.get_value(self.stack.pop())
        var_name = self.stack.pop()

        if not isinstance(var_name, str):
            self.error("ASSIGN")

        self.values_dict[var_name] = value


    def do_print(self):
        if len(self.stack) < 1:
            self.error("PRINT")

        value = self.get_value(self.stack.pop())
        print(value)


    def error(self, operator):
        print(f"Error for operator: {operator}")
        sys.exit()


if __name__ == "__main__":
    interpreter = SInterpreter()
    interpreter.cycle()
