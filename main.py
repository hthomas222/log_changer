import re
import sys
from rich.console import Console
from rich.table import Table


def ip_viewer():
    with open(log_file) as file:
        file = file.read()
        gotem = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", file)
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
        pids = re.findall("\d{4}", file)
    return pids


def pid_replacer(o, n):
    with open(log_file) as file:
        file = file.read()
    rep = file.replace(o, n)
    with open(log_file, "w") as file:
        file.write(rep)


def options():
    console.print(
        "[cyan]--------------------------------OPTIONS--------------------------------[/cyan]"
    )
    print()
    console.print(
        "\t[green]1[/green] - [red]IP Viewer[/red] - [blue]Lists the IP addresses found in the log file.[/blue]"
    )
    console.print(
        "\t[green]2[/green] - [red]IP Changer[/red] - [blue]Changes the IP addresses in the log file.[/blue]"
    )
    console.print(
        "\t[green]3[/green] - [red]PID Viewer[/red] - [blue]Lists the PIDs found in the log file.[/blue]"
    )
    console.print(
        "\t[green]4[/green] - [red]PID Changer[/red] - [blue]Changes the PIDs in the log file.[/blue]"
    )
    console.print(
        "\t[green]5[/green] - [red]LISTS THE OPTIONS[/red] - [blue]This command will list all available options.[/blue]"
    )
    console.print(
        "\t[green]0[/green] - [red]EXITS PROGRAM[/red] - [blue]This command will exit the program.[/blue]"
    )
    print()


console = Console()
console.print(
    "[cyan]--------------------------------LOGGER--------------------------------[/cyan]"
)
print()
log_file = console.input("[cyan]Enter the log file: [/cyan]")
print()
user_input = ""
options()
while user_input != "0":
    user_input = console.input("[cyan]Enter a number to select the option: [/cyan]")
    print()
    table = Table(title="Docker Commands")
    table.add_column("NUM", style="green")
    table.add_column("TASK", style="red")
    table.add_column("Description", style="blue")

    table.add_row("0", "EXITS PROGRAM", "This command will exit the program.")
    table.add_row("1", "IP Viewer", "Lists the IP addresses found in the log file.")
    table.add_row("2", "IP Changer", "Changes the IP addresses in the log file.")
    table.add_row("3", "PID Viewer", "Lists the PIDs found in the log file.")
    table.add_row("4", "PID Changer", "Changes the PIDs in the log file.")
    table.add_row(
        "5", "LISTS THE OPTIONS", "This command will list all available options."
    )
    console = Console()
    console.print(table)
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
    elif user_input == "5":
        options()
    elif user_input == "0":
        console.print("\t[cyan]LOGGER SAYS GOODBYE![/cyan]")
        sys.exit()
    else:
        console.print("[cyan]Please enter one of the choices!!!![/cyan]")
        print()
