from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():
    # Get the plain text data from the POST request
    data = request.data.decode('utf-8')
    
    # Get the IP address of the sender
    ip_address = request.remote_addr
    
    # Print the received data and IP address to the console
    print(f"Received POST request from {ip_address}: {data}")
    
    # You can perform further processing with the received data here
    
    return 'Received POST request successfully!', 200

if __name__ == '__main__':
    app.run(debug=True)
