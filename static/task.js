async function fetchTasks() {
    const response = await fetch("/api/tasks");
    const tasks = await response.json();

    const container = document.getElementById("tasks-container");
    container.innerHTML = "";

    tasks.forEach(task => {
        const div = document.createElement("div");
        div.innerHTML = `
            <h3>Task ${task.task_id}</h3>
            <p>${task.description}</p>
            <button onclick="submitSummary(${task.task_id}, '${encodeURIComponent(task.description)}')">Summarize</button>
            <div id="summary-${task.task_id}"></div>
            <hr />
        `;
        container.appendChild(div);
    });
}

async function submitSummary(taskId, descriptionEncoded) {
    const description = decodeURIComponent(descriptionEncoded);

    const response = await fetch("/api/submit_summary", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task_id: taskId, description: description })
    });

    const result = await response.json();
    const summaryDiv = document.getElementById(`summary-${taskId}`);

    if (response.ok) {
        summaryDiv.innerHTML = `<b>Summary:</b> ${result.summary}`;
    } else {
        summaryDiv.innerHTML = `<b>Error:</b> ${result.error}`;
    }
}

window.onload = fetchTasks;
