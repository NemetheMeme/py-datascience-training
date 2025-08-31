import pandas as pd
import numpy as np
from scipy import stats

# determine if the scores belong to the same probability distribution through T-tests
data = pd.read_csv("exams.csv")

score_columns = ['math score', 'reading score', 'writing score']
alpha = 0.05

# testing functions

def check_normality(series, alpha=0.05):
    stat, p = stats.shapiro(series)
    return p

def check_equal_variance(x,y):
    stat, p = stats.levene(x,y)
    return p

# 1. define the H0 -> try T tests for independent datas
# 2. define the H0 -> try T tests for paired data

#1 T-tests independent
#
# if we formulate the null hypothesis as negated, the condition changes to <, if the null condition is positive we change it to > -> pval < | > alpha
print("===== T-test independent (two-sample) =====")
pairs = [('math score','reading score'), ('math score','writing score'), ('reading score','writing score')]

#### CHAT's implementation and logic
#
# for a,b in pairs:
#     x = data[a].dropna()
#     y= data[b].dropna()
#
#     p_shap_x = check_normality(x)
#     p_shap_y = check_normality(y)
#     p_levene = check_equal_variance(x,y)
#
#     tstat, pval = stats.ttest_ind(x,y,equal_var=(p_levene > alpha))
#
#     print(f"\nPair: {a} vs {b}")
#     print(f" Shapiro p-values: {a}={p_shap_x:.4f}, {b}={p_shap_y:.4f}  (H0: normalitate)")
#     print(f" Levene p-value (equal variances?): {p_levene:.4f}")
#     print(f" t-statistic = {tstat:.4f}, p-value = {pval:.6f}")
#     if pval < alpha:
#         print(f" => p < {alpha}: we deny H0 (mean values are significant different).")
#     else:
#         print(f" => p >= {alpha}: we do not have proof to deny H0 (mean values can be equal).")
#
#
# # 2. Paired tests
#
# print("\n===== T-test paired (paired samples) =====")
# for a,b in pairs:
#     paired = data[[a,b]].dropna()
#     x = paired[a]
#     y = paired[b]
#     diff = x - y
#     p_shap_diff = stats.shapiro(diff)[1]
#     tstat, pval = stats.ttest_rel(x, y)
#
#     print(f"\nPair: {a} vs {b}")
#     print(f" Shapiro on differences p-value = {p_shap_diff:.4f}  (H0: differences ~ normal)")
#     print(f" t-statistic (paired) = {tstat:.4f}, p-value = {pval:.6f}")
#     if pval < alpha:
#         print(f" => p < {alpha}: we deny H0 (mean values are significant different).")
#     else:
#         print(f" => p >= {alpha}: we do not have proof to deny H0 (mean values can be equal).")
