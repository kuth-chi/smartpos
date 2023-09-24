import { toggleDarkMode, toggleUserMenu, profileDropdownMenu, toggleFullScreen } from "./utils.js";
import {ClockTiming } from "./clocking.js";

ClockTiming();
toggleDarkMode();
toggleUserMenu();
profileDropdownMenu();


document.addEventListener('DOMContentLoaded', function () {
    // Call the toggleFullScreen function when the button is clicked
    const fullScreenToggle = document.getElementById('FullScreenToggle');
    fullScreenToggle.addEventListener('click', toggleFullScreen);
});







