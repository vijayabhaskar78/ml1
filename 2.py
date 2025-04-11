import pandas as pd

df = pd.DataFrame([
    ["Morning", "Sunny", "Warm", "Yes", "Mild", "Strong", "Yes"],
    ["Evening", "Rainy", "Cold", "No", "Mild", "Normal", "No"],
    ["Morning", "Sunny", "Moderate", "Yes", "Normal", "Normal", "Yes"],
    ["Evening", "Sunny", "Cold", "Yes", "High", "Strong", "Yes"]
])

h = ['0'] * 6
for r in df.values:
    if r[6] == 'Yes':
        for i in range(6):
            h[i] = r[i] if h[i] in ['0', r[i]] else '?'
print("Final Hypothesis:", h)
