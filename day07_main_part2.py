from collections import defaultdict

f = open("day07_input.txt", "r")
order_cards = ['A','K','Q','T','9','8','7','6','5','4','3','2','J'][::-1]

dict_hands = defaultdict(list)
dict_bids = defaultdict(int)
for i,line in enumerate(f):
    line = line.strip().split(" ")
    dict_hands[i] = line[0]
    dict_bids[i] = int(line[1])


order_hand_strength = [[1,1,1,1,1],[2,1,1,1],[2,2,1],[3,1,1],[3,2],[4,1],[5]]
order_hand_strength_final = []
for ord in dict_hands:
    dict_cnt = defaultdict(int)
    all_js = False
    for c in dict_hands[ord]:
        dict_cnt[c] += 1
    ls = list(dict_cnt.values())

    if "J" in dict_cnt and dict_hands[ord] != "JJJJJ":
        ls_max = max([dict_cnt[cc] for cc in dict_cnt if cc != "J"])
        for c in dict_cnt:
            if dict_cnt[c] == ls_max and c != "J":
                dict_cnt[c] += dict_cnt["J"]
                dict_cnt["J"] -= dict_cnt["J"]

    ls = [cc for cc in dict_cnt.values() if cc != 0]
    ls.sort(reverse=True)
    order_hand_strength_final.append((ord,order_hand_strength.index(ls)))


dict_hand_strength = defaultdict(int)
for ord,hand_strength in order_hand_strength_final:
    dict_hand_strength[hand_strength] += 1


def rec(a,b):
    a0 = a[0]
    b0 = b[0]
    a1 = a[1]
    b1 = b[1]
    try:
        for i in range(len(a)):
            oa = order_cards.index(a1[i])
            ob = order_cards.index(b1[i])
            if oa > ob:
                return a0,b0
            elif ob > oa:
                return b0,a0
            else:
                return rec((a0,a1[1:]),(b0,b1[1:]))
    except:
        print(a,b)



order_final = []
hand_strength_ = [x for x in dict_hand_strength]
hand_strength_.sort(reverse=True)
for hs in hand_strength_:
    if dict_hand_strength[hs] == 1:  #number of hands with hs
        for ord,hs1 in order_hand_strength_final:
            if hs1 == hs:
                order_final.append((ord,dict_hands[ord]))
                break
    else:
        hands_to_sort = []
        for ord,hs1 in order_hand_strength_final:
            if hs1 == hs:
                hands_to_sort.append((ord,dict_hands[ord]))
        reordered = 1
        while reordered:
            reordered = 0
            for i in range(len(hands_to_sort)):
                if i+1 <= len(hands_to_sort)-1:
                    ordered = rec(hands_to_sort[i],hands_to_sort[i+1])
                    if (hands_to_sort[i][0],hands_to_sort[i+1][0]) != ordered:
                        reordered += 1
                        placeholder = hands_to_sort[i]
                        hands_to_sort[i] = hands_to_sort[i+1]
                        hands_to_sort[i+1] = placeholder
        order_final += hands_to_sort

print(order_final)
ii = len(order_final)
final_sum = []
for i,x in enumerate(order_final):
    ord,hand = x
    ord2 = ii-i
    final_sum.append(dict_bids[ord]*ord2)
print(sum(final_sum))

