def calculate_points(category, dice):
    number = { "Einser": 1, "Zweier": 2, "Dreier": 3, "Vierer": 4, "Fünfer": 5, "Sechser": 6 }

    if category in number:
        number = numbers[category]
        points = dice.count(number) * number
        print(points)
        return 
        #dice.count(zahl) * zahl

    elif category == "Ein Paar":
        points = 0
        for number in range(1, 7):
            if dice.count(number) >= 2:
                points = number * 2
                print(points)
        return points
    
    elif category == "Zwei Paare":
        pairs = []
        for number in range(1, 7):
            if dice.count(number) >= 2:
                pairs.append(number)
        if len(pairs) == 2:
            return sum(pairs) * 2
        
        return 0
    
    elif category == "Drilling":
        for number in range(1, 7):
            if dice.count(number) >= 3:
                return number * 3
            
        return 0

    elif category == "Vierling":
        for number in range(1, 7):
            if dice.count(number) >= 4:
                return number * 4
        return 0

    elif category == "Kleine Strasse":
        if sorted(dice) == [1, 2, 3, 4] or  [2, 3, 4, 5] or [3, 4, 5, 6]:
            return 15
        return 0

    elif category == "Grosse Strasse":
        if sorted(dice) == [1, 2, 3, 4, 5,] or [2, 3, 4, 5, 6]:
            return 20
        return 0

    elif category == "Full House":
        pair = False
        triple = False

        for number in range(1, 7):
            if dice.count(number) == 2:
                pair = True

            if dice.count(number) == 3:
                triple = True

        if pair and triple:
            return sum(dice)

        return 0

    elif category == "Chance":
        return sum(dice)

    elif category == "Yatzy":
        if dice.count(dice[0]) == 5:
            return 50

        return 0

    return 0
