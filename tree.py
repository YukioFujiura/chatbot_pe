import pandas as pd
from sklearn import tree

data = pd.read_csv('kc_house_data.csv', sep=',')

filtered_data = data.query("zipcode==98008")
filtered_data = filtered_data.reset_index(drop=True)

filtered_data['price_sqft'] = filtered_data['price']/filtered_data['sqft_living']

average = round(filtered_data['price_sqft'].mean(), 2)

filtered_data['pricing'] = filtered_data['price_sqft'] > average
filtered_data['pricing'] = filtered_data['pricing'].replace([False, True], [0,1])

aval_data = filtered_data.tail(10)

filtered_data = filtered_data[:-10]

filtered_data.to_csv(r'filtered_data.csv', index=False)
aval_data.to_csv(r'aval_data.csv', index=False)

print('arquivos gerados')

train = pd.read('filtered_data.csv')
train = pd.read_csv('filtered_data.csv')

columns = ['bedrooms', 'bathrooms', 'floors', 'view', 'condition', 'pricing']
train = train[columns]

y_train = train['pricing']
x_train = train.drop(['pricing'], axis=1).values

decision_tree = tree.DecisionTreeClassifier(max_depth = 20)
decision_tree.fit(x_train, y_train)

with open("decision_tree.dot", 'w') as f:
    f = tree.export_graphviz(decision_tree,
                             out_file=f,
                             max_depth=20,
                             impurity=True,
                             feature_names=list(train.drop(['pricing'], axis=1)),
                             class_names=['False', 'True'],
                             rounded=True,
                             filled=True)
print('.dot gerado')