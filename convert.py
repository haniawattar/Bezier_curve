# -*- coding: utf-8 -*-
#
# Copyright 2019  Projektpraktikum Python.
# SPDX-License-Identifier: Apache-2.0

"""Bezier curve conversion functions
"""
import matplotlib.pyplot as plt




def range_t(listp1, listc1, listc2, listp2, precision):

    """ this function calculates the range of t
    Keyword arguments:
    listp1 --  Punkt 1
    listc1 --  Punkt 2
    listc2 --  Punkt 3
    listp2 --  Punkt 4
    precision --  Genauigkeit
    """
    max_distance_1 = max(abs(listc1[0] - listp1[0]), abs(listc1[1]-listp1[1]))
    max_distance_2 = max(abs(listc2[0] - listc1[0]), abs(listc2[1]-listc1[1]))
    max_distance_3 = max(abs(listp2[0] - listc2[0]), abs(listp2[1]-listc2[1]))

    max_distance = max(max_distance_1, max_distance_2, max_distance_3)
    t_precision = precision/max_distance
    list_t = []
    tvar = 0.0
    while tvar < 1.0:
        list_t.append(tvar)
        tvar += t_precision
    list_t.append(1)

    return list_t


def linear(listp1, listp2, list_t):
    """ get Two Points as List[x,y] and a list of TVektor
    Keyword arguments:
    pkt1x -- X-KO von Punkt 1
    pkt1y -- Y-KO von Punkt 1
    pkt2x -- X-KO von Punkt 2
    pkt2y -- Y-KO von Punkt 2
    precision --  Genauigkeit
    list_t -- T-Vektor
    """
    pkt1x = listp1[0]
    pkt1y = listp1[1]
    pkt2x = listp2[0]
    pkt2y = listp2[1]
    list_x = []
    list_y = []
    for index in list_t:
        l0x = (1-index) * pkt1x + index * pkt2x
        l0y = (1-index) * pkt1y + index * pkt2y
        list_x.append(l0x)
        list_y.append(l0y)
    return list_x, list_y



def quad(listofpoints, list_t):
    """ get Two Points and Precision and a T-List
    Keyword arguments:
    pkt1x -- X-KO von Punkt 1
    pkt1y -- Y-KO von Punkt 1
    pkt2x -- X-KO von Punkt 2
    pkt2y -- Y-KO von Punkt 2
    precision --  Genauigkeit
    list_t -- T-Vektor
    listofpoints=[p1x,p1y,c1x,c1y,c2x,c2y,p2x,p2y]
    """
    lst = listofpoints
    list_x_1, list_y_1 = linear([lst[0], lst[1]], [lst[2], lst[3]], list_t)
    list_x_2, list_y_2 = linear([lst[2], lst[3]], [lst[4], lst[5]], list_t)
    list_x_3, list_y_3 = linear([lst[4], lst[5]], [lst[6], lst[7]], list_t)
    g0x_list = []
    g0y_list = []
    g1x_list = []
    g1y_list = []

    for indexi, indext in enumerate(list_t):
        g0x_list.append((1-indext) * list_x_1[indexi] + indext * list_x_2[indexi])
        g0y_list.append((1-indext) * list_y_1[indexi] + indext * list_y_2[indexi])

    for indexi, indext in enumerate(list_t):
        g1x_list.append((1-indext) * list_x_2[indexi] + indext * list_x_3[indexi])
        g1y_list.append((1-indext) * list_y_2[indexi] + indext * list_y_3[indexi])

    return g0x_list, g0y_list, g1x_list, g1y_list


def quad2(listofpoints, list_t):
    """ get Two Points and Precision and a T-List
    Keyword arguments:
    pkt1x -- X-KO von Punkt 1
    pkt1y -- Y-KO von Punkt 1
    pkt2x -- X-KO von Punkt 2
    pkt2y -- Y-KO von Punkt 2
    precision --  Genauigkeit
    list_t -- T-Vektor
    listofpoints=[p1x,p1y,c1x,c1y,c2x,c2y,p2x,p2y]
    """
    lst = listofpoints
    list_x_1, list_y_1 = linear([lst[0], lst[1]], [lst[2], lst[3]], list_t)
    list_x_2, list_y_2 = linear([lst[2], lst[3]], [lst[4], lst[5]], list_t)
    g0x_list = []
    g0y_list = []
    for indexi, indext in enumerate(list_t):
        g0x_list.append((1-indext) * list_x_1[indexi] + indext * list_x_2[indexi])
        g0y_list.append((1-indext) * list_y_1[indexi] + indext * list_y_2[indexi])
    return g0x_list, g0y_list


def kubisch(listofpoints, list_t):
    """ get Two Points and Precision and a T-List
    Keyword arguments:
    listofpoints
    pre
    list_t """
    lst = listofpoints
    c0x_list = []
    c0y_list = []
    g0x_lst, g0y_lst = quad2([lst[0], lst[1], lst[2], lst[3], lst[4], lst[5]], list_t)
    g1x_lst, g1y_lst = quad2([lst[2], lst[3], lst[4], lst[5], lst[6], lst[7]], list_t)
    for indexi, indext in enumerate(list_t):
        c0x = (1-indext) * g0x_lst[indexi] + indext * g1x_lst[indexi]
        c0y = (1-indext) * g0y_lst[indexi] + indext * g1y_lst[indexi]
        c0x_list.append(c0x)
        c0y_list.append(c0y)

    return c0x_list, c0y_list


LIST_T = range_t([2, 2], [6, 8], [10, 8], [12, 4], 0.1)
LIST_T_TEST = range_t([2, 2], [1, 2], [2, 1], [3, 2], 0.1)
print(LIST_T_TEST)

C0XLIST, C0YLIST = kubisch([2, 2, 6, 8, 10, 8, 12, 4], LIST_T)
G0XLIST, G0YLIST, G1XLIST, G1YLIST = quad([2, 2, 6, 8, 10, 8, 12, 4], LIST_T)
print(kubisch([2, 2, 1, 2, 2, 1, 3, 2], LIST_T_TEST))

LISTX1, LISTY1 = linear([2, 2], [6, 8], LIST_T)
print(LISTX1)
print(LISTY1)
LISTX2, LISTY2 = linear([6, 8], [10, 8], LIST_T)
LISTX3, LISTY3 = linear([10, 8], [12, 4], LIST_T)

# plot linear functions
plt.plot(LISTX1, LISTY1, color='g', linestyle='-')
plt.plot(LISTX2, LISTY2, color='g', linestyle='-')
plt.plot(LISTX3, LISTY3, color='g', linestyle='-')

# plot quadratic function
plt.plot(G0XLIST, G0YLIST, color='b', linestyle='-')
plt.plot(G1XLIST, G1YLIST, color='b', linestyle='-')

# plot cubic function
plt.plot(C0XLIST, C0YLIST, color='r', linestyle='-', label='Curve')
plt.grid(linestyle='-', axis='both', drawstyle='steps-pre')
plt.xlabel('x-Axis')
plt.ylabel('y-Axis')
plt.show()
