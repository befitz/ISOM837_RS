from sklearn.metrics import accuracy_score


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.3, random_state=0)

max_depth = []
acc_gini = []
acc_entropy = []
for i in range (1,30):
    dtree = DecisionTreeClassifier(criterion='gini', max_depth=i)
    dtree.fit(X_train,y_train)
    pred = dtree.predict(X_test)
    acc_gini.append(accuracy_score(y_test, pred))
    ##
    dtree = DecisionTreeClassifier(criterion = 'entropy', max_depth = i)
    dtree.fit(X_train, y_train)
    pred = dtree.predict(X_test)
    acc_entropy.append(accuracy_score(y_test, pred))
    ###
    max_depth.append(i)

d = pd.DataFrame({'acc_gini': pd.Series(acc_gini),
                'acc_entropy': pd.Series(acc_entropy),
                'max_depth': pd.Series(max_depth)})

plt.figure(figsize = (8,8))
plt.plot('max_depth', 'acc_gini', data = d, label= 'gini')
plt.plot('max_depth', 'acc_entropy', data= d, label='entropy')
plt.xticks(np.arange(0, len(max_depth)+1, 2))

plt.xlabel('max_depth')
plt.ylabel('accuracy')
plt.legend()
