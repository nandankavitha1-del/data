const display = document.getElementById("n1");
function addValue(value) {
if (display.value === "Error") {
display.value = "";
}
display.value += value;
}
function calculate() {
const expression = display.value;
if (expression === "") {
    return;
}
try {
    const result = eval(expression);
    if (!isFinite(result)) {
        display.value = "Error";
    } else {
        display.value = result;
    }
} catch (error) {
    display.value = "Error";
}
}
function clearDisplay() {
display.value = "";
}