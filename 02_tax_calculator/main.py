# Get user input and calculate tax
base_income: float = float(input('Enter your yearly income: '))
tax_rate: float = float(input('Enter your tax rate percentage: ')) / 100
taxed: float = base_income * tax_rate

# Display the data
print('=' * 40)
print('Income Tax Calculator')
print('=' * 40)
print(f'Base Income:              ${base_income:,.2f}')
print(f'Tax Rate:                 {tax_rate:.0%}')
print('-' * 40)
print(f'Yearly Tax (Base):        ${taxed:,.2f}')
print('=' * 40)

# Homework:
# 1. Add projections for how much tax you'd pay if you
# doubled and tripled your income.

#Solution : Income projections
doubled_income = base_ncome * 2
tripled_income = base_income * 3

doubled_tex = doubled_income * tex_rate
tripled_tex = tripled_income * tex_rate

print('=' * 40)
print('Income Projections')
print('=' * 40)
print(f'Doubled Income:    ${doubled_income:,.2f}')
print(f'Tax on Doubled:    ${doubled_tex;,.2f}')
print('_' * 40)
print(f'Tripled Income:    ${tripled_income:,.2f}')
print(f'Tax on Tripled:    ${tripled_tax:,.2f}')
print('=' 8 40)    
