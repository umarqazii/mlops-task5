document.getElementById("userInfoForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var formData = new FormData(this);

    fetch('/submit', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("message").innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
