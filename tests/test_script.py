import re


def ip_viewer():
    with open("test_file.log") as file:
        file = file.read()
        gotem = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", file)
    return gotem


def pid_viewer():
    with open("test_file.log") as file:
        file = file.read()
        pids = re.findall("\d{4}", file)
    return pids


def ip_replacer(o, n):
    with open("test.log") as file:
        file = file.read()
    rep = file.replace(o, n)
    with open("test.log", "w") as file:
        file.write(rep)


def pid_replacer(o, n):
    with open("test.log") as file:
        file = file.read()
    rep = file.replace(o, n)
    with open("test.log", "w") as file:
        file.write(rep)
