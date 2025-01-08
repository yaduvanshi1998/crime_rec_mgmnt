document.addEventListener("DOMContentLoaded", () => {
    const victimForm = document.getElementById("victimForm");
  
    if (victimForm) {
      victimForm.addEventListener("submit", (event) => {
        // Prevent form submission
        event.preventDefault();
  
        // Validate form fields
        const isValid = validateForm();
        if (isValid) {
          victimForm.submit(); // Submit the form if valid
        }
      });
    }
  
    function validateForm() {
      // Extract form fields
      const F_name = document.getElementById("F_name").value.trim();
      const L_name = document.getElementById("L_name").value.trim();
      const Age = document.getElementById("Age").value.trim();
      const Nationality = document.getElementById("Nationality").value.trim();
      const Address = document.getElementById("Address").value.trim();
      const Phone_no = document.getElementById("Phone_no").value.trim();
      const Court_name = document.getElementById("Court_name").value.trim();
      const Judge_name = document.getElementById("Judge_name").value.trim();
  
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
      let phonePattern = /^\+?\d{9,15}$/;
        if (!phoneInput || !phoneInput.match(phonePattern)) {
        errors.push("Phone number must be in the format '+123456789'. Up to 15 digits allowed.");
      }
  
      // Court Name validation
      if (!Court_name) {
        errorMessage += "Please select a Court.\n";
        isValid = false;
      }
  
      // Judge Name validation
      if (!Judge_name) {
        errorMessage += "Please select a Judge.\n";
        isValid = false;
      }
  
      // Show error messages
      if (!isValid) {
        alert(errorMessage);
      }
  
      return isValid;
    }
  });
  