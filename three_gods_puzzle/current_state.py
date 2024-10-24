from random import shuffle, randint as ri


# you don't know what is X and Y
X, Y = (True, False) if ri(0, 1) else (False, True)

bool_to_xy = {X: "X", Y: "Y"}


# gods behavior functions
def t(ans):
    return bool_to_xy[ans]


def f(ans):
    return bool_to_xy[not ans]


def r(ans):
    return bool_to_xy[bool(ri(0, 1))]


gods = [t, f, r]

names_to_behavior = {
    "T": t,
    "F": f,
    "R": r,
}

# you don't know which god is who
shuffle(gods)


# ______________________________________________LOGICAL_CONSTRUCTIONS___________________________________________________
def god_is(god_index_to, god_index_about, he_is):
    # Is that god of Truth("T")/Lies("F")/Random("R")?
    return gods[god_index_to](gods[god_index_about] == names_to_behavior[he_is])


def answer_is_x(god_index_to, question):
    # If I ask that god this, will his answer be 'X'?
    return gods[god_index_to](question == "X")
# ________________________________________________USING_QUESTIONS_______________________________________________________


def isYourAnswerWillBe_X_IfIAskYou_IsTheThirdGodTheGodOfRandom__to_the_first_god():
    return answer_is_x(0, god_is(0, 2, "R"))


def isYourAnswerWillBe_X_IfIAskYou_IsTheThirdGodTheGodOfRandom__to_the_second_god():
    return answer_is_x(1, god_is(1, 2, "R"))


def isYourAnswerWillBe_X_IfIAskYou_AreYouTheGodOfTruth__to_the_first_god():
    return answer_is_x(0, god_is(0, 0, "T"))


def isYourAnswerWillBe_X_IfIAskYou_AreYouTheGodOfTruth__to_the_second_god():
    return answer_is_x(1, god_is(1, 1, "T"))


def isYourAnswerWillBe_X_IfIAskYou_IsTheFirstGoodTheGodOfRandom__to_the_third_god():
    return answer_is_x(2, god_is(2, 0, "R"))
