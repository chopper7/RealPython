# Real Python Part 1
# Chapter 8 Assignment: "cats_with_hats"


# Initially all cats, numbered 1 through 100, do not have a hat
cat_hats = {k: False for k in range(1, 101)}

# If a cat has an n-th key (every 3rd, every 5th, every 31st, etc),
# change its hat status: if has hat take it off; if no hat put it on
for n in range(1, 101):
    for cat in cat_hats.keys():
        if cat % n == 0:
            cat_hats[cat] = not (cat_hats[cat])

# Output which cats have hats at the end
for cat,hat in cat_hats.items():
    if hat:
        print('Cat # {} has a hat!'.format(cat))