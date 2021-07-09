#!/usr/bin/env python3
# Standard Library
import sys
from subprocess import run


def _inspect_tasks(prefix):
    return {
        k.replace(prefix, ""): v
        for k, v in globals().items()
        if k.startswith(prefix)
    }


def _cmd(command, args=[]):
    return run(command.split(" ") + args)


def _pycmd(command, args=[]):
    py3 = ".venv/bin/python3"
    return run([py3, "-m"] + command.split(" ") + args)


def _exit_handler(status):
    statuses = status if type(status) == list else [status]
    bad_statuses = [s for s in statuses if s.returncode != 0]
    if bad_statuses:
        sys.exit(bad_statuses)


def task_init(args):
    results = []
    results.append(_cmd("python3 -m venv .venv"))
    results.append(_pycmd(f"pip install --upgrade pip setuptools wheel"))
    results.append(_pycmd(f"pip list -v --no-index"))
    return results


def task_test(args):
    return _pycmd(f"pytest")

def task_cra(args):
    return _cmd("npx create-react-app --template typescript --use-npm frontend", args)

def task_sam(args):
    return _cmd("sam init --runtime python3.8 --dependency-manager pip --output-dir backend --name api", args)

if __name__ == "__main__":
    tasks = _inspect_tasks("task_")

    if len(sys.argv) >= 2 and sys.argv[1] in tasks.keys():
        _exit_handler(tasks[sys.argv[1]](sys.argv[2:]))
    else:
        print(f"Must provide a task from the following: {list(tasks.keys())}")
