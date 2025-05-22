// backend/static/js/task.js
document.getElementById("task-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    const input = document.getElementById("task-input").value;

    const response = await fetch("/submit_task", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task: input })
    });

    const data = await response.json();
   document.getElementById("result-area").innerHTML = `
    <div class="alert alert-success">
        <strong>AI Summary:</strong><br/> ${data.result}<br/>
        <hr>
        <strong>Transaction Hash:</strong> ${data.tx_hash}
    </div>
`;

});
