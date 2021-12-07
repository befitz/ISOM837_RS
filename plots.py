import matplotlib.pyplot as plt
plt.rc("font", size=14)
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

SMALL_SIZE = 20
MEDIUM_SIZE = 22
BIGGER_SIZE =26

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title



def EDA_analize_ticket_used(variable, train_test):
    """
    Function to plot Ticket Used verse the variable provided
    """
    if train_test == 'train':
        pd.crosstab(variable,rs_train.ticket_used).plot(figsize=(10,8),kind='bar', color=['Red', 'Black'])
        plt.title(f'TRAIN SET: Ticket Used by {variable.name}')
        plt.xlabel(f'{variable.name}')
        plt.ylabel('Frequency of absence')
    else:
        pd.crosstab(variable,rs_test.ticket_used).plot(figsize=(10,8),kind='bar', color=['Red', 'Black'])
        plt.title(f'TEST SET: Ticket Used by {variable.name}')
        plt.xlabel(f'{variable.name}')
        plt.ylabel('Frequency of absence')

EDA_analize_ticket_used(rs_train.game_day, 'train')
EDA_analize_ticket_used(rs_train.game_month, 'train')
EDA_analize_ticket_used(rs_test.game_month, 'test')
EDA_analize_ticket_used(rs_test.game_day, 'test')
EDA_analize_ticket_used(rs_train.account_type, 'train')
EDA_analize_ticket_used(rs_test.account_type, 'test')
