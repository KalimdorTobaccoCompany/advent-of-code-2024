#!/usr/bin/python3

"""
--- Part Two ---

The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

    7 6 4 2 1: Safe without removing any level.
    1 2 7 8 9: Unsafe regardless of which level is removed.
    9 7 6 2 1: Unsafe regardless of which level is removed.
    1 3 2 4 5: Safe by removing the second level, 3.
    8 6 4 4 1: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.

Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
"""

if __name__ == "__main__":
    number_of_safe_reports = 0
    with open("problem_2_2.in", 'r') as in_file:
        for line in in_file:
            numbers = line.split()
            diff_trouble = 0
            asc_trouble = 0
            desc_trouble = 0
            broken = False
            for i in range(0, len(numbers) - 1):
                N1 = int(numbers[i])
                N2 = int(numbers[i+1])
                N3 = None
                if (i + 2) < len(numbers):
                    N3 = int(numbers[i+2])
                diff = abs(N2 - N1)
                # Check if the diff is too big. If it is, will the removal of number help?
                if diff < 1 or diff > 3:
                    if N3 is None:
                        # No more members left. Simply discard the following number
                        diff_trouble += 1
                    else:
                        new_diff = abs(N3 - N1)
                        if new_diff >= 1 and new_diff <= 3:
                            diff_trouble += 1
                        else:
                            diff_trouble += 21
                else:
                    if N1 <= N2:
                        if N3 is None:
                            desc_trouble += 1
                        else:
                            if N1 > N3:
                                desc_trouble += 1
                            else:
                                desc_trouble += 2
                    elif N1 >= N2:
                        if N3 is None:
                            asc_trouble += 1
                        else:
                            if N1 < N3:
                                asc_trouble += 1
                            else:
                                asc_trouble += 2
            if diff_trouble < 2 and (desc_trouble < 2 or asc_trouble < 2):
                print(numbers)
                print("Diff trouble: ", diff_trouble)
                print("Asc trouble: ", asc_trouble)
                print("Desc trouble: ", desc_trouble)
                print("+1")
                number_of_safe_reports += 1
            else:
                print(numbers)
                print("Diff trouble: ", diff_trouble)
                print("Asc trouble: ", asc_trouble)
                print("Desc trouble: ", desc_trouble)
                print("0")
            print("######\n")
    print(number_of_safe_reports)