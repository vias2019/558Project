# 558Project
README: 558 Project

Name: Dictionary

Contributors: Ruby Zhao, Tomas Kao, and Viktoriya Grishkina

GitHub: https://github.com/vias2019/558Project

Description:

“Dictionary” application translates English words into Spanish. In case an English word is missing in the database, the application offers to add a new key:value pair to the dictionary. The application is offering either search for a word translation or add a new word to the dictionary. The application consists of three main parts: client side, server side, and database part.

Client: client_A.py - runs from a client’s side. A user should update “host” and “port” variables in order to run this file.

Server: multi_thread_server.py - runs in the Azure Virtual Machine. A user should update “host” and “port” variables to run this file. Also, dictionary.py (hash table class) is stored on the server side.

Database: dictionary.py - Dictionary class which has a hash table as its property along with “searchDictionary” and “addDictionary” functions.

Execution:
IDE: VS Code/Intellij IDEA

Localhost - the application can be run using localhost for testing purposes. 
Assume you know what English vocabulary is or expected in the dictionary, and now you would like to find what its meaning is in Spanish. The following words are already in dictionary
“quick”, “brown”, “fox”, “jump”, “over”, “lazy”, “dog”, “hello”, “world”
Step1: Execute first multi_thread_server.py and then client_A.py
Step2: The program will offer the user an option to select either “01” or “ 02”.
Step3: Input the number according to the client_A.py message in the terminal.
“01” is for translation while “02” is for adding words into dictionary
Step4: Input, for example, “01” and word such as “dog”
Step5: Server receives the request and then responds “perro” to the client
Note: option “02” will offer to add an English and Spanish word into the dictionary

Cloud (in case if multi_thread_server.py is run on the cloud)
Step1: Set up VM in Azure and enable VM
Step2: Deploy multi_thread_server.py on VM
Step3: Assign the VM’s private IP address to variable (TCP_IP) in multi_thread_server.py
Step4: Assign the VM’s public IP address to variable (host) in client_A.py
Step5: Execute both py and follow the steps from the “localhost” section above.


