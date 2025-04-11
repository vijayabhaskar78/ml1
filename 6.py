from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

train = [
    "Team won match", 
    "Scored a goal", 
    "Player signed contract with club", 
    "Government passed law", 
    "Prime minister held press conference", 
    "PM gave speech"
]
labels = ["Sports", "Sports", "Sports", "Politics", "Politics", "Politics"]

test = [
    "The player signed a new contract with the club", 
    "The prime minister held a press conference"
]
true = ["Sports", "Politics"]

vec = CountVectorizer()
X = vec.fit_transform(train)
m = MultinomialNB().fit(X, labels)

pred = m.predict(vec.transform(test))
acc = (pred == true).mean() * 100

print(f"Accuracy: {acc:.1f} %")
for d, p in zip(test, pred):
    print(f"Document: '{d}' → Predicted Category: {p}")

