const form = document.getElementById("simplify-form");
const simplifiedText = document.getElementById("simplified-text");

form.addEventListener("submit", e => {
  e.preventDefault();
  const text = document.getElementById("text-input").value;
  fetch("/simplify", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ text: text })
  })
    .then(response => response.json())
    .then(data => {
      simplifiedText.innerHTML = `<p>Original text:</p><p>${data.text}</p><p>Simplified text:</p><p>${data.simplified_text}</p>`;
    });
});
