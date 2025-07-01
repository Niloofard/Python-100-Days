def calculate_love_score(name1,name2):
    count_1=0
    count_2=0
    for letter in name1:
        if letter in "TRUE":
            count_1+=1
    for letter in name2:
        if letter in "TRUE":
            count_1+=1
    for letter in name1:
        if letter in "LOVE":
            count_2+=1
    for letter in name2:
        if letter in "LOVE":
            count_2+=1
    Final = count_1 *10 + count_2
    print(Final)

name1 = input("enter your name:").upper()
name2 = input("enter your loved name:").upper()
calculate_love_score(name1,name2)