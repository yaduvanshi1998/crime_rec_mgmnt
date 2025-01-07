document.addEventListener("DOMContentLoaded", () => {
    // Reference the form and input fields
    const form = document.getElementById("dataForm");
    const fNameInput = document.getElementById("F_name");
    const lNameInput = document.getElementById("L_name");
    const designationInput = document.getElementById("Designation");
    const courtNameSelect = document.getElementById("Court_name");
    const ageInput = document.getElementById("Age");
    const addressInput = document.getElementById("Address");
    const phoneInput = document.getElementById("Phone");
    const emailInput = document.getElementById("Email");
    const errorMessagesDiv = document.getElementById("errorMessages");

    // Validate input fields before form submission
    form.addEventListener("submit", (e) => {
        // Clear previous error messages
        errorMessagesDiv.innerHTML = "";
        let errors = [];

        // Validate first name
        if (!fNameInput.value.trim()) {
            errors.push("First Name is required.");
        }

        // Validate last name
        if (!lNameInput.value.trim()) {
            errors.push("Last Name is required.");
        }

        // Validate designation
        if (!designationInput.value.trim()) {
            errors.push("Designation is required.");
        }

        // Validate court name
        if (!courtNameSelect.value) {
            errors.push("Please select a court.");
        }

        // Validate age
        const age = parseInt(ageInput.value.trim(), 10);
        if (isNaN(age) || age <= 0) {
            errors.push("Please enter a valid age.");
        }

        // Validate address
        if (!addressInput.value.trim()) {
            errors.push("Address is required.");
        }

            // Phone pattern validation
        let phonePattern = /^\+?\d{9,15}$/;
        if (!phoneInput || !phoneInput.match(phonePattern)) {
        errors.push("Phone number must be in the format '+123456789'. Up to 15 digits allowed.");
        }

        // Validate email
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email regex
        if (!emailRegex.test(emailInput.value.trim())) {
            errors.push("Please enter a valid email address.");
        }

        // If there are errors, prevent form submission and display errors
        if (errors.length > 0) {
            e.preventDefault();
            errors.forEach((error) => {
                const errorMessage = document.createElement("p");
                errorMessage.textContent = error;
                errorMessage.style.color = "red";
                errorMessagesDiv.appendChild(errorMessage);
            });
        }
    });

    // Example of adding dynamic behavior: auto-capitalize names
    [fNameInput, lNameInput].forEach((input) => {
        input.addEventListener("input", (e) => {
            e.target.value = e.target.value.charAt(0).toUpperCase() + e.target.value.slice(1);
        });
    });
});
