# Computer Security Final Project
## Rachelle Phipps and Ben Walls

### How to run the application


### The Program
Our application is built in Python, HTML, Javascript, and CSS in order to run the backend and frontend. The backend consists of application.py that routes the pages and messages using flask/flask-socketio while AES.py handles the encryption/decryption of the message. The frontend consists of login.html and message.html for each our of pages. 

When using the program, you will be prompts on the home screen to enter your name for chatting and shared password with another user. After entering your information, the page will be routed to the messaging page where you are able to type a message that will be sent to everyone on the page. 

If another user wants to join the room, they must enter their name and the shared password in order to enter. 


### Our choosen cipher 
We decided to choose AES CTR with a 256 bit key length to improve security. 