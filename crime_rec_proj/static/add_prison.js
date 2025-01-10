// JavaScript file: add_prison.js

// Function to validate form inputs
function validateForm() {
    // Retrieve form elements
    const prisonName = document.getElementById("prison_name").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const address = document.getElementById("address").value.trim();
    const offenderFname = document.getElementById("offender_fname").value.trim();
    const offenderLname = document.getElementById("offender_lname").value.trim();
    const errorMessages = document.getElementById("errorMessages");

    // Clear previous error messages
    errorMessages.innerHTML = "";

    let isValid = true; // Track form validity
    let errorMessageList = []; // Store error messages

    // Validate prison name
    if (prisonName === "") {
        isValid = false;
        errorMessageList.push("Prison name is required.");
    }

    // Validate phone number (basic validation)
    const phoneRegex = /^[0-9]{10,15}$/; // Matches 10-15 digits
    if (!phoneRegex.test(phone)) {
        isValid = false;
        errorMessageList.push("Telephone number must be 10-15 digits.");
    }

    // Validate address
    if (address === "") {
        isValid = false;
        errorMessageList.push("Address is required.");
    }

    // Validate offender's first name
    if (offenderFname === "") {
        isValid = false;
        errorMessageList.push("Offender's first name is required.");
    }

    // Validate offender's last name
    if (offenderLname === "") {
        isValid = false;
        errorMessageList.push("Offender's last name is required.");
    }

    // If the form is not valid, display error messages
    if (!isValid) {
        errorMessageList.forEach((msg) => {
            const errorItem = document.createElement("p");
            errorItem.className = "error-message";
            errorItem.textContent = msg;
            errorMessages.appendChild(errorItem);
        });
    }

    return isValid; // Return form validity
}

// Add event listener for form submission
document.getElementById("dataForm").addEventListener("submit", function (event) {
    if (!validateForm()) {
        event.preventDefault(); // Prevent form submission if validation fails
    }
});
