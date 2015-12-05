'''
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?

Your puzzle answer was 236.

--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?

Your puzzle answer was 51.
'''


import re

NAUGHTY_STRINGS_old = ['ab', 'cd', 'pq', 'xy']

NICE_DOUBLE_old = re.compile(r'.*(.)\1.*')
NICE_VOWELS_old = re.compile(r'(.*[a,e,i,o,u]){3}')

NICE_DOUBLE = re.compile(r'(?P<group_one>[a-z]{2})[a-z]*(?P=group_one)')
NICE_VOWELS = re.compile(r'(?P<group_one>[a-z])[a-z](?P=group_one)')


def naughty_o_meter_old(citizen):
    if not any(x in citizen for x in NAUGHTY_STRINGS_old):
        if NICE_VOWELS_old.match(citizen) and NICE_DOUBLE_old.match(citizen):
            return "Nice"
        else:
            return "Naughty"
    else:
        return "Naughty"

def naughty_o_meter(citizen):
    if NICE_DOUBLE.search(citizen) and NICE_VOWELS.search(citizen):
        return "Nice"
    else:
        return "Naughty"

good_strings_old = 0
good_strings = 0

f = open('day5_strings.csv', 'r')
for line in f:
    if naughty_o_meter_old(line) == "Nice":
        good_strings_old += 1
    if naughty_o_meter(line) == "Nice":
        good_strings += 1


print("Old List: " + str(good_strings_old) + " New List: " + str(good_strings))
