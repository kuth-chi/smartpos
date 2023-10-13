export function ShortNumberFormat(numbersToFormat) {
    // Format the number
    function formatNumber(number) {
      if (number >= 1e9) {
        return (number / 1e9).toFixed(2) + "B";
      } else if (number >= 1e6) {
        return (number / 1e6).toFixed(2) + "M";
      } else if (number >= 1e3) {
        return (number / 1e3).toFixed(2) + "K";
      } else {
        return number.toFixed(0);
      }
    }
  
    // Update a single number
    function updateNumber(id, number) {
      const element = document.getElementById(id);
      if (element) {
        element.innerText = formatNumber(number);
      }
    }
  
    // Update multiple numbers
    function updateNumbers(numbersToFormat) {
      numbersToFormat.forEach(({ id, number }) => {
        updateNumber(id, number);
      });
    }
  
    // Update the numbers based on the provided data
    updateNumbers(numbersToFormat);
  }
  