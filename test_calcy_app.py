import unittest
import tkinter as tk
from calculator_app import CalculatorApp  # Import your CalculatorApp class

class TestCalculatorApp(unittest.TestCase):

    def setUp(self):
        """Set up the Tkinter Calculator App for testing."""
        self.root = tk.Tk()
        self.app = CalculatorApp(self.root)  # Initialize the Calculator app

    def test_addition(self):
        """Test the addition functionality."""
        self._simulate_input("5+5=")
        result = self.app.result_var.get()  # Get the result displayed in the entry
        self.assertEqual(result, "10", "Addition result should be 10")

    def test_subtraction(self):
        """Test the subtraction functionality."""
        self._simulate_input("10-4=")
        result = self.app.result_var.get()
        self.assertEqual(result, "6", "Subtraction result should be 6")

    def test_multiplication(self):
        """Test the multiplication functionality."""
        self._simulate_input("3*3=")
        result = self.app.result_var.get()
        self.assertEqual(result, "9", "Multiplication result should be 9")

    def test_division(self):
        """Test the division functionality."""
        self._simulate_input("8/2=")
        result = self.app.result_var.get()
        self.assertEqual(result, "4", "Division result should be 4")

    def test_clear(self):
        """Test the 'C' button (clear functionality)."""
        self._simulate_input("5+5=C")
        result = self.app.result_var.get()
        self.assertEqual(result, "", "Clear should reset the display.")

    def test_invalid_expression(self):
        """Test an invalid expression."""
        self._simulate_input("5++5=")
        result = self.app.result_var.get()
        self.assertEqual(result, "", "Invalid expression should result in empty display.")

    def _simulate_input(self, input_sequence):
        """
        Simulate button clicks for the given input sequence.

        Args:
            input_sequence (str): The sequence of button presses to simulate.
        """
        for char in input_sequence:
            button = self._get_button_by_label(char)
            if button:
                button.invoke()  # Simulate a button click

    def _get_button_by_label(self, label):
        """
        Find a button widget in the app by its displayed label.

        Args:
            label (str): The label of the button to find.

        Returns:
            Button: The Tkinter Button widget if found, otherwise None.
        """
        for child in self.app.root.winfo_children():
            if isinstance(child, tk.Button) and child.cget("text") == label:
                return child
        return None

    def tearDown(self):
        """Destroy the Tkinter app after each test."""
        self.root.destroy()

# Run the tests when executed in IDLE
if __name__ == "__main__":
    unittest.main(exit=False)
