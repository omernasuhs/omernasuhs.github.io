document.getElementById("divorce-form").addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const inputData = Object.fromEntries(formData);

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ data: inputData }) // Verileri "data" anahtarına sararak gönderiyoruz
    })
        .then((response) => response.json())
        .then((result) => {
            const message = result.divorced ? "Divorced" : "Not divorced";
            alert("Prediction: " + message);
        })
        .catch((error) => {
            console.error("Error:", error);
            alert("An error occurred. Please try again.");
        });
});
