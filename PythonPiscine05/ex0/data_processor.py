

from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data = []  # Data guarda ingested values (FIFO queue) 
        self._counter = 0 # Keeps track of output order
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass  # Debe acceptar any y retornar True or False
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass  #Child classes will override this con tipos mas específicos
    def output(self) -> tuple[int, str]:
        if not self._data:
            raise ValueError("No data available")
        value = self._data.pop(0)  # Take the oldest value
        index = self._counter
        self._counter += 1
        return index, value # Retorna index y value y lo borra del storage

# Convierte numbers en strings, store data (maneja nun simples y lista de nums)
class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False
    def ingest(self, data) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data") # Todo: process y store
        if isinstance(data, list):
            for x in data:
                self._data.append(str(x))
        else:
            self._data.append(str(data))

# Acepta str y listas[str]. No se necesita conversor en esta
class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False
    def ingest(self, data) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            self._data.extend(data)
        else:
            self._data.append(data)

# Acepta dict[(KEY)str, (VALUE)str] o listas de dicts
class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_valid_dict(d):
            return (
                isinstance (d, dict)
                and all(isinstance(k, str) and isinstance(v, str) for k, v in d.items())
            )
        if is_valid_dict(data):
            return True
        if isinstance(data, list):
            return all(is_valid_dict(d) for d in data)
        return False
    def ingest(self, data) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        def format_log(d):
            return f"{d['log_level']}: {d['log_message']}"
        if isinstance(data, list):
            for d in data:
                self._data.append(format_log(d))
        else:
            self._data.append(format_log(data))


if __name__ == '__main__':
    print("=== Code Nexus - Data Processor ===")
    print()
    print("Testing Numeric Processor...")
    num = NumericProcessor()
    print("Trying to validate input '42':", num.validate(42))  # True
    print("Trying to validate input 'Hello':", num.validate("Hello")) # False
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num.ingest("foo")
    except Exception as e:
        print("Got exception:", e)
    print("Processing data:", [1, 2, 3, 4, 5])
    num.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for _ in range(3):
        try:
            i, v = num.output()
            print(f"Numeric value {i}: {v}")
        except Exception as e:
            print("Error:", e)
    print()
    print("Testing Text Processor...")
    text = TextProcessor()
    print("Trying to validate input '42':", text.validate(42))  # True
    print("Procesing data:", ['Hello', 'Nexus', 'World'])
    text.ingest(['Hello', 'Nexus', 'World'])
    print("Extracting 1 value...")
    i, v = text.output()
    print(f"Text value {i}: {v}")
    print()
    print("Testing Log Processor...")
    log = LogProcessor()
    print("Trying to validate input 'Hello':", log.validate("Hello"))
    logs = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print("Processing data:", logs)
    log.ingest(logs)
    print("Extracting 2 values...")
    for _ in range(2):
        i, v = log.output()
        print(f"Log entry {i}: {v}")

