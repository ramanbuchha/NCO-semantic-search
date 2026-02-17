async function search() {
  const query = document.getElementById("query").value;
  const resultsDiv = document.getElementById("results");

  resultsDiv.innerHTML = "<p>Searching...</p>";

  try {
    const response = await fetch(`http://127.0.0.1:9000/semantic_search?query=${query}&k=10`);

    if (!response.ok) {
      throw new Error("Backend error");
    }

    const data = await response.json();

    resultsDiv.innerHTML = "";

    data.forEach(item => {
      const card = document.createElement("div");
      card.className = "result-card";

      card.innerHTML = `
        <h3>${item.title}</h3>
        <p><b>NCO 2015 Code:</b> ${item.nco_2015_code}</p>
        <p><b>Similarity Distance:</b> ${item.distance}</p>
      `;

      resultsDiv.appendChild(card);
    });

  } catch (err) {
    resultsDiv.innerHTML = `<p style="color:red;">Error: Could not connect to backend</p>`;
    console.error(err);
  }
}
