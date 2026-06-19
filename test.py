"""Simple greeting module."""


def hello(name: str = "World") -> str:
    """
    Generate a greeting message.

    Args:
        name: Name of the person to greet.

    Returns:
        A formatted greeting string.
    """
    return f"Hello, {name}!"


def main() -> None:
    """
    Run the application.
    """
    message = hello()
    print(message)


if __name__ == "__main__":
    main()
