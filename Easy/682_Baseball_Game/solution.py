class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record: List[str] = []
        result: int = 0
        for operation in operations:
            match operation:
                case "C":
                    record.pop()
                case "D":
                    record.append(str(int(record[-1]) * 2))
                case "+":
                    first = int(record[-1])
                    second = int(record[-2])
                    record.append(str(first + second))
                case _:
                    record.append(str(operation))
        for num in record:
            result += int(num)

        return result


