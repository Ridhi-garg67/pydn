from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():
    # Get the plain text data from the POST request
    data = request.data.decode('utf-8')
    
    # Print the received data to the console
    print("Received POST request:")
    print(data)
    
    # You can perform further processing with the received data here
    
    return 'Received POST request successfully!', 200

if __name__ == '__main__':
    app.run(debug=True)
