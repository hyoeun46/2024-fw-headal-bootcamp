class Unit:
    def __init__(self, s, t):
        self.s = s
        self.t = t

    def is_subsequence(self):
        s_index, t_index = 0, 0
        while s_index < len(self.s) and t_index < len(self.t):
            if self.s[s_index] == self.t[t_index]:
                s_index += 1
            t_index += 1

        return s_index == len(self.s)
    
    @staticmethod
    def process_input():
        try:
            while True:
                line = input().strip()
                if not line:
                    break
                s, t = line.split()

                test = Unit(s, t)

                if test.is_subsequence():
                    print("Yes")
                else:
                    print("No")

        except EOFError:
            pass

Unit.process_input()