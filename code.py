def stringSimilarity(string):
    n = len(string)
    z = [0] * n
    zbox_left, zbox_right, z[0] = 0, 0, n
    for i in range(1, n):          
        if i < zbox_right:
            k = i - zbox_left
            if z[k] < zbox_right - i:
                z[i] = z[k]
                continue            
            zbox_left = i
        else:
            zbox_left = zbox_right = i
        while zbox_right < n and string[zbox_right - zbox_left] == string[zbox_right]: 
            zbox_right += 1 
        z[i] = zbox_right - zbox_left
    return sum(z)
  

'''
solution for two strings A and B, we define the similarity of the strings to be the length of the longest prefix common to both strings. For example,
the similarity of strings "abc" and "abd" is 2, while the similarity of strings "aaa" and "aaab" is 3.
Calculate the sum of similarities of a string S with each of its suffixes.
'''



