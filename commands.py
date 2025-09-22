# commands.py
import os
import shutil
from pathlib import Path
from utils import safe_print


def cmd_pwd(args):
    safe_print(os.getcwd())

def cmd_ls(args):
    path = args[0] if args else "."
    try:
        for entry in sorted(os.listdir(path)):
            safe_print(entry)
    except Exception as e:
        safe_print(f"ls: {e}")

def cmd_cd(args):
    path = args[0] if args else os.path.expanduser("~")
    try:
        os.chdir(path)
    except Exception as e:
        safe_print(f"cd: {e}")

def cmd_mkdir(args):
    if not args:
        safe_print("mkdir: missing operand")
        return
    for path in args:
        try:
            os.makedirs(path, exist_ok=True)
        except Exception as e:
            safe_print(f"mkdir: {e}")

def cmd_rm(args):
    if not args:
        safe_print("rm: missing operand")
        return
    recursive = False
    if args[0] == "-r":
        recursive, args = True, args[1:]
    for path in args:
        try:
            if os.path.isdir(path) and not os.path.islink(path):
                if recursive:
                    shutil.rmtree(path)
                else:
                    safe_print(f"rm: cannot remove '{path}': Is a directory")
            else:
                os.remove(path)
        except Exception as e:
            safe_print(f"rm: {e}")

def cmd_echo(args):
    safe_print(" ".join(args))

def cmd_help(args):
    safe_print("Available commands: " + ", ".join(COMMANDS.keys()))

COMMANDS = {
    "pwd": cmd_pwd,
    "ls": cmd_ls,
    "cd": cmd_cd,
    "mkdir": cmd_mkdir,
    "rm": cmd_rm,
    "echo": cmd_echo,
    "help": cmd_help,
}
