document.addEventListener('DOMContentLoaded', function() {
    fetchLogs();
});

// Fetch logs from the API
function fetchLogs() {
    fetch('/api/logs/')
        .then(response => response.json())
        .then(data => {
            const logsList = document.getElementById('logs-list');
            data.forEach(log => {
                const listItem = document.createElement('li');
                listItem.className = 'list-group-item';
                listItem.innerHTML = `
                    <div>
                        <strong>${log.timestamp}</strong> - ${log.computer_name} - ${log.event_type}
                        <button class="btn btn-link" onclick="toggleDetails(this)">Показать подробности</button>
                    </div>
                    <div class="log-details" style="display:none;">
                        <p><strong>Application:</strong> ${log.application}</p>
                        <p><strong>Window Title:</strong> ${log.window_title}</p>
                        <p><strong>Content:</strong> ${log.content}</p>
                        <p><strong>Screenshot:</strong> <a href="${log.screenshot_url}" download>Скачать</a></p>
                    </div>
                `;
                logsList.appendChild(listItem);
            });
        });
}

// Toggle log details visibility
function toggleDetails(button) {
    const details = button.parentElement.nextElementSibling;
    if (details.style.display === 'none') {
        details.style.display = '';
        button.textContent = 'Скрыть подробности';
    } else {
        details.style.display = 'none';
        button.textContent = 'Показать подробности';
    }
}