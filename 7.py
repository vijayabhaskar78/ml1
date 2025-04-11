import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

df = pd.read_csv("heart.csv")  # UCI Heart Dataset

model = BayesianModel([('cp', 'target'), ('thalachh', 'target'), ('exng', 'target')])
model.fit(df, estimator=MaximumLikelihoodEstimator)

infer = VariableElimination(model)
q = infer.query(variables=['target'], evidence={'cp': 1, 'thalachh': 150, 'exng': 0})
print(q)
