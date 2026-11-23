from operation import Operation


class Calculator:
    """A calculator that manages and executes registered operations.

    Operations are registered using a unique name and can be executed
    dynamically by calling calculate() with the corresponding name.
    """

    def __init__(self):
        """Initialize the calculator with an empty operation registry.

        The registry stores operation names as keys and Operation
        instances as values.
        """
        self._operations:dict[str, Operation] = {}

    def register(
            self,
            name: str,
            operation: Operation) -> None:
        """Register a mathematical operation with the calculator.

        Registers the operation only if the provided name is not
        already present in the operation registry.

        Args:
            name (str): Unique name used to identify the operation.
            operation (Operation): Operation instance to register.

        Returns:
            None
        """
        if name not in self._operations:
            self._operations[name] = operation

    def calculate(self, name:str, **kwargs) -> float:
        """Execute a registered operation by its name.

        Retrieves the operation from the registry and invokes its
        calculate() method with the provided keyword arguments.

        Args:
            name (str): Name of the registered operation to execute.
            **kwargs: Arguments required by the selected operation.

        Returns:
            float: Result returned by the selected operation.

        Raises:
            KeyError: If the requested operation name is not registered.

        Example:
            >>> calculator.calculate("addition", a=10, b=5)
            15
        """
        # todo: If name is not registered throw error
        return self._operations[name].calculate(**kwargs)

    def list_operations(self) -> list[str]:
        """Return the names of all registered operations.

        Returns:
            list[str]: List containing registered operation names.

        Example:
            >>> calculator.list_operations()
            ['addition', 'subtraction', 'multiplication']
        """
        return list(self._operations)
