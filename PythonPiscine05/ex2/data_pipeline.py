

from abc import ABC, abstractmethod
from typing import Any, Protocol

class DataProcessor(ABC):
    @abstractmethod
    # Decides if it can handle data # Debe acceptar any y retornar True or False
    def can_process(self, data: Any) -> bool:
        pass

    @abstractmethod
    # Processes it #Child classes will override this con tipos mas específicos
    def process(self, data: Any) -> None:
        pass

class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...

class DataStream:
    def __init__(self):
        # Stores processors
        self.processors = []

    # Register processors, No type checking, polymorphism handles it
    def register_processor(self, proc):
        self.processors.append(proc)

    # Asking each processor, if they can handled OK if None of them, then Error
    def process_stream(self, stream):
        for element in stream:
            handled = False

            for proc in self.processors:
                if proc.can_process(element):
                    proc.process(element)
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - Can't process element in stream: {element}")

    def print_processors_stats(self):
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            print(f"{proc.name}: total {proc.total_processed} items processed, remaining {len(proc.buffer)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin):
        for proc in self.processors:
            data = proc.output(nb)
            if data:
                plugin.process_output(data)

class NumericProcessor(DataProcessor):
    def __init__(self):
        self.name = "Numeric Processor"
        self.total_processed = 0
        self.buffer = [] #Or list of stored items
        self.output_index = 0

    def can_process(self, data):
        return (
            isinstance(data, (int, float)) or
            (isinstance(data, list) and all(isinstance(x, (int, float)) for x in data))
        )
    def process(self, data):
        if isinstance(data, list):
            self.buffer.extend(data)
            self.total_processed += len(data)
        else:
            self.buffer.append(data)
            self.total_processed += 1

    def output(self, n: int):
        taken = self.buffer[:n]
        self.buffer = self.buffer[n:]

        result = []
        for value in taken:
            result.append((self.output_index, str(value)))
            self.output_index += 1
        return result

class TextProcessor(DataProcessor):
    def __init__(self):
        self.name = "Text Processor"
        self.total_processed = 0
        self.output_index = 0
        self.buffer = []
    
    def can_process(self, data):
        return (
            isinstance(data, str) or
            (isinstance(data, list) and all(isinstance(x, str) for x in data))
        )
    
    def process(self, data):
        if isinstance(data, list):
            self.buffer.extend(data)
            self.total_processed += len(data)
        else:
            self.buffer.append(data)
            self.total_processed += 1

    def output(self, n: int):
        taken = self.buffer[:n]
        self.buffer = self.buffer[n:]

        result = []
        for value in taken:
            result.append((self.output_index, str(value)))
            self.output_index += 1
        return result

class LogProcessor(DataProcessor):
    def __init__(self):
        self.name = "Log Processor"
        self.total_processed = 0
        self.buffer = []
        self.output_index = 0

    def can_process(self, data):
        return isinstance(data, list) and all(isinstance(x, dict) for x in data)

    def process(self, data):
        self.buffer.extend(data)
        self.total_processed += len(data)

    def output(self, n: int):
        taken = self.buffer[:n]
        self.buffer = self.buffer[n:]

        result = []
        for log in taken:
            formatted = f"{log['log_level']}: {log['log_message']}"
            result.append((self.output_index, formatted))
            self.output_index += 1
        return result



# No inheritance required por plugins. that's duck typing. It looks like a duck it is a duck
class CSVPlugin:
    def process_output(self, data):
        print("CSV Output:")
        values = [v for _, v in data]
        print(",".join(values))
        
class JSONPlugin:
    def process_output(self, data):
        print("JSON Output:")
        items = [f'"item_{i}": "{v}"' for i, v in data]
        print("{" + ", ".join(items) + "}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    ds = DataStream()
    print()
    print("Initialize Data Stream...")
    print()
    ds.print_processors_stats()
    print()
    # ALL processors here
    print("Registering Processors")
    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    stream = [
        "Hello world",
        [3.14, -1, 2.71],
        [{"log_level": "WARNING", "log_message": "Telnet access! Use ssh instead"},
        {"log_level": "INFO", "log_message": "User wil is connected"}],
        42,
        ["Hi", "five"]
    ]
    print("\nSend first batch of data on stream:", stream)
    print()
    ds.process_stream(stream)
    ds.print_processors_stats()


    new_stream = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [{"log_level": "ERROR", "log_message": "500 server crash"},
        {"log_level": "NOTICE", "log_message": "Certificate expires in 10 days"}],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, CSVPlugin())
    print()
    ds.print_processors_stats()
    print("\nSend another batch of data:", new_stream)
    ds.process_stream(new_stream)
    ds.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, JSONPlugin())
    print()
    ds.print_processors_stats()
