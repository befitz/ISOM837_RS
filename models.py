from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from scipy import stats

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import plot_tree
import warnings

from sklearn import tree

from variable_creation import train_test

train, test = train_test()

def decision_tree(df):
    X = df[['price_per_ticket', 'paid_full_price', 'paid_online',
           'Regular_Ticket', 'age', 'est_income', 'Male', 'married', 'fam_w_kids',
           'kids_in_house', 'from_Boston', 'from_MA','game_hour',
           'RS_v_Yankees', 'STH_Act', 'BUSINESS_STH_Act',
           'GROUP_Act', 'BUSINESS_act', 'Individual_Act', 'SPONSOR_Act',
           'EMPLOYEE_Act', 'April', 'May', 'June', 'July', 'August', 'September',
           'Thursday', 'Sunday', 'Tuesday', 'Wednesday', 'Saturday', 'Friday',
           'Monday', 'low_scale_seat', 'med_scale_seat', 'high_scale_seat']]
    y = df['ticket_used']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.3, random_state=0)
    tree_test = DecisionTreeClassifier(max_depth = 5)
    tree_test.fit(X_train,y_train)
    y_pred_test = tree_test.predict(X_test)


    cm_test = confusion_matrix(y_test, y_pred_test)
    plt.figure(figsize=(8,8))
    sns.heatmap(data=cm_test, linewidths=.5, annot=True, square=True, cmap='Reds', fmt="d", cbar=False)
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    all_sample_title = 'Decision Tree: 70/30 Split Accuracy Score:{:.4f}'.format(tree_test.score(X_test, y_test))
    plt.title(all_sample_title)
    from sklearn import tree
    fn = ['price_per_ticket', 'paid_full_price', 'paid_online',
           'Regular_Ticket', 'age', 'est_income', 'Male', 'married', 'fam_w_kids',
           'kids_in_house', 'from_Boston', 'from_MA','game_hour',
           'RS_v_Yankees', 'STH_Act', 'BUSINESS_STH_Act',
           'GROUP_Act', 'BUSINESS_act', 'Individual_Act', 'SPONSOR_Act',
           'EMPLOYEE_Act', 'April', 'May', 'June', 'July', 'August', 'September',
           'Thursday', 'Sunday', 'Tuesday', 'Wednesday', 'Saturday', 'Friday',
           'Monday', 'low_scale_seat', 'med_scale_seat', 'high_scale_seat']
    text_representation = tree.export_text(tree_test, feature_names = fn, show_weights=True)
    print(text_representation)

decision_tree(train)
