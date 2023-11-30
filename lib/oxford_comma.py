def oxford_comma(items):
    if len(items) == 1:
        return ''.join(items)
    elif len(items) == 2: 
        items.insert(-1, "and")
        sentence = ' '.join(items)
        return (sentence)
    else:
        last_item = items.pop()
        items = [item + ',' for item in items]
        items.append(last_item)
        items.insert(-1, "and")
        sentence = ' '.join(items)
        return (sentence)

        
#oxford_comma(['Kiwi', 'Panda', 'Goat'])
