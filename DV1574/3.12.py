def show_wordlist(w_list):
    for a in w_list.keys():
        print(a, ": ", w_list[a])


numbers = {'one': 1, 'two': 2, 'seven': 6, 'eight': 9}
show_wordlist(numbers)