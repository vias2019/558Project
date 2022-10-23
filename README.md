README: 558 Project

Name: Dictionary

Contributors: Ruby Zhao, Tomas Kao, and Viktoriya Grishkina

GitHub: https://github.com/vias2019/558Project

Description:

“Dictionary” application translates English into Spanish. The application consists of three main parts: client side, server side, and database file.

Client: client_A.py and client_B.py - are run from a client’s side. A user should update “host” and “port” variables in order to run this file. The clients are running at the same time using separate threads. Currently, we are using time.sleep() to prolong the run time of each thread to demonstrate concurrency using threads.

Server: multi_thread_server.py - runs on the Azure Virtual Machine. A user should update “host” (an internal IP address) and “port” variables to run this file. Also, dictionary.py (hash table class) is stored on the server side.

Database: dictionary.py - Dictionary class which has a hash table as its property along with “searchDictionary” function. The dictionary stores key:values (English word: Spanish word). 

Execution:
IDE: VS Code/Intellij IDEA

Localhost - the application can be run using localhost for testing purposes. 
Assume you know what English vocabulary is or expected in the dictionary, and now you would like to find what its meaning is in Spanish. The following words are already in dictionary
“quick”, “brown”, “fox”, “jump”, “over”, “lazy”, “dog”, “hello”, “world”
Step1: Execute first multi_thread_server.py
Step2: Run client_A.py
Step3: Run client_B.py


Cloud (in case if multi_thread_server.py is run on the cloud)
Step1: Set up VM in Azure and enable VM
Step2: Deploy multi_thread_server.py on VM
Step3: Assign the VM’s private IP address to variable (TCP_IP) in multi_thread_server.py
Step4: Assign the VM’s public IP address to variable (host) in client_A.py and client_B.py
Step5: Execute .py files and follow the steps from the “localhost” section above.


