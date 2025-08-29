def find_needle(haystack):
    for i in range(0, len(haystack)):
        if  haystack[i] == 'needle':
            res = "found the needle at position " + str(i)
            print (res)
            return res
        

find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"])