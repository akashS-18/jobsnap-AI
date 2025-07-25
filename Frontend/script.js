document.getElementById("resumeForm").addEventListener("submit", async function (e) {
  e.preventDefault(); // Prevent form from refreshing

  const jobDescription = document.getElementById("jobDescription").value;
  const tone = document.getElementById("tone").value;
  const mode = document.getElementById("mode").value;

  if (!jobDescription || !tone || !mode) {
    alert("Please fill all the fields!");
    return;
  }

  // Show loading message
  document.getElementById("result").innerHTML = "⏳ Generating documents...";

  try {
    const response = await fetch("http://127.0.0.1:8000/api/generator/generate/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        prompt: jobDescription,
        tone: tone,
        mode: mode
      })
    });

    const data = await response.json();

    if (data.status === "success") {
      document.getElementById("result").innerHTML = `
        <h3>🎉 AI-Generated Documents</h3>
        <p>${data.description}</p>
      `;
    } else {
      document.getElementById("result").innerHTML = `<p style="color:red;">${data.message}</p>`;
    }
  } catch (error) {
    console.error("Error:", error);
    document.getElementById("result").innerHTML = `<p style="color:red;">Something went wrong while connecting to server.</p>`;
  }
});
