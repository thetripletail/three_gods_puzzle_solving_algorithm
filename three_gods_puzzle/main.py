from current_state import *

suggestions = [None, None, None]


first_answer = isYourAnswerWillBe_X_IfIAskYou_IsTheThirdGodTheGodOfRandom__to_the_first_god()


if first_answer == "X":
    second_answer = isYourAnswerWillBe_X_IfIAskYou_IsTheThirdGodTheGodOfRandom__to_the_second_god()
    if second_answer == "X":
        suggestions[2] = names_to_behavior["R"]
        third_answer = isYourAnswerWillBe_X_IfIAskYou_AreYouTheGodOfTruth__to_the_first_god()
        if third_answer == "X":
            suggestions[0], suggestions[1] = names_to_behavior["T"], names_to_behavior["F"]
        else:
            suggestions[1], suggestions[0] = names_to_behavior["T"], names_to_behavior["F"]
    else:
        suggestions[0] = names_to_behavior["R"]
        third_answer = isYourAnswerWillBe_X_IfIAskYou_AreYouTheGodOfTruth__to_the_second_god()
        if third_answer == "X":
            suggestions[1], suggestions[2] = names_to_behavior["T"], names_to_behavior["F"]
        else:
            suggestions[2], suggestions[1] = names_to_behavior["T"], names_to_behavior["F"]
else:
    second_answer = isYourAnswerWillBe_X_IfIAskYou_IsTheFirstGoodTheGodOfRandom__to_the_third_god()
    if second_answer == "X":
        suggestions[0] = names_to_behavior["R"]
        third_answer = isYourAnswerWillBe_X_IfIAskYou_AreYouTheGodOfTruth__to_the_second_god()
        if third_answer == "X":
            suggestions[1], suggestions[2] = names_to_behavior["T"], names_to_behavior["F"]
        else:
            suggestions[2], suggestions[1] = names_to_behavior["T"], names_to_behavior["F"]
    else:
        suggestions[1] = names_to_behavior["R"]
        third_answer = isYourAnswerWillBe_X_IfIAskYou_AreYouTheGodOfTruth__to_the_first_god()
        if third_answer == "X":
            suggestions[0], suggestions[2] = names_to_behavior["T"], names_to_behavior["F"]
        else:
            suggestions[2], suggestions[0] = names_to_behavior["T"], names_to_behavior["F"]


print("State: ", [g.__name__ for g in gods], "x = True, y = False" if X else "y = True, x = False")
print("Suggestions: ", [g.__name__ for g in suggestions])
