const input = document.getElementById("imageinput");
const preview = document.getElementById("preview");
const resultsList = document.getElementById("results");

input.addEventListener("change", () => {
    const file = input.files[0];
    preview.src = URL.createObjectURL(file);
});

async function uploadimage() {
    const file = input.files[0];
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch(
        "http://127.0.0.1:8000/predict",
        {method: "POST",
        body: formData
        });

    const data = await response.json();
    console.log("hello world");

    resultsList.innerHTML = "";
    data.detections.forEach(det => {
    const li = document.createElement("li");
    li.textContent = det.label;
    resultsList.appendChild(li)
    });
}