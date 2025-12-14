import pandas as pd
import numpy as np

data = {
    'Region': ['East', 'West', 'East', 'West', 'North', 'North'],
    'Month': ['Jan', 'Feb', 'Jan', 'Feb', 'Jan', 'Feb'],
    'Product': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Sales': [100, 150, 200, 50, 80, 120]
}
df1 = pd.DataFrame(data)

print("--- 1. إطار البيانات الأصلي (Long Format) ---")
print(df1)
print("-" * 50)
# استخدام pivot_table
pivot_sales = pd.pivot_table(
    df1,
    index='Region',          # ماذا نضع في الصفوف (الفهرس الجديد)
    columns='Month',         # ماذا نضع في الأعمدة
    values='Sales',          # ما هي القيم التي سنلخصها
    aggfunc='sum',           # كيف نلخص القيم (باستخدام المجموع)
    fill_value=0             # ملء الخلايا الفارغة بقيمة 0 بدلاً من NaN
)

print("--- 2. جدول ملخص المبيعات (Pivot Table) ---")
print(pivot_sales)
print("-" * 50)
# حساب المجموع والمتوسط لنفس البيانات
pivot_multi_agg = pd.pivot_table(
    df1,
    index='Region',
    columns='Month',
    values='Sales',
    aggfunc=['sum', 'mean']
)

print("--- 3. جدول يلخص المجموع والمتوسط ---")
print(pivot_multi_agg)
print("-" * 50)
d = {'key1': {'a': 5, 'c': 90, 5: 50}, 'key2':{'b': 3, 'c': "yes"}}
d[5] = {1: 2, 3: 4}
print(d)