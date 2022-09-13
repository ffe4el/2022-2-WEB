import tkinter as tk
from tkinter import simpledialog
from rich import print

root = tk.Tk()
root.withdraw()


def gui_input(title, text):
    return (simpledialog.askstring(title=title, prompt=text))

def input_with_check(prompt):
    while True:
        value = gui_input("구구단", prompt)
        try:
            value = int(value)
            if 2 <= value <= 9:
                return value

        except ValueError as e:
            print(e)
            print("2-9까지 자연수를 입력하세요.")

def main():
    # dan = int(gui_input("구구단", "단을 입력하세요. => "))
    dan = input_with_check("단을 입력하세요. => ")

    for i in range(9):
        print("[bold magenta]{}[/bold magenta] * {} = [bold blue]{}[/bold blue]" .format(dan, i+1, dan*(i+1)))

    from rich.panel import Panel
    print(Panel.fit(f"구구단 [red]{dan}단!", border_style="red"))
    print(Panel.fit("\n".join(["{} * {} = {}". format(dan, i+1, dan*(i+1)) for i in range(1,10)]),border_style="blue"))

if __name__ == "__main__":
    main()