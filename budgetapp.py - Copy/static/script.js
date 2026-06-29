let totalBalance = 0;
let dailyBudget = 0;
let totalSpent = 0;

// Set Budget Function
function setBudget() {

    totalBalance = Number(document.getElementById("totalAmount").value);
    dailyBudget = Number(document.getElementById("dailyBudget").value);

    if (totalBalance <= 0 || dailyBudget <= 0) {
        alert("Please enter valid amounts!");
        return;
    }

    document.getElementById("balance").innerText = "₹" + totalBalance;
    document.getElementById("budget").innerText = "₹" + dailyBudget;
    document.getElementById("spent").innerText = "₹0";
    document.getElementById("remaining").innerText = "₹" + dailyBudget;
}

// Add Expense Function
function addExpense() {

    let expenseName =
        document.getElementById("expenseName").value;

    let expenseAmount =
        Number(document.getElementById("expenseAmount").value);

    if (expenseName === "" || expenseAmount <= 0) {
        alert("Please enter expense details!");
        return;
    }

    totalSpent += expenseAmount;

    let remaining = dailyBudget - totalSpent;

    // Update Summary
    document.getElementById("spent").innerText =
        "₹" + totalSpent;

    document.getElementById("remaining").innerText =
        "₹" + remaining;

    // Add Expense to History
    let li = document.createElement("li");

    li.innerHTML =
        `${expenseName} - ₹${expenseAmount}`;

    document.getElementById("expenseList")
        .appendChild(li);

    // Voice Reminder
    if (remaining <= 0) {

        speak(
            "Warning! You have reached your daily budget limit. Stop spending money."
        );

        alert(
            "Budget Limit Reached!"
        );

    } else {

        speak(
            `You have saved ${remaining} rupees today.`
        );
    }

    // Clear Inputs
    document.getElementById("expenseName").value = "";
    document.getElementById("expenseAmount").value = "";
}

// Voice Function
function speak(message) {

    let speech =
        new SpeechSynthesisUtterance(message);

    speech.lang = "en-IN";

    window.speechSynthesis.speak(speech);
}