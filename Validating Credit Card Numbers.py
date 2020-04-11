# You and Fredrick are good friends. Yesterday, Fredrick received
#
# credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!
#
# A valid credit card from ABCD Bank has the following characteristics:
#
# ► It must start with a
# , or .
# ► It must contain exactly digits.
# ► It must only consist of digits (-).
# ► It may have digits in groups of , separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have or more consecutive repeated digits.
import re
credit_card=[]
n = int(input())
for i in range(n):
    credit_card.append(input())

for i in credit_card:
    if len(i) == 16:
        if i[0] == [4,5,6]:
            x = re.split('-')
            for j in x:
                if len(j) == 4:
                    if j.isdigit():
                        if re.match('/(\d)\1{4,}/',''.join(x)):
                            print()





