document.addEventListener("DOMContentLoaded", () => {
    const offenderForm = document.getElementById("dataForm");

    if (offenderForm) {
        offenderForm.addEventListener("submit", (event) => {
            // Prevent form submission
            event.preventDefault();

            // Validate form fields
            const isValid = validateForm();
            if (isValid) {
                offenderForm.submit(); // Submit the form if valid
            }
        });
    }

    function validateForm() {
        // Extract form fields
        const F_name = document.getElementById("f_name").value.trim();
        const L_name = document.getElementById("l_name").value.trim();
        const gender = document.querySelector('input[name="Gender"]:checked');
        const Age = document.getElementById("age").value.trim();
        const Nationality = document.getElementById("nationality").value.trim();
        const Address = document.getElementById("address").value.trim();
        const Phone_no = document.getElementById("phone").value.trim();
        const Offense_type = document.getElementById("offense_type").value.trim();
        const Bail_status = document.querySelector('input[name="Bail_status"]:checked');
        const Court_name = document.getElementById("court_name").value.trim();
        const Victim_phone = document.getElementById("victim_no").value.trim();
        const Judge_email = document.getElementById("judge_email").value.trim();

        let isValid = true;
        let errorMessage = "";

        // First Name validation
        if (!F_name) {
            errorMessage += "First Name is required.\n";
            isValid = false;
        }

        // Last Name validation
        if (!L_name) {
            errorMessage += "Last Name is required.\n";
            isValid = false;
        }

        // Gender validation
        if (!gender) {
            errorMessage += "Gender is required.\n";
            isValid = false;
        }

        // Age validation
        if (!Age || isNaN(Age) || Age <= 0 || Age > 120) {
            errorMessage += "Please enter a valid Age between 1 and 120.\n";
            isValid = false;
        }

        // Nationality validation
        if (!Nationality) {
            errorMessage += "Nationality is required.\n";
            isValid = false;
        }

        // Address validation
        if (!Address) {
            errorMessage += "Address is required.\n";
            isValid = false;
        }

        // Phone number validation (10-15 digits)
        const phonePattern = /^\+?\d{9,15}$/;
        if (!Phone_no.match(phonePattern)) {
            errorMessage += "Phone number must be in the format '+123456789'. Up to 15 digits allowed.\n";
            isValid = false;
        }

        // Offense Type validation
        if (!Offense_type) {
            errorMessage += "Offense Type is required.\n";
            isValid = false;
        }

        // Bail status validation
        if (!Bail_status) {
            errorMessage += "Bail Status is required.\n";
            isValid = false;
        }

        // Court Name validation
        if (!Court_name) {
            errorMessage += "Please select a Court.\n";
            isValid = false;
        }

        // Victim phone validation
        if (!Victim_phone) {
            errorMessage += "Victim phone number is required.\n";
            isValid = false;
        }

        // Judge email validation
        const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
        if (!Judge_email.match(emailPattern)) {
            errorMessage += "Please enter a valid Judge email.\n";
            isValid = false;
        }

        // Show error messages
        if (!isValid) {
            alert(errorMessage);
        }

        return isValid;
    }
});
