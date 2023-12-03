
class A:
    def print_a(self):
        print("A")

class B:
    def print_b(self):
        print("B")

# Heredamos A y B en C
class C(A, B):
    def print_c(self):
        print("C")

c = C()
