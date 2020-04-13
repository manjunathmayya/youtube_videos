import pandas as pd

''' Read first excel file '''
team_time_excel = pd.ExcelFile('team_time.xlsx')
team_time_data = team_time_excel.parse('Sheet1')


''' Read second excel file '''
team_data_excel = pd.ExcelFile('team_info.xlsx')
team_data = team_data_excel.parse('Sheet1')


''' Calculate effort of each person '''
effort_data = team_time_data.groupby(['Email']).agg({'Effort': ['sum']})


''' Add effort data to 1st file '''
effort_list = []
for index, row in team_data.iterrows():
    effort_list.append (effort_data.loc[row['Email']][0])

team_data["Effort"] = effort_list
team_data.to_excel('new_data.xlsx')
