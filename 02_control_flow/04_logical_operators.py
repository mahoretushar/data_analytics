passing_year_2022 = True
has_high_score = False
arts_student = True

# and operator
# if passing_year_2022 and has_high_score:
#     print("Eligible for Interview")
# else:
#     print("Not Eligible for Interview")

# not operator
# if not arts_student:
#     print("Eligible")
# else:
#     print("Not Eligible")


# haskell
# complex conditions
if (passing_year_2022 or has_high_score) and not arts_student:
    #       True                False              True
    #               True                           False
    #                                  False
    print("Eligible")
else:
    print("Not Eligible")