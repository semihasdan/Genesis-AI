let display = document.getElementById('display');
let currentInput = '0';
let operator = null;
let previousInput = null;

function appendToDisplay(value) {
    if (currentInput === '0' && value !== '.') {
        currentInput = value;
    } else {
        // Prevent multiple decimal points
        if (value === '.' && currentInput.includes('.')) {
            return;
        }
        currentInput += value;
    }
    updateDisplay();
}

function clearDisplay() {
    currentInput = '0';
    operator = null;
    previousInput = null;
    updateDisplay();
}

function deleteLast() {
    if (currentInput.length === 1) {
        currentInput = '0';
    } else {
        currentInput = currentInput.slice(0, -1);
    }
    updateDisplay();
}

function calculate() {
    if (operator && previousInput !== null) {
        let result;
        const prev = parseFloat(previousInput);
        const current = parseFloat(currentInput);
        
        switch (operator) {
            case '+':
                result = prev + current;
                break;
            case '-':
                result = prev - current;
                break;
            case '*':
                result = prev * current;
                break;
            case '/':
                if (current === 0) {
                    result = 'Error';
                } else {
                    result = prev / current;
                }
                break;
            default:
                return;
        }
        
        currentInput = result.toString();
        operator = null;
        previousInput = null;
        updateDisplay();
    }
}

function updateDisplay() {
    display.value = currentInput;
}

// Add event listeners for keyboard input
document.addEventListener('keydown', function(event) {
    if (event.key >= '0' && event.key <= '9' || event.key === '.') {
        appendToDisplay(event.key);
    } else if (event.key === '+' || event.key === '-' || event.key === '*' || event.key === '/') {
        // Handle operator input
        if (currentInput !== '0') {
            if (previousInput === null) {
                previousInput = currentInput;
                operator = event.key === '*' ? '*' : event.key;
                currentInput = '0';
            } else {
                calculate();
                operator = event.key === '*' ? '*' : event.key;
                previousInput = currentInput;
                currentInput = '0';
            }
        }
    } else if (event.key === 'Enter' || event.key === '=') {
        calculate();
    } else if (event.key === 'Escape') {
        clearDisplay();
    } else if (event.key === 'Backspace') {
        deleteLast();
    }
});