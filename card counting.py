import tkinter as tk

def count_cards(cards):
    count = 0
    for card in cards:
        if card in [2, 3, 7]:
            count += 1
        elif card in [4, 5, 6]:
            count += 2
        elif card == 9:
            count -= 1
        elif card in [10, 'J', 'Q', 'K']:
            count -= 2
    return count

def update_count(*args):
    count = count_cards([int(card.get()) for card in player_card_entries + dealer_card_entries if card.get().isdigit()])
    count_var.set(count)
    running_count_var.set(running_count_var.get() + count)

def clear_inputs(*args):
    for entry in player_card_entries + dealer_card_entries:
        entry.delete(0, tk.END)
    count_var.set(0)

root = tk.Tk()
root.title("Blackjack Card Counter")

player_label = tk.Label(root, text="My Hand:")
player_label.grid(row=0, column=0, columnspan=6, sticky="W", pady=10)

player_card_entries = []
for i in range(6):
    entry = tk.Entry(root)
    entry.grid(row=1, column=i)
    player_card_entries.append(entry)

dealer_label = tk.Label(root, text="Dealer Hand:")
dealer_label.grid(row=2, column=0, columnspan=6, sticky="W", pady=10)

dealer_card_entries = []
for i in range(6):
    entry = tk.Entry(root)
    entry.grid(row=3, column=i)
    dealer_card_entries.append(entry)

update_button = tk.Button(root, text="Update", command=update_count)
update_button.grid(row=4, column=0, columnspan=6, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_inputs)
clear_button.grid(row=5, column=0, columnspan=6, pady=10)

count_var = tk.StringVar()
count_label = tk.Label(root, textvariable=count_var)
count_label.grid(row=6, column=0, columnspan=6, pady=10)

running_count_var = tk.IntVar(value=0)
running_count_label = tk.Label(root, textvariable=running_count_var)
running_count_label.grid(row=7, column=0, columnspan=6, pady=10)

root.mainloop()

