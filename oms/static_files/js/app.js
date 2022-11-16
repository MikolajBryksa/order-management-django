const elements = document.getElementsByClassName('status');
for (let i = 0; i < elements.length; i++) {

    if (elements[i].textContent.includes('Valuation') ||
        elements[i].textContent.includes('Wycena')) {
        elements[i].style.color = "#F9629F";

    } else if (elements[i].textContent.includes('Urgent') ||
        elements[i].textContent.includes('Pilne')) {
        elements[i].style.color = "#ED2939";

    } else if (elements[i].textContent.includes('Drawing') ||
        elements[i].textContent.includes('Rysowane')) {
        elements[i].style.color = "#ff8c00";

    } else if (elements[i].textContent.includes('Incomplete') ||
        elements[i].textContent.includes('Niekompletne')) {
        elements[i].style.color = "gray";

    } else if (elements[i].textContent.includes('Designed') ||
        elements[i].textContent.includes('Zaprojektowane')) {
        elements[i].style.color = "green";

    } else if (elements[i].textContent.includes('Evaluation') ||
        elements[i].textContent.includes('Oceniane')) {
        elements[i].style.color = "#ff8c00";

    } else if (elements[i].textContent.includes('Improvement') ||
        elements[i].textContent.includes('Poprawka')) {
        elements[i].style.color = "#007FFF";

    } else if (elements[i].textContent.includes('Accepted') ||
        elements[i].textContent.includes('Zaakceptowane')) {
        elements[i].style.color = "green";

    } else if (elements[i].textContent.includes('Production') ||
        elements[i].textContent.includes('Produkcja')) {
        elements[i].style.color = "#ff8c00";

    } else if (elements[i].textContent.includes('Packed') ||
        elements[i].textContent.includes('Zapakowane')) {
        elements[i].style.color = "green";

    } else {
        elements[i].style.color = "black"
    }
}