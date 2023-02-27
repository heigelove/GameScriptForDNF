"""
@File buttonEnum.py
@Contact cmrhyq@163.com
@License (C)Copyright 2022-2025 AlanHuang
@Modify Time 2023/2/24 15:55
@Author Alan Huang
@Version 0.0.1
@Description None
"""
from enum import Enum


class LeftKeyBoard(Enum):
    A = 65
    B = 66
    C = 67
    D = 68
    E = 69
    F = 70
    G = 71
    H = 72
    I = 73
    J = 74
    K = 75
    L = 76
    M = 77
    N = 78
    O = 79
    P = 80
    Q = 81
    R = 82
    S = 83
    T = 84
    U = 85
    V = 86
    W = 87
    X = 88
    Y = 89
    Z = 90
    k0 = 48
    k1 = 49
    k2 = 50
    K3 = 51
    k4 = 52
    k5 = 53
    k6 = 54
    k7 = 55
    k8 = 56
    k9 = 57


class RightKeyBoard(Enum):
    k0 = 96
    k1 = 97
    k2 = 98
    K3 = 99
    k4 = 100
    k5 = 101
    k6 = 102
    k7 = 103
    k8 = 104
    k9 = 105
    star_key = 106
    plus_key = 107
    enter = 108
    minus_key = 109
    dot_key = 110
    left_slash = 111


class FunctionKeyBoard(Enum):
    F1 = 112
    F2 = 113
    F3 = 114
    F4 = 115
    F5 = 116
    F6 = 117
    F7 = 118
    F8 = 119
    F9 = 120
    F10 = 121
    F11 = 122
    F12 = 123


class ControlKeyBoard(Enum):
    backspace = 8
    tab = 9
    clear = 12
    enter = 13
    shift = 16
    control = 17
    alt = 18
    cape_lock = 20
    esc = 27
    space_bar = 32
    page_up = 33
    page_down = 34
    end = 35
    home = 36
    left_arrow = 37
    up_arrow = 38
    right_arrow = 39
    down_arrow = 40
    insert = 45
    delete = 46
    num_lock = 144
    semicolon_or_colon = 186
    equal_or_plus = 187
    comma_or_less_than_sign = 188
    minus_or_underline = 189
    dot_or_greater_than_sign = 190
    left_slash_or_question_mark = 191
    tilde = 192
    left_parenthesis = 219
    right_slash = 220
    right_parenthesis = 221
    quotation = 222
