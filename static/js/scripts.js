let latitude = null;
let longitude = null;

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(setCoordinates, showError);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function setCoordinates(position) {
    latitude = position.coords.latitude;
    longitude = position.coords.longitude;
    document.getElementById('status').innerText = 'Coordinates obtained. Please fill in your details.';
    document.getElementById('submitButton').disabled = false;  // Enable the submit button
}

function sendForm(event) {
    event.preventDefault();

    if (latitude === null || longitude === null) {
        alert('Please obtain your coordinates first.');
        return;
    }

    const userForm = document.getElementById('userForm');
    const formData = new FormData(userForm);

    const data = {
        latitude: latitude,
        longitude: longitude,
        user_name: formData.get('user_name'),
        user_email: formData.get('user_email'),
        user_phone: formData.get('user_phone') || 'Not provided',
        user_address: formData.get('user_address') || 'Not provided'
    };

    fetch('/send_coordinates', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        document.getElementById('status').innerText = 'Coordinates and details sent successfully!';
        document.getElementById('submitButton').disabled = true;  // Disable the submit button after submission
    })
    .catch(error => console.error('Error:', error));
}

function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            alert("User denied the request for Geolocation.");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Location information is unavailable.");
            break;
        case error.TIMEOUT:
            alert("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
            alert("An unknown error occurred.");
            break;
    }
}
