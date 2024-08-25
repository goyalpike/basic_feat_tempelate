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
from math_ops.basic_math_ops import Adder

# %% [markdown]
# Define an instance which always adds five.

# %%
five_adder = Adder(5)
a = 10
b = five_adder(a)
print(f"five_adder to {a} is {b}.")
