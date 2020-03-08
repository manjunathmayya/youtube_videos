'''

1. Download TFS power tools
https://marketplace.visualstudio.com/items?itemName=TFSPowerToolsTeam.MicrosoftVisualStudioTeamFoundationServer2015Power

2. Running the command
    i. Go to the TFS mapped path. Ex: D:\TFS_WORKING_FOLDER
    ii. Execute the command 
    Ex: tfpt workitem /new Project1\Task /fields:"Title=New;Area Path= myArea\path;Assigned To= XXXXXX"
    On success, message "Work item 385356 created." is displayed.

'''

import os

def CreateTask(title, assigned_to, description):
    
    command = 'tfpt workitem /new Project1\Task /fields:"Area Path= myArea\path;Title=' + title +';'
    command += 'Assigned To='+ assigned_to + ';'
    command += 'Iteration Path= Iter\Path;'
    command +=  'Description=' + description 
    
    #NOTE: Update the project path, area path and iteration path according to your project, before executing this script !!!
    
    print ('Command executed: ' + command)
    path = "D:\TFS_WORKING_FOLDER"
    os.chdir(path)
    os.system(command)     
    #Below message will be seen after command execution "Work item 385356 created."


CreateTask('title of task', 'myself', 'description of task')
