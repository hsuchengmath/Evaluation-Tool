import numpy as np

true_rank = [1,2,3,4,5]
rank = [2,2,2,1,4]


def NDCG_Function(rank):
    rank_score = [max(rank)-rank[i]+1 for i in range(len(rank))]
    rank_score_sorted = sorted(rank_score,reverse=True)

    DCG = sum([((2**rank_score[i])-1)/(np.log2(i+2)) for i in range(len(rank_score))])
    IDCG  = sum([((2**rank_score_sorted[i])-1)/(np.log2(i+2)) for i in range(len(rank_score_sorted))])
    ncdg = DCG/IDCG
    return ncdg

NDCG = NDCG_Function(rank)
print(NDCG)
