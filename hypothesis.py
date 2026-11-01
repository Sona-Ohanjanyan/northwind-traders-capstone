import pandas as pd

df = pd.read_csv(r"C:\Users\Asus\Desktop\power BI\final project\data\raw\fact_sales.csv")
print(df.head())



import pandas as pd
from scipy import stats

# Բեռնում ենք ֆայլը
df = pd.read_csv(
    r"C:\Users\Asus\Desktop\power BI\final project\data\raw\fact_sales.csv"
)

# 🧹 Մաքրում ենք սյունակների անունները 'Sum of ' նախածանցից
df.columns = df.columns.str.replace("Sum of ", "").str.strip()

# Տպում ենք մաքրված սյունակները
print("Մաքրված սյունակները:", df.columns.tolist())
print("-" * 40)

# 1. Կորելացիոն վերլուծություն
if "discount" in df.columns and "unit_price" in df.columns:
  corr = df["discount"].corr(df["unit_price"])
  print(f"Կորելացիա զեղչի և միավորի գնի միջև: {corr:.4f}")

# 2. T-test (Զեղչված և չզեղչված վաճառքների համեմատություն)
if "discount" in df.columns and "unit_price" in df.columns:
  group_with_discount = df[df["discount"] > 0]["unit_price"].dropna()
  group_without_discount = df[df["discount"] == 0]["unit_price"].dropna()

  t_stat, p_value = stats.ttest_ind(
      group_with_discount, group_without_discount, nan_policy="omit"
  )

  print("\n--- T-test Արդյունքներ ---")
  print(f"T-statistic: {t_stat:.4f}")
  print(f"P-value: {p_value}")

  if p_value < 0.05:
    print(
        "Եզրակացություն: P-value-ն < 0.05 է։ Մենք մերժում ենք զրոյական հիպոթեզը"
        " (H0): Զեղչերը վիճակագրորեն նշמעալի ազդեցություն ունեն միավորի գնի"
        " վրա։"
    )
  else:
    print(
        "Եզրակացություն: P-value-ն >= 0.05 է։ Զրոյական հիպոթեզը չի մերժվում։"
    )
