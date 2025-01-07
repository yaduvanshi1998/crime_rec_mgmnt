document.getElementById('dataForm').addEventListener('submit', function(e) {
    e.preventDefault();

    let errors = [];

    // Get form values
    let id = document.getElementById('Court_Id').value;
    let name = document.getElementById('Name').value.trim();
    let address = document.getElementById('Address').value.trim();
    let level = document.getElementById('Level').value.trim();
    let phone = document.getElementById('Phone').value.trim();
    let email = document.getElementById('Email').value.trim();
    
    // Id Validation: Should not be empty
    if (!id) {
        errors.push("Id is required.");
    }

    // Name Validation: Should not be empty
    if (!name) {
        errors.push("Name is required.");
    }

    // address Validation: Should not be empty
    if (!address) {
        errors.push("address is required.");
    }

    // level Validation: Should not be empty &should either high, medium or low
    if (level != high || medium || low) {
        errors.push("level should either high, medium or low");
    }

    // Email Validation: Should be a valid email format
    if (!email || !validateEmail(email)) {
        errors.push("Enter a valid email address.");
    }

    // Phone pattern validation
    let phonePattern = /^\+?\d{9,15}$/;
    if (!phone || !phone.match(phonePattern)) {
    errors.push("Phone number must be in the format '+123456789'. Up to 15 digits allowed.");
    }

    // Display Errors
    if (errors.length > 0) {
        document.getElementById('errorMessages').innerHTML = errors.join('<br>');
    } else {
        document.getElementById('errorMessages').innerHTML = '';
        alert("Form submitted successfully!");
        // You can submit the form data to the server here.
    }
});

// Simple Email Validator
function validateEmail(email) {
    const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(String(email).toLowerCase());
}
