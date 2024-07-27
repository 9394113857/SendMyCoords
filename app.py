from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
from datetime import datetime

app = Flask(__name__)

# Configuring Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'practicesession3@gmail.com'
app.config['MAIL_PASSWORD'] = 'gpap kwxz sujc qxie'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_coordinates', methods=['POST'])
def send_coordinates():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    user_name = data.get('user_name')
    user_email = data.get('user_email')
    user_phone = data.get('user_phone', '')  # Default to empty string if not provided
    user_address = data.get('user_address', '')  # Default to empty string if not provided
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Prepare the email
    msg = Message('User GPS Coordinates and Details',
                  sender=('Coordinates Service', 'practicesession3@gmail.com'),  # Display name and email
                  recipients=['practicesession3@gmail.com', user_email])

    msg.html = f'''
        <h2>User GPS Coordinates and Details</h2>
        <table border="1" cellpadding="10" cellspacing="0">
            <tr>
                <th>S.No</th>
                <th>Field</th>
                <th>Details</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Latitude</td>
                <td>{latitude}</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Longitude</td>
                <td>{longitude}</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Name</td>
                <td>{user_name}</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Email</td>
                <td>{user_email}</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Phone</td>
                <td>{user_phone}</td>
            </tr>
            <tr>
                <td>6</td>
                <td>Address</td>
                <td>{user_address}</td>
            </tr>
            <tr>
                <td>7</td>
                <td>Timestamp</td>
                <td>{timestamp}</td>
            </tr>
        </table>
        <p>This email was sent from Flask-Mail at {timestamp}</p>
    '''
    
    # Send the email
    mail.send(msg)
    
    return jsonify({'message': 'Coordinates and details sent successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
