const inputField = document.getElementById("inputField");
const outputField = document.getElementById("outputField");

inputField.addEventListener("input", () => {
  const text = inputField.value;
  fetch("/simplify", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({text: text})
  })
  .then(response => response.json())
  .then(data => {
    outputField.textContent = data.simplified_text;
  });
});

