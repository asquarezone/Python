from abc import ABC, abstractmethod
import json
import os

class CacluatorStore:
    @abstractmethod
    def load(self):
        pass


    @abstractmethod
    def append(self, operation:str, args: dict):
        pass


class InMemoryStore(CacluatorStore):
    def __init__(self):
        self.store = []

    def load(self):
        return self.store

    def append(self, operation: str, args:dict, result: float):
        self.store.append(
            {
            "operation": operation,
            "input": args,
            "output": result
            }
        )

    def __str__(self):
        text = ""
        for item in self.store:
            text += f"{item}"
        return text

    def __repr__(self):
        text = ""
        for item in self.store:
            text += f"{item}" 
        return text




class JsonMemoryStore(CacluatorStore):
    def __init__(self, file_path: str = "history.json"):
        self.file_path = file_path
        self.store = []
        self._load_from_file()

    def _load_from_file(self):
        """Load history from the JSON file if it exists."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    self.store = json.load(f)
            except (json.JSONDecodeError, OSError):
                # Start with an empty history if the file is invalid
                self.store = []
        else:
            self.store = []

    def _save_to_file(self):
        """Persist the current history to disk."""
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.store, f, indent=4)

    def load(self):
        """Return the calculation history."""
        return self.store

    def append(self, operation: str, args: dict, result: float):
        """Append a new calculation and persist it."""
        self.store.append(
            {
                "operation": operation,
                "input": args,
                "output": result,
            }
        )
        self._save_to_file()

    def clear(self):
        """Clear the history."""
        self.store = []
        self._save_to_file()

    def __str__(self):
        return json.dumps(self.store, indent=4)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(file_path='{self.file_path}', entries={len(self.store)})"
        )