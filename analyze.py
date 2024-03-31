import os
import json
import math
import pandas as pd
import numpy as np

folder = 'report_cards/'
report_card_files = [i for i in os.listdir(folder) if i.endswith('.json')]
report_cards = []

for file_name in report_card_files:
    with open(os.path.join(folder, file_name), 'r') as f:
        report_cards.append(json.load(f))


def corr_coe(x, y):
    n = len(x)
    if n <= 1 or (np.std(x) == 0) or (np.std(y) == 0):
        return "NaN"
    xy = [i * j for i, j in zip(x, y)]
    xsqr = [i ** 2 for i in x]
    ysqr = [i ** 2 for i in y]
    return (n * sum(xy) - sum(x) * sum(y)) / (math.sqrt((n * sum(xsqr) - (sum(x) ** 2)) * (n * sum(ysqr) - (sum(y) ** 2))))


subjects = set()
for card in report_cards:
    subjects.update(card.keys())

results = []
for subject1 in subjects:
    for subject2 in subjects:
        if subject1 != subject2:
            x = []
            y = []
            for card in report_cards:
                if subject1 in card and subject2 in card:
                    x.append(card[subject1])
                    y.append(card[subject2])
            if x and y:
                correlation = corr_coe(x, y)
                results.append((subject1, subject2, correlation))
            else:
                results.append((subject1, subject2, np.nan))

df = pd.DataFrame(results, columns=['Subject1', 'Subject2', 'Correlation'])
with open('last_run.json', 'w') as f:
    json.dump(df.to_dict(orient='dict'), f, indent=4)

if __name__ == "__main__":
    # Convert results into Excel spreadsheet
    df.to_excel('correlation_results.xlsx', index=False)
