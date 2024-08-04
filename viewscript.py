import webbrowser, time

url = input("Input your url: ")
duration = input("Enter duration: ")
amount = input("How many tabs are we opening?: ")

for i in range(int(amount)):
    webbrowser.open_new_tab(url)
    time.sleep(int(duration))
    print("done")
    print("made by @9ghoul")

    
