class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = int(num1) - int("0")
        n2 = int(num2) - int("0")
        return f"{n1*n2}"
        