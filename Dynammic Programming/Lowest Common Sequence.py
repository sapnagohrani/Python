S1 = "longest"
S2 = "stone"
m = len(S1)
n = len(S2)

common_char_list = []
lcs_table = [[0 for x in range(n+1)] for x in range(m+1)]
common_string = ''


def lcs_algo(S1, S2, m, n):
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs_table[i][j] = 0
            elif S1[i - 1] == S2[j - 1]:
                lcs_table[i][j] = 1 + lcs_table[i - 1][j - 1]
                common_char_list.append(S1[i-1])
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])
    return lcs_table, common_char_list


lcs_table, common_char_list = lcs_algo(S1, S2, m, n)


def get_common_string(lcs_table, common_char_list):
    length_longest_string = lcs_table[m][n]
    common_char_list = common_char_list[0:length_longest_string]
    return common_string.join(common_char_list)


common_string = get_common_string(lcs_table, common_char_list)
print(common_string)