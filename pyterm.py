import os
import sys
from commands import COMMANDS
from utils import safe_print
from nl_translator import nl_to_command


def parse_and_execute(line, history):
    # Handle natural language commands
    if line.startswith("nl:"):
        nl_query = line[3:].strip()
        translated = nl_to_command(nl_query)

        if translated.startswith("[nl] error:"):
            safe_print(translated)
            return

        safe_print(f"[nl->] {translated}")
        line = translated  # replace NL query with actual command

    # Split command and args
    parts = line.split()
    if not parts:
        return

    cmd, *args = parts

    # Exit handling
    if cmd == "exit":
        raise SystemExit

    if cmd == "help":
        safe_print("Available commands:")
        for c in COMMANDS.keys():
            safe_print(f" - {c}")
        safe_print("Prefix with 'nl:' for natural language translation.")
        return

    # Special handling for history
    if cmd == "history":
        if "history" in COMMANDS:
            COMMANDS["history"](args, history)
        return

    # Run built-in command
    if cmd in COMMANDS:
        try:
            COMMANDS[cmd](args)
        except Exception as e:
            safe_print(f"Error executing {cmd}: {e}")
    else:
        # Otherwise, fallback to OS command
        os.system(line)


def main():
    safe_print("Welcome to PyTerm! Type 'help' for commands, 'exit' to quit.")
    history = []

    while True:
        try:
            line = input("PyTerm> ").strip()
        except (EOFError, KeyboardInterrupt):
            safe_print("\nExiting PyTerm.")
            break

        if not line:
            continue

        if line == "exit":
            safe_print("Exiting PyTerm.")
            break

        history.append(line)
        try:
            parse_and_execute(line, history)
        except SystemExit:
            break


if __name__ == "__main__":
    main()
