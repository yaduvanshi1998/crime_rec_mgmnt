// add_crime.js

// Utility function to display an error message below the form
function displayError(message) {
    const errorMessagesDiv = document.getElementById("errorMessages");
    errorMessagesDiv.innerHTML = `<p class="error">${message}</p>`;
    errorMessagesDiv.style.color = "red";
}

// Form validation before submission
function validateForm(event) {
    event.preventDefault(); // Prevent form submission for validation
    const form = document.getElementById("dataForm");

    // Collect all input fields
    const weaponUsed = document.getElementById("weapon_used").value.trim();
    const crimeDate = document.getElementById("crime_date").value.trim();
    const crimeTime = document.getElementById("crime_time").value.trim();
    const crimeLocation = document.getElementById("crime_location").value.trim();
    const offenderFName = document.getElementById("offender_fname").value.trim();
    const offenderLName = document.getElementById("offender_lname").value.trim();
    const victimFName = document.getElementById("victim_fname").value.trim();
    const victimLName = document.getElementById("victim_lname").value.trim();

    // Check for missing or invalid input
    if (!crimeDate || !crimeTime || !crimeLocation || !offenderFName || !victimFName) {
        displayError("All required fields must be filled.");
        return;
    }

    // Optional: Validate date and time formats
    const dateRegex = /^\d{4}-\d{2}-\d{2}$/; // Example: YYYY-MM-DD
    const timeRegex = /^([01]\d|2[0-3]):([0-5]\d)$/; // Example: HH:MM in 24-hour format

    if (!dateRegex.test(crimeDate)) {
        displayError("Crime date must be in the format YYYY-MM-DD.");
        return;
    }

    if (!timeRegex.test(crimeTime)) {
        displayError("Crime time must be in the format HH:MM.");
        return;
    }

    // If all validations pass, submit the form
    form.submit();
}

// Attach validation to the form's submit event
document.getElementById("dataForm").addEventListener("submit", validateForm);
