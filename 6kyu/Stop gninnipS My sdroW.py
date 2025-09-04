def spin_words(sentence):
    split_sentence = sentence.split()
    if len(split_sentence) <= 1 :
        for i in split_sentence:
            lists = list(i)
            if len(lists) < 5:
                return i 
            else:
                lists.reverse()             
                res = "".join(lists)
                return res
    elif len(split_sentence) > 1 :
        result = []
        for i in split_sentence:
            if len(i) < 5 :
                result.append(i)
            elif len(i) >= 5:
                lists = list(i)
                lists.reverse()
                result.append("".join(lists))
        total = " ".join(result)
        return total
    

"Hey fellow warriors" 
['Hey', 'fellow', ]

['h', 'e', 'y']