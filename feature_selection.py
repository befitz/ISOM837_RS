from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

X = rs_train[['price_per_ticket', 'seat_row', 'paid_full_price', 'paid_online',
       'Regular_Ticket', 'age', 'est_income', 'Male', 'married', 'fam_w_kids',
       'kids_in_house', 'from_Boston', 'from_MA','game_hour',
       'RS_v_Yankees', 'STH_Act', 'BUSINESS_STH_Act',
       'GROUP_Act', 'BUSINESS_act', 'Individual_Act', 'SPONSOR_Act',
       'EMPLOYEE_Act', 'April', 'May', 'June', 'July', 'August', 'September',
       'Thursday', 'Sunday', 'Tuesday', 'Wednesday', 'Saturday', 'Friday',
       'Monday', 'low_scale_seat', 'med_scale_seat', 'high_scale_seat']]

y = rs_train['ticket_used']
names = pd.DataFrame(X.columns)

model_fs = SelectKBest(score_func = chi2, k=4)
fs_results = model_fs.fit(X,y)

#print(fs_results.scores_)
results_df = pd.DataFrame(fs_results.scores_)
scored= pd.concat([names, results_df], axis=1)
scored.columns = ["Feature", "Score"]
scored.sort_values(by=["Score"])
