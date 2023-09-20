
document.addEventListener('DOMContentLoaded', function () {
  const userMenuButton = document.getElementById('user-menu-button');;
  const collapsibleDiv = document.getElementById('navbar-user');

  userMenuButton.addEventListener('click', function () {
    // Toggle the 'hidden' class to show/hide the dropdown 
    collapsibleDiv.classList.toggle('hidden');
    // Update the 'aria-expanded' attribute for accessibility
    // const expanded = collapsibleDiv.classList.contains('hidden') ? 'false' : 'true';
    userMenuButton.setAttribute('aria-expanded', expanded);
  });
});

document.addEventListener('DOMContentLoaded', function () {
    const userDropdownButton = document.getElementById('dropdown-button');
    const userDropdown = document.getElementById('user-dropdown');
    
    userDropdownButton.addEventListener('click', function () {
      // Toggle the 'hidden' class to show/hide the dropdown
      userDropdown.classList.toggle('hidden');
      
  
      // Update the 'aria-expanded' attribute for accessibility
      const expanded = collapsibleDiv.classList.contains('hidden') ? 'false' : 'true';
      userDropdownButton.setAttribute('aria-expanded', expanded);
    });
  });


 // Get references to the button and the collapsible div



  // Dark mode
  document.addEventListener('DOMContentLoaded', function () {
    const themeToggle = document.getElementById('theme-toggle');
    const darkIcon = document.getElementById('theme-toggle-light-icon');
    const lightIcon = document.getElementById('theme-toggle-dark-icon');

    // Check user's theme preference
    const isDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;

    // Retrieve the user's preference from localStorage
    const systemPreference = localStorage.getItem('themePreference');

    // Set the initial theme mode based on the user's preference or the system's preference
    if (systemPreference === 'dark') {
        darkIcon.classList.remove('hidden');
        lightIcon.classList.add('hidden');
        // You can also toggle your application's dark mode here
        document.documentElement.classList.add('dark');
    } else if (systemPreference === 'light') {
        darkIcon.classList.add('hidden');
        lightIcon.classList.remove('hidden');
        // You can also toggle your application's light mode here
        document.documentElement.classList.remove('dark');
    } else if (isDarkMode) {
        darkIcon.classList.remove('hidden');
        lightIcon.classList.add('hidden');
        // You can also toggle your application's dark mode here
        document.documentElement.classList.add('dark');

    } else {
        darkIcon.classList.add('hidden');
        lightIcon.classList.remove('hidden');
        // Toggle your application's light mode here
        document.documentElement.classList.remove('dark');
    }

    // Toggle theme manually on button click
    themeToggle.addEventListener('click', function () {
        if (darkIcon.classList.contains('hidden')) {
            darkIcon.classList.remove('hidden');
            lightIcon.classList.add('hidden');
            // Toggle to dark mode
            document.documentElement.classList.add('dark');
            // You can save the user's preference in local storage here
            // Save the user's preference in localStorage
            localStorage.setItem('themePreference', 'dark');
        } else {
            darkIcon.classList.add('hidden');
            lightIcon.classList.remove('hidden');
            // Toggle to light mode
            document.documentElement.classList.remove('dark');
            // You can save the user's preference in local storage here
            localStorage.setItem('themePreference', 'light');
        }
    });
});


