document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/dashboard-data')
        .then(function (r) { return r.json(); })
        .then(renderCharts);
});

function renderCharts(data) {
    var font = { family: "'Inter', sans-serif", size: 11 };
    var gridColor = '#f1f5f9';
    var palette = ['#049fd9', '#00bceb', '#6abf4b', '#7b61ff', '#f5a623'];

    // Projects by Type
    var tLabels = Object.keys(data.type_counts);
    var tValues = Object.values(data.type_counts);

    new Chart(document.getElementById('typeChart'), {
        type: 'bar',
        data: {
            labels: tLabels,
            datasets: [{
                data: tValues,
                backgroundColor: palette.slice(0, tLabels.length),
                borderRadius: 5,
                maxBarThickness: 44
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
                y: { beginAtZero: true, ticks: { stepSize: 1, font: font }, grid: { color: gridColor } },
                x: { ticks: { font: font, maxRotation: 12 }, grid: { display: false } }
            }
        }
    });

    // Status doughnut
    var sLabels = Object.keys(data.status_counts);
    var sValues = Object.values(data.status_counts);
    var sColors = ['#6abf4b', '#1565c0', '#f5a623'];

    new Chart(document.getElementById('statusChart'), {
        type: 'doughnut',
        data: {
            labels: sLabels,
            datasets: [{ data: sValues, backgroundColor: sColors, borderWidth: 0, spacing: 2 }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '62%',
            plugins: {
                legend: { position: 'bottom', labels: { font: font, padding: 14, usePointStyle: true, pointStyleWidth: 8 } }
            }
        }
    });

    // Stage averages
    var stLabels = Object.keys(data.stage_averages);
    var stValues = Object.values(data.stage_averages);

    if (stLabels.length === 0) {
        var c = document.getElementById('stageChart').parentElement;
        c.innerHTML = '<div style="display:flex;align-items:center;justify-content:center;height:100%;color:#94a3b8;font-size:13px;">Start tracking metrics to see stage-wise analysis.</div>';
        return;
    }

    var barColors = stValues.map(function (v) {
        if (v >= 75) return '#6abf4b';
        if (v >= 40) return '#f5a623';
        return '#e2231a';
    });

    new Chart(document.getElementById('stageChart'), {
        type: 'bar',
        data: {
            labels: stLabels,
            datasets: [{ label: '% Complete', data: stValues, backgroundColor: barColors, borderRadius: 5, maxBarThickness: 28 }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
                x: { beginAtZero: true, max: 100, ticks: { font: font, callback: function (v) { return v + '%'; } }, grid: { color: gridColor } },
                y: { ticks: { font: font }, grid: { display: false } }
            }
        }
    });
}
