
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def prCurve(labels, scores):
    assert(len(labels) == len(scores))
    ls = sorted(list(zip(labels, scores)), key=lambda x: x[1], reverse=True)
    pos_num = labels.count(1)
    pr = []
    for i in range(1, len(ls) + 1):
        tp = [x[0] for x in ls[0: i]].count(1)
        recall = 1.0 * tp / pos_num
        precision = 1.0 * tp / i
        pr.append((recall, precision))
    return pr


def rocCurve(labels, scores):
    assert(len(labels) == len(scores))
    ls = sorted(list(zip(labels, scores)), key=lambda x: x[1], reverse=True)
    pos_num = labels.count(1)
    neg_num = len(labels) - pos_num
    roc = []
    for i in range(1, len(ls) + 1):
        tp = [x[0] for x in ls[0: i]].count(1)
        fp = [x[0] for x in ls[0: i]].count(0)
        tpr = 1.0 * tp / pos_num
        fpr = 1.0 * fp / neg_num
        roc.append((fpr, tpr))
    return roc


def calc_auc(labels, scores):
    assert(len(labels) == len(scores))
    pos_num = labels.count(1)
    neg_num = len(labels) - pos_num
    ls = sorted(list(zip(labels, scores)), key=lambda x: x[1], reverse=False)
    rank_sum = 0
    for i in range(len(ls)):
        if ls[i][0] == 1:
            rank_sum += i
    auc = 1.0 * (rank_sum - pos_num * (pos_num - 1) * 0.5) / (pos_num * neg_num)
    return auc


if __name__ == '__main__':
    a = [1, 0, 1]
    b = [0.8, 0.3, 0.6]
    res = calc_auc(a, b)
    print(res)




