import re
import sys
from rich.console import Console

def ip_viewer():
    with open(log_file) as file:
        file = file.read()
    gotem = re.findall("\d{2,3}.\d{2,3}.\d{2,3}.\d{2,3}", file)
    return gotem

def ip_replacer(o, n):
    with open(log_file) as file:
        file = file.read()
    rep = file.replace(o, n)
    with open(log_file, "w") as file:
        file.write(rep)

def pid_viewer():
    with open(log_file) as file:
        file = file.read()
        pids = re.findall("\[\d{4}\]", file)
    return pids

def pid_replacer(o, n):
    with open(log_file) as file:
        file = file.read()
    rep = file.replace(o, n)
    with open(log_file, "w") as file:
        file.write(rep)

def options():
    options = {
        "0": "EXITS PROGRAM",
        "1": "IP Viewer: Lists the IP",
        "2": "IP Changer: Changes the IP",
        "3": "PID Viewer: Lists the PIDS",
        "4": "PID Changer: Changes the PID",
        "op": "LISTS THE OPTIONS"
    }
    for k,v in options.items():
        console.print(f"\t[red]{k}[/red] --> [green]{v}[/green]")
    print()

console = Console()
console.print("[cyan]---------------------LOGGER---------------------[/cyan]")
print()
log_file = console.input("[cyan]Enter the log file --> [/cyan]")
print()
user_input = ""
options()
while user_input != "0":
    user_input = console.input("[cyan]Enter a number to select the option: [/cyan]")
    print()
    if user_input == "1":
        temp = ip_viewer()
        temp = list(set(temp))
        console.print("\t [bold red]Unique IPS:[/bold red]")
        console.print("\t [bold red]----------[/bold red]")
        for i in temp:
            console.print(f"\t [green]{i}[/green]")
        print()
    elif user_input == "2":
        replace = console.input("[cyan]Enter a IP to replace: [/cyan]")
        new = console.input("[cyan]Enter new IP: [/cyan]")
        ip_replacer(replace, new)
        print()
    elif user_input == "3":
        temp = pid_viewer()
        new_temp = []
        for i in temp:
            i = i.strip("[]")
            new_temp.append(i)
        console.print("\t\t[bold red]Unique PIDS:[/bold red]")
        console.print("\t\t[bold red]----------[/bold red]")
        cols = 5
        max_w = 0
        for ele in new_temp:
            c_len = len(str(ele))
            if c_len > max_w:
                max_w = c_len
        for i, ele in enumerate(new_temp, 1):
            console.print(f"[green]   {str(ele):<{max_w}}[/green]", end="")
            if i % cols == 0:
                print()
        print()
        print()
    elif user_input == "4":
        replace = console.input("[cyan]Enter a PID to replace: [/cyan]")
        new = console.input("[cyan]Enter new PID: [/cyan]")
        print()
        pid_replacer(replace, new)  
    elif user_input == "op":
        options()
    elif user_input == "0":
        console.print("\t[cyan]LOGGER SAYS GOODBYE![/cyan]")
        sys.exit()
    else:
        console.print("[cyan]Please enter one of the choices!!!![/cyan]")
        print()
