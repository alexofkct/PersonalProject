**Socket Programming and Multithreading in Python**

This project demonstrates my understanding of socket programming and multithreading in Python, gradually building from basic socket connections to a fully functional encrypted chatroom application.

**1. Basic Socket Server**

The first script, server.py, listens for incoming TCP connections. Upon receiving a connection, it prints the IP address and port number of both the client and the server. Once the connection details are displayed, the program exits. This demonstrates a fundamental TCP handshake.
________________________________________
**2. Client-Server Communication**

In the second stage, two scripts were introduced: server.py and client.py. These scripts establish a TCP connection and allow basic message transmission. Messages are encoded into bytes before being sent. However, this version lacks true interactivity—each client must wait for the other to send a message before responding, as there is no concurrency.
________________________________________
**3. Introduction to Multithreading**

To address the lack of parallelism, multithreading was introduced in a simple script. This foundational experiment allowed me to understand how multiple tasks could run concurrently using threads, preparing for its integration into the chat system.
________________________________________
**4. Multi-Client Chatroom with Threaded Server**

Multithreading was then applied to the chatroom. The server.py script was enhanced to handle multiple clients simultaneously using threads. When a client sends a message, it is broadcast to all connected clients. To improve message traceability and ensure non-repudiation, each message is prefixed with the sender’s IP address and port number. However, to preserve privacy, it became clear that encryption was necessary—the server should not be able to read the content of user messages.
________________________________________
**5. Encrypted Chat with AES**

In the final phase, AES symmetric encryption was implemented on the client side to ensure message confidentiality. A separate script was created to generate and store the AES key and IV. Before integration, encryption and decryption were tested independently to minimize runtime errors. For now, all clients share the same key and IV, but future enhancements will include asymmetric encryption, where each client has their own private key and exchanges public keys for secure communication.
Additionally, to resolve lingering threads when a client disconnects, the client-side message handling thread was set as a daemon. This allows it to terminate cleanly when the main program ends, improving resource management and shutdown behavior.
________________________________________
**6. Authentication Integration**

In the sixth phase of the project, an authentication system was implemented. Throughout the development, abstraction was emphasized to simplify testing and reduce errors. This phase introduced user registration and login functionality, with the Python script interacting with a MySQL database using the mysql.connector module.

To align with best security practices, a dedicated database user was created with only SELECT and INSERT privileges, following the principle of least privilege. Upon successful registration, changes are committed to the database, ensuring persistence. The authentication mechanism was tested in isolation before being integrated into the main server.py script.
In this setup, server.py functions as the authentication server, while client.py represents the user. If login fails, the server immediately terminates the connection. On successful authentication, encrypted communication is established. Accordingly, encryption and decryption logic was added to server.py to support secure exchanges.

As the project evolves, the attack surface naturally increases. Future phases will focus on reinforcing security, including:

- Blocking duplicate logins from the same user credentials
- Enabling concurrent logins by different users using multithreading
- Replacing shared symmetric keys with asymmetric encryption, where each user possesses a private key and exchanges public keys securely
- Adding comprehensive logging and error handling to ensure reliability and traceability


These enhancements will solidify the project as a secure, scalable, and production-grade networked chat application.
