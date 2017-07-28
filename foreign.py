import sys

if sys.version_info < (3,0):
    from Tkinter import *
    from Tkinter import ttk
else:
    from tkinter import *
    from tkinter import ttk

from yahoo_finance import Currency

def calculate(*args):
    try:
        value = float(currencyToConvert.get())
        currencyCreate = Currency(choices[var.get()] + choices[var1.get()])
        currencyCreate.refresh()
        currencyValue = currencyCreate.get_rate()
        convertedCurrency.set("{:.2f}".format(value * float(currencyValue)))
        age = choices[var.get()]
    except ValueError:
        pass



root = Tk()
root.title("Foreign Exchange")
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=0)
mainframe.rowconfigure(0, weight=0)
mainframe.pack()


currencyToConvert = StringVar()
convertedCurrency = StringVar()
convertEntry = ttk.Entry(mainframe, width=15, textvariable=currencyToConvert)
convertEntry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=convertedCurrency).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)


choices = {
    'US Dollar': 'USD',
    'Euro': 'EUR',
    'Japanese Yen': 'JPY',
    'British Pound': 'GBP',
    'Australian Dollar ': 'AUD',
    'New Zealand Dollar': 'NZD',
    'Canadian Dollar': 'CAD',
    'Swedish Krona': 'SEK',
    'Swiss Franc': 'CHF',
    'Hungarian Forint': 'HUF',
    'Chinese Yuan': 'CNY',
    'Hong Kong Dollar': 'HKD',
    'Singapore Dollar': 'SGD',
    'Indian Rupee': 'INR',
    'Mexican Peso': 'MXN',
    'Philippine Peso': 'PHP',
    'Indonesian Rupiah': 'IDR',
    'Thai Baht': 'THB',
    'Malaysian Ringgit': 'MYR',
    'South African Rand': 'ZAR',
    'Russian Ruble': 'RUB',
}


var = StringVar(root)
option = OptionMenu(mainframe, var, *choices)
# var.set('USD')
option.grid(column=3, row=1, sticky = (W,E))

var1 = StringVar(root)
option = OptionMenu(mainframe, var1, *choices)
# var1.set('USD')
option.grid(column=3, row=2, sticky = (W,E))

option.configure(width=20)

Label(mainframe, text="$").grid(row=1)
Label(mainframe, text="$").grid(row=2)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
convertEntry.focus()
root.bind('<Return>', calculate)

root.mainloop()
