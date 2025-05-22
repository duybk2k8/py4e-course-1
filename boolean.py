#boolean la kieu du lieu chi nhan true/false
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        #co the dung break o day
    print(found, value)
print('After', found)