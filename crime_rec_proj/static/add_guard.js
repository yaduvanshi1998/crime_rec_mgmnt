document.addEventListener("DOMContentLoaded", function () {
    // Reference to the form
    const form = document.getElementById("dataForm");
    const errorMessagesDiv = document.getElementById("errorMessages");

    // Helper function to display error messages
    function displayError(message) {
        errorMessagesDiv.innerHTML = `<p style="color: red;">${message}</p>`;
    }

    // Helper function to clear error messages
    function clearErrors() {
        errorMessagesDiv.innerHTML = "";
    }

    // Validate email format
    function isValidEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }

    // Phone number validation (10-15 digits)
    const phonePattern = /^\+?\d{9,15}$/;
    if (!phoneInput || !phoneInput.match(phonePattern)) {
    errors.push("Phone number must be in the format '+123456789'. Up to 15 digits allowed.");
    }

    // Validate time format (HH:MM in 24-hour format)
    function isValidTime(time) {
        const timePattern = /^([01]\d|2[0-3]):([0-5]\d)$/;
        return timePattern.test(time);
    }

    // Form submission handler
    form.addEventListener("submit", function (event) {
        clearErrors(); // Clear previous errors
        let isValid = true;

        // Retrieve form values
        const fName = document.getElementById("f_name").value.trim();
        const lName = document.getElementById("l_name").value.trim();
        const gender = document.querySelector("input[name='Gender']:checked");
        const age = document.getElementById("age").value.trim();
        const address = document.getElementById("address").value.trim();
        const phone = document.getElementById("phone").value.trim();
        const shiftStart = document.getElementById("shift_start").value.trim();
        const shiftEnd = document.getElementById("shift_end").value.trim();
        const email = document.getElementById("email").value.trim();
        const prisonName = document.getElementById("prison_name").value.trim();

        // Field validations
        if (!fName || !lName || !gender || !age || !address || !phone || !shiftStart || !shiftEnd || !email || !prisonName) {
            displayError("All fields are required. Please fill out the form completely.");
            isValid = false;
        } else if (isNaN(age) || parseInt(age) <= 0) {
            displayError("Age must be a valid positive number.");
            isValid = false;
        } else if (!isValidPhone(phone)) {
            displayError("Phone number must be exactly 10 digits.");
            isValid = false;
        } else if (!isValidEmail(email)) {
            displayError("Invalid email format.");
            isValid = false;
        } else if (!isValidTime(shiftStart)) {
            displayError("Shift start time must be in HH:MM 24-hour format.");
            isValid = false;
        } else if (!isValidTime(shiftEnd)) {
            displayError("Shift end time must be in HH:MM 24-hour format.");
            isValid = false;
        }

        // Prevent form submission if validation fails
        if (!isValid) {
            event.preventDefault();
        }
    });
});
