document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("dataForm");
    const fromDateInput = document.getElementById("from_date");
    const toDateInput = document.getElementById("to_date");
    const fromTimeInput = document.getElementById("from_time");
    const toTimeInput = document.getElementById("to_time");
    const errorMessagesDiv = document.getElementById("errorMessages");

    // Regular expression for YYYY-MM-DD date format
    const dateRegex = /^\d{4}-\d{2}-\d{2}$/;
    // Regular expression for HH:MM time format
    const timeRegex = /^([01]\d|2[0-3]):([0-5]\d)$/;

    function validateInput() {
        let isValid = true;
        let errorMessages = [];

        // Validate "From Date"
        if (!dateRegex.test(fromDateInput.value)) {
            isValid = false;
            errorMessages.push("From Date must be in the format YYYY-MM-DD.");
        }

        // Validate "To Date"
        if (!dateRegex.test(toDateInput.value)) {
            isValid = false;
            errorMessages.push("To Date must be in the format YYYY-MM-DD.");
        }

        // Validate "From Time"
        if (!timeRegex.test(fromTimeInput.value)) {
            isValid = false;
            errorMessages.push("From Time must be in the format HH:MM.");
        }

        // Validate "To Time"
        if (!timeRegex.test(toTimeInput.value)) {
            isValid = false;
            errorMessages.push("To Time must be in the format HH:MM.");
        }

        // Check if "To Date and Time" is after "From Date and Time"
        if (isValid) {
            const fromDateTime = new Date(`${fromDateInput.value}T${fromTimeInput.value}`);
            const toDateTime = new Date(`${toDateInput.value}T${toTimeInput.value}`);
            if (toDateTime <= fromDateTime) {
                isValid = false;
                errorMessages.push("To Date and Time must be after From Date and Time.");
            }
        }

        // Display error messages
        errorMessagesDiv.innerHTML = "";
        if (!isValid) {
            errorMessages.forEach((message) => {
                const errorItem = document.createElement("p");
                errorItem.textContent = message;
                errorItem.style.color = "red";
                errorMessagesDiv.appendChild(errorItem);
            });
        }

        return isValid;
    }

    // Add event listener for form submission
    form.addEventListener("submit", function (event) {
        if (!validateInput()) {
            event.preventDefault(); // Prevent form submission if validation fails
        }
    });
});
