import pandas as pd


dataFrame = pd.read_csv('wine+quality/winequality-red.csv', sep=';')

# print(dataFrame.head())
print(dataFrame.head(2))
print('dataFrame.shape: ', dataFrame.shape)

dataFrame.info()

# 정답 데이터 만들기
# True: 1, False: 0
dataFrame['good'] = (dataFrame['quality'] >= 7).astype(int)

y = dataFrame['good']

# 문제 데이터 만들기
X = dataFrame.drop(
    columns=['quality', 'good']
)

# 데이터 쪼개기
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 의사 결정 트리
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train) # 학습

wine = [[
    7.5,      
    0.75,         
    5.50,
    2.75,
    0.075,
    12.5,
    50.0,
    6.3125,
    3.75,
    1.75,
    9.5
]]

wine_df = pd.DataFrame(wine)

wine_pred = model.predict(wine_df)
print('Pred 예측 결과', wine_pred)

wine_prob = model.predict_proba(wine_df)
print('Prob 예측 결과', wine_prob)
print('Prob 예측 결과', wine_prob)
print('Prob 예측 결과', wine_prob)