# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: fastai_22
#     language: python
#     name: python3
# ---

# %%
from math_ops.basic_math_ops import Multiplier

# %%
three_multiplier = Multiplier(3)
a = 10
b = three_multiplier(a)
print(f"three_mtulplier of {a} is {b}.")

# %%
