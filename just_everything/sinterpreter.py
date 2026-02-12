import sys

class SInterpreter:
    def __init__(self):
        self.values_dict = {}
        self.stack = []


    def cycle(self):
        for l in sys.stdin:
            l = l.strip()
            if not l:
                continue

            parts = l.split()

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
                if len(self.stack) < 2:
                    self.error("ASSIGN")
                
                value = self.stack.pop()
                var_name = self.stack.pop()

                if not isinstance(var_name, str):
                    self.error("ASSIGN")
                
                self.values_dict[var_name] = value

            elif operator == "PRINT":
                if len(self.stack) < 1:
                    self.error("PRINT")

                value = self.stack[-1]

                if isinstance(value, str):
                    value = self.values_dict.get(value, 0)

                print(value)

            else:
                self.error(operator)

        

    def error(self, operator):
        print(f"Error for operator: {operator}")
        sys.exit(0)


    def push(self, operand):
        if isinstance(operand, int):
            self.stack.append(operand)
        elif operand.isdigit():
            self.stack.append(int(operand))
        else:
            self.stack.append(self.values_dict.get(operand, 0))


    def add(self):
        if len(self.stack) < 2:
            self.error("ADD")
        a = self.stack.pop()
        b = self.stack.pop()

        if isinstance(a, str):
            a = self.values_dict.get(a, 0)
        if isinstance(b, str):
            b = self.values_dict.get(b, 0)

        a = int(a)
        b = int(b)

        self.stack.append(b + a)


    def sub(self):
        if len(self.stack) < 2:
            self.error("SUB")
        a = self.stack.pop()
        b = self.stack.pop()

        if isinstance(a, str):
            a = self.values_dict.get(a, 0)
        if isinstance(b, str):
            b = self.values_dict.get(b, 0)

        a = int(a)
        b = int(b)

        self.stack.append(b - a)


    def mult(self):
        if len(self.stack) < 2:
            self.error("MULT")
        a = self.stack.pop()
        b = self.stack.pop()

        if isinstance(a, str):
            a = self.values_dict.get(a, 0)
        if isinstance(b, str):
            b = self.values_dict.get(b, 0)

        a = int(a)
        b = int(b)

        self.stack.append(b * a)


    def assign(self):
        if len(self.stack) < 2:
            self.error("ASSIGN")
        
        value = self.stack.pop()
        var_name = self.stack.pop()
        if isinstance(value, str):
            value = self.values_dict.get(value, 0)

        if not isinstance(var_name, str):
            self.error("ASSIGN")
        
        self.values_dict[var_name] = value

    def print_top_of_stack(self):
        if len(self.stack) < 1:
            self.error("PRINT")
        value = self.stack[-1]
        if isinstance(value, str):
            value = self.values_dict.get(value, 0)
        print(value)

if __name__ == "__main__":
    interpreter = SInterpreter()
    interpreter.cycle()