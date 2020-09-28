Create the following folders D:python\385\venv\

Install Python 64-bit in "D:python\385" for your user only without adding it to the path

Open the Terminal (CMD, PowerShell, New Terminal)

Navigate to "D:\python\385"

Create the virtual environment "study":
	D:\python\385>python -m venv d:\python\385\.myvenv\study

Activate the virtual environment "study":
	D:\python\385>.myvenv\study\Scripts\activate
	
Test the virtual environment "study":
	(study) D:\python\385>python
	
Install Pandas:
	(study) D:\python\385>pip install pandas	

In VSCode, go to your project's folder and locate "settings.json" inside the folder ".vscode"

Update the python.pythonPath as follows:
{
    "python.pythonPath": "D:\\python\\385\\.myvenv\\study\\Scripts\\python.exe"
} 

In PowerShell allow scripts to be run (this is done only once):
	PS C:\Users\mkrast01> Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser

Deactivate the virtual environment "study":
	(study) D:\python\385>deactivate

Remove the virtual environment "study":
	After deactivating the environment navigate to the folder where it is located:
		D:\python\385>cd .myvenv
	And run
		D:\python\385\.myvenv>rm -r study
	The "study" folder will be deleted allong with ts content (this can be also done manually).
