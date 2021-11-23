class ScoreColumn:
    def __init__(self, player_name: str):
        self.name = player_name
        # upper
        self.upper = [None, None, None, None, None, None] # [ones, twos, threes, ...]
        self.upper_sum = 0
        self.bonus = 0
        # lower
        self.one_pair = None
        self.two_pairs = None
        self.three_of_a_kind = None
        self.four_of_a_kind = None
        self.small_straight = None
        self.large_straight = None
        self.full_house = None
        self.chance = None
        self.yatzy = None

    def __str__(self):
        s = "\n" + self.name + "\'s scoreboard: \n"
        for i in range(6):
            s += "[" + str(i+1) + "]s : " + str(self.upper[i]) + "\n"
        s += "Sum: " + str(self.upper_sum) + "\n"
        s += "Bonus (Sum >= 63 required): " + str(self.check_bonus())  + "\n"
        s += "[7] One Pair: " + str(self.one_pair) + "\n"
        s += "[8] Two Pairs: " + str(self.two_pairs) + "\n"
        s += "[9] Three of a Kind: " + str(self.three_of_a_kind) + "\n"
        s += "[10] Four of a Kind: " + str(self.four_of_a_kind) + "\n"
        s += "[11] Small Straight: " + str(self.small_straight) + "\n"
        s += "[12] Large Straight: " + str(self.large_straight) + "\n"
        s += "[13] Full House: " + str(self.full_house) + "\n"
        s += "[14] Chance: " + str(self.chance) + "\n"
        s += "[15] Yatzy: " + str(self.yatzy) + "\n"
        s += "Total: " + str(self.get_total()) + "\n"
        return s

    def check_upper(self, number: int, dice: list, write = False):
        if self.upper[number-1] != None:
            return None
        score = 0
        for d in dice:
            if d == number:
                score += number
        if write:
            self.upper[number-1] = score
            self.upper_sum += score
        return score

    def check_bonus(self):
        if self.bonus == 50:
            return 5
        if self.upper_sum >= 63:
            self.bonus = 50
            return 50
        return 0

    def check_one_pair(self, dice: list, write = False):
        if self.one_pair != None:
            return None
        count = [0,0,0,0,0,0] # counts how many of each dice
        for d in dice:
            count[d-1] += 1
        largest = 0
        largest_index = 0
        for i, c in enumerate(count):
            if c >= 2:
                largest = c
                largest_index = i
        if largest < 2:
            result = 0
        else:
            result = 2*(largest_index+1)
        if write: 
            self.one_pair = result
        return result

    def check_two_pairs(self, dice: list, write = False):
        if self.two_pairs != None:
            return None
        count = [0,0,0,0,0,0] # counts how many of each dice
        for d in dice:
            count[d-1] += 1
        largest1 = 0
        largest2 = 0
        largest_index1 = 0
        largest_index2 = 0
        for i, c in enumerate(count):
            if c >= 2:
                if largest_index1 < largest_index2:
                    largest1 = c
                    largest_index1 = i
                else:
                    largest2 = c
                    largest_index2 = i
        if largest1 < 2 or largest2 < 2:
            result = 0
        else:
            result = 2*(largest_index1+1) + 2*(largest_index2+1)
        if write:
            self.two_pairs = result
        return result

    def check_three_of_a_kind(self, dice: list, write = False):
        if self.three_of_a_kind != None:
            return None
        count = [0,0,0,0,0,0] # counts how many of each dice
        for d in dice:
            count[d-1] += 1
        largest = 0
        largest_index = 0
        for i, c in enumerate(count):
            if c >= 3:
                largest = c
                largest_index = i
        if largest < 3:
            result = 0
        else:
            result = 3*(largest_index+1)
        if write: 
            self.three_of_a_kind = result
        return result

    def check_four_of_a_kind(self, dice: list, write = False):
        if self.four_of_a_kind != None:
            return None
        count = [0,0,0,0,0,0] # counts how many of each dice
        for d in dice:
            count[d-1] += 1
        largest = 0
        largest_index = 0
        for i, c in enumerate(count):
            if c >= 4:
                largest = c
                largest_index = i
        if largest < 4:
            result = 0
        else:
            result = 4*(largest_index+1)
        if write: 
            self.four_of_a_kind = result
        return result

    def check_small_straight(self, dice: list, write = False):
        if self.small_straight != None:
            return None
        if sorted(dice) == [1,2,3,4,5]:
            result = 15
        else:
            result = 0
        if write:
            self.small_straight = result
        return result

    def check_large_straight(self, dice: list, write = False):
        if self.large_straight != None:
            return None
        if sorted(dice) == [2,3,4,5,6]:
            result = 20
        else:
            result = 0
        if write:
            self.small_straight = result
        return result

    def check_full_house(self, dice: list, write = False):
        if self.full_house != None:
            return None
        count = [0,0,0,0,0,0] # counts how many of each dice
        for d in dice:
            count[d-1] += 1
        has_triple = False
        triple_index = 0
        has_double = False
        double_index = 0
        for i, c in enumerate(count):
            if c == 3:
                has_triple = True
                triple_index = i
        for i, c in enumerate(count):
            if c == 2:
                has_double = True
                double_index = i
        if has_triple and has_double:
            result = 3*(triple_index+1) + 2*(double_index+1)
        else:
            result = 0
        if write:
            self.full_house = result
        return result
        
    def check_chance(self, dice: list, write = False):
        if self.chance != None:
            return None
        if write:
            self.chance = sum(dice)
        return sum(dice)

    def check_yatzy(self, dice: list, write = False):
        if self.yatzy != None:
            return None
        yatzy = True
        for i in range(1,5):
            if dice[i] != dice[i-1]:
                yatzy = False
                break
        if yatzy:
            result = 50
        else:
            result = 0
        if write:
            self.yatzy = result
        return result
        
    def get_total(self):
        total = self.upper_sum
        total += self.check_bonus()
        for score in (self.one_pair, self.two_pairs, self.three_of_a_kind,
                        self.four_of_a_kind, self.small_straight,
                        self.large_straight, self.full_house,
                        self.chance, self.yatzy):
            if score == None:
                total += 0
            else:
                total += score
        return total
    
    def is_full(self):
        for score in self.upper:
            if score == None:
                return False
        for score in (self.one_pair, self.two_pairs, self.three_of_a_kind,
                        self.four_of_a_kind, self.small_straight,
                        self.large_straight, self.full_house,
                        self.chance, self.yatzy):
            if score == None:
                return False
        return True