import os

function sendMail(contactForm) {
    console.log("Hello")
    emailjs.send("service_0a3s8xf","template_szeqs67", {
        "to_email": "sdoc67@gmail.com",
        "website": "Axiom",
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "from_tel": contactForm.tel.value,
        "interest": contactForm.interest.value
    })
    .then(
        function(response) {
            contactForm.reset();
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}