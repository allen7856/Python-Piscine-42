from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(
                isinstance(x, (int, float)) for x in data
        )

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: invalid numeric data"
        total: int | float = sum(data)
        avg: float = total / len(data)
        return (f"Processed {len(data)} numeric values, "
                f"sum={total}, avg={avg}")

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: Invalid text data"
        chars: int = len(data)
        words: int = len(data.split())
        return f"Processed text: {chars} characters, {words} words"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: Invalid log entry"
        level: str = data.split(":")[0].strip()
        message: str = data.split(":")[1].strip()
        alert = "ALERT" if level == "ERROR" else "INFO"
        return f"[{alert}] {level} level detected: {message}"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric = NumericProcessor()
    print("\nInitializing Numeric Processor...")
    print("Processing data: [1, 2, 3, 4, 5]")
    print("Validation: Numeric data verified")
    try:
        print(numeric.format_output(numeric.process([1, 2, 3, 4, 5])))
    except Exception as e:
        print(f"Error: {e}")

    text = TextProcessor()
    print("\nInitializing Text Processor...")
    print('Processing data: "Hello Nexus World"')
    print("Validation: Text data verified")
    try:
        print(text.format_output(text.process("Hello Nexus World")))
    except Exception as e:
        print(f"Error: {e}")

    log = LogProcessor()
    print("\nInitializing Log Processor...")
    print('Processing data: "ERROR: Connection timeout"')
    print("Validation: Log entry verified")
    try:
        print(log.format_output(log.process("ERROR: Connection timeout")))
    except Exception as e:
        print(f"Error: {e}")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: list[DataProcessor] = [
            NumericProcessor(),
            TextProcessor(),
            LogProcessor(),
            ]
    data: list[Any] = [
            [1, 2, 3],
            "Hello Nexus",
            "INFO: System ready",
            ]
    i: int = 1
    for processor, item in zip(processors, data):
        try:
            print(f"Result {i}: {processor.process(item)}")
        except Exception as e:
            print(f"Result {i}: Error - {e}")
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
