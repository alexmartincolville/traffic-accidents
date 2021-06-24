
const ageBandsConfig = {
    type: 'pie',
    data: {
        datasets: [{
            data: data['bands'],
            label: 'Amount of Accidents',
            backgroundColor: getColors(data['bands'].length),
        }],
        labels: labels['bands']
    },
    options: {
        title: {
            display: true,
            text: 'Accidents by Age Band'
        },
        legend: {
            position: 'bottom'
        }
    }
};

const vehicleAgeConfig = {
    type: 'bar',
    data: {
        datasets: [{
            data: data['vehicle'],
            label: 'Amount of Accidents',
            backgroundColor: getColors(data['vehicle'].length),
        }],
        labels: labels['vehicle']
    },
    options: {
        title: {
            display: true,
            text: 'Accidents by Age of Vehicle'
        },
        legend: {
            position: 'bottom'
        }
    }
};


const dailyAmountConfig = {
    type: 'bar',
    data: {
        datasets: [{
            data: data['amount'],
            label: 'Amount of Accidents',
            backgroundColor: getColors(data['amount'].length),
        }],
        labels: labels['amount']
    },
    options: {
        title: {
            display: true,
            text: 'Accidents by Day of the Week'
        },
        legend: {
            position: 'bottom'
        }
    }
};

const severityConfig = {
    type: 'bar',
    data: {
        datasets: [{
            data: data['severity'],
            label: 'Amount of Accidents',
            backgroundColor: getColors(data['severity'].length),
        }],
        labels: labels['severity']
    },
    options: {
        title: {
            display: true,
            text: 'Accidents by Severity'
        },
        legend: {
            position: 'bottom'
        }
    }
};

function getColors(length) {
    var colors = [];
    while (colors.length < length) {
        do {
            var color = Math.floor((Math.random() * 1000000) + 1);
        } while (colors.indexOf(color) >= 0);
        colors.push("#" + ("000000" + color.toString(16)).slice(-6));
    }
    return colors;
};

window.onload = function () {

    var ageBandChart = document.getElementById('age-band-chart').getContext('2d');
    window.myPie = new Chart(ageBandChart, ageBandsConfig);

    var vehicleAgeChart = document.getElementById('vehicle-age-chart').getContext('2d');
    window.myPie = new Chart(vehicleAgeChart, vehicleAgeConfig);

    var dailyAmountChart = document.getElementById('daily-amount-chart').getContext('2d');
    window.myPie = new Chart(dailyAmountChart, dailyAmountConfig);

    var accidentSeveritChart = document.getElementById('accident-severity-chart').getContext('2d');
    window.myPie = new Chart(accidentSeveritChart, severityConfig);
};

