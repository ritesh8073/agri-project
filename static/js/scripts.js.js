const form = document.getElementById('input-form');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', function(event) {
    event.preventDefault();
    const latitude = document.getElementById('latitude').value;
    const longitude = document.getElementById('longitude').value;
    const nitrogen = document.getElementById('nitrogen').value;
    const phosphorus = document.getElementById('phosphorus').value;
    const potassium = document.getElementById('potassium').value;

    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            latitude: latitude,
            longitude: longitude,
            nitrogen: nitrogen,
            phosphorus: phosphorus,
            potassium: potassium
        })
    })
    .then(response => response.json())
    .then(data => {
        resultDiv.innerHTML = data.recommendation;
    })
    .catch(error => {
        resultDiv.innerHTML = 'Error: ' + error.message;
    });
});
