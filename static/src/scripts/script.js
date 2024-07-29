window.dataLayer = window.dataLayer || [];
function gtag() {
  dataLayer.push(arguments);
}
gtag("js", new Date());

gtag("config", "G-11YS73K066");

document.addEventListener("DOMContentLoaded", (event) => {
  const dropZone = document.getElementById("drop-zone");
  const fileInput = document.getElementById("image");

  ["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
    dropZone.addEventListener(eventName, preventDefaults, false);
  });

  function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
  }

  ["dragenter", "dragover"].forEach((eventName) => {
    dropZone.addEventListener(eventName, highlight, false);
  });

  ["dragleave", "drop"].forEach((eventName) => {
    dropZone.addEventListener(eventName, unhighlight, false);
  });

  function highlight(e) {
    dropZone.classList.add("border-blue-500");
  }

  function unhighlight(e) {
    dropZone.classList.remove("border-blue-500");
  }

  dropZone.addEventListener("drop", handleDrop, false);

  function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;
    fileInput.files = files;

    // Optional: Display file name
    if (files[0]) {
      const fileName = files[0].name;
      dropZone.querySelector("p").textContent = `File selected: ${fileName}`;
    }
  }
});

const d = new Date();
let year = d.getFullYear();
document.getElementById("years").innerHTML = year;
