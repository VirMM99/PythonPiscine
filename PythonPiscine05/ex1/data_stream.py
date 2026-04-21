

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    # Decides if it can handle data
    # Debe acceptar any y retornar True or False
    def can_process(self, data: Any) -> bool:
        pass

    @abstractmethod
    # Processes it #Child classes will override this
    # con tipos mas específicos
    def process(self, data: Any) -> None:
        pass


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
                print(
                    "DataStream error -"
                    f"Can't process element in stream: {element}"
                    )

    def print_processors_stats(self):
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            print(
                f"{proc.name}: total {proc.total_processed}"
                f"items processed, remaining {len(proc.buffer)} on processor"
                )


class NumericProcessor(DataProcessor):
    def __init__(self):
        self.name = "Numeric Processor"
        self.total_processed = 0
        self.buffer = []  # Or list of stored items

    def can_process(self, data):
        return (
            isinstance(data, (int, float))
            or isinstance(data, list)
            and all(isinstance(x, (int, float)) for x in data)
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
        return taken


class TextProcessor(DataProcessor):
    def __init__(self):
        self.name = "Text Processor"
        self.total_processed = 0
        self.buffer = []

    def can_process(self, data):
        return (
            isinstance(data, str)
            or (isinstance(data, list)
                and all(isinstance(x, str) for x in data))
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
        return taken


class LogProcessor(DataProcessor):
    def __init__(self):
        self.name = "Log Processor"
        self.total_processed = 0
        self.buffer = []

    def can_process(self, data):
        return (
            isinstance(data, list)
            and all(isinstance(x, dict) for x in data)
        )

    def process(self, data):
        self.buffer.extend(data)
        self.total_processed += len(data)

    def output(self, n: int):
        taken = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return taken


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    ds = DataStream()
    print()
    print("Initialize Data Stream...")
    ds.print_processors_stats()

    print("\nRegistering Numeric Processor")
    ds.register_processor(NumericProcessor())

    stream = [
        "Hello world",
        [3.14, -1, 2.71],
        [{"log_level": "WARNING", "log_message":
            "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message":
                "User wil is connected"}],
        42,
        ["Hi", "five"]
    ]
    print("\nSend first batch of data on stream:")
    ds.process_stream(stream)
    ds.print_processors_stats()
    print("\nRegistering other processors")
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())
    print("Send the same batch again")
    ds.process_stream(stream)
    ds.print_processors_stats()
    print(
            "\nConsume some elements from the data processors: "
            "Numeric 3, Text 2, Log 1"
        )
    num_proc = ds.processors[0]
    text_proc = ds.processors[1]
    log_proc = ds.processors[2]
    num_proc.output(3)
    text_proc.output(2)
    log_proc.output(1)
    ds.print_processors_stats()

# Create stream
# No processors → errors
# Add numeric processor → partial success
# Add others → full success
# Consume some data → stats update
