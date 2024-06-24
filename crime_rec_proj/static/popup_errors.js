// Function to display an alert message
function showAlert(message) {
    alert(message = "Invalid Credentials");
}

// Check if there's an error message from the server
window.onload = function() {
    if (window.errorMessage) {
        showAlert(window.errorMessage);
    }
}

// Function to remove required attributes when Sign Up is clicked
function handleSignupClick() {
    document.getElementById('Username').removeAttribute('required');
    document.getElementById('Password').removeAttribute('required');
}