Welcome to CareerRecomedator! 

This is a relatively simple software used to recommend careers in UVG, based in 4 simple questions.
The code is written in Python and uses Neo4J to create relationships between everything.

There are 2 things that you need:
1. Python 3.7 (or  any newer version, just make sure its 3.something) You can get it here: https://www.python.org/downloads/
2. Neo4J You can get it here:https://neo4j.com/download/

Make sure to download and install everything

First, we will fiddle with Python
1. Type python in your Windows Search funtion
2. Right click on Python 3.x and click "Go to folder"
3. Click on the file path on top of the window and copy it
4. Follow this tutorial: https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/
5. On the last step, paste the direction we got in step number 3
6. Press Windows + R on your keyboard, type "cmd" and press enter
7. Type "python -m pip install Tkinter", press Enter and wait for install to finish
8. Type "python -m pip install neo4j", press Enter and wait for install to finish
9. Close the cmd, we are done with it

Now, onto Neo4J
1. Click on "Add Graph" and select "Create Local Graph"
2. Wait for it to be created and click "Start"
3. Click "Manage" and "Open in Browser"
4. Type ":server connect" in the top of the window
5. Make sure the URL is bolt://localhost:7687
6. If it is, jump to line 11 
7. If not, let´s take a little detour
8. Go to the folder: AED_Proyecto
9. Open the file DBMain.py with your favourite text editor (we reommend Notepad++)
10. Change line 7 to match the URL of line 5
11. Press enter
12. Copy the contents of the file DataBase.txt
13. Paste them in the line at the top of the window
14. Click run
15. Wait for it to be finished and minimize Neo4J

Now, let´s run the program!
1. In the Folder AED_Proyecto
2. Look for the file named "DBMain.py"
3. Right click on this file, select "Open with" and then click "Python"
4. Enjoy!
