
async function loadDashboard() {
    const status = document.getElementById("appStatus");
    const version = document.getElementById("appVersion");
    const commit = document.getElementById("commitSha");
    const environment = document.getElementById("appEnvironment");
    const navStatus = document.getElementById("navStatus");

    try {
        const [healthResponse, infoResponse] = await Promise.all([
            fetch("/health"),
            fetch("/api/info")
        ]);

        if (!healthResponse.ok || !infoResponse.ok) {
            throw new Error("Application unavailable");
        }

        const health = await healthResponse.json();
        const info = await infoResponse.json();

        const healthy = health.status === "healthy";

        status.textContent = healthy ? "Operational" : "Degraded";
        navStatus.textContent = healthy ? "All systems operational" : "Service degraded";

        version.textContent = info.version;
        commit.textContent = info.commit;
        environment.textContent =
            window.location.hostname === "localhost" ||
            window.location.hostname === "127.0.0.1"
                ? "Local"
                : "Cloud";

        document.querySelectorAll(".status-dot").forEach(dot => {
            dot.style.background = healthy ? "#239b70" : "#d97757";
        });

    } catch (error) {
        status.textContent = "Unavailable";
        navStatus.textContent = "Service unavailable";

        document.querySelectorAll(".status-dot").forEach(dot => {
            dot.style.background = "#d97757";
        });

        console.error("Dashboard error:", error);
    }
}

document.getElementById("refreshBtn").addEventListener("click", loadDashboard);

loadDashboard();
