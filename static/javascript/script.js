/* 
I am listening for the "DOMContentLoaded" event because when I tried clicking my search-icons in the browser, 
I encountered an error stating ':5000/favicon.ico:1 Failed to load resource: the server responded with a status of -
404 (NOT FOUND)'. I realized that in this case, "favicon" refers to the click event and icon. By using the "DOMContentLoaded" -
event listener, I can ensure that the JavaScript code executes only after the initial HTML document has been fully loaded - 
and parsed by the browser. This resolves the issue with the search-icons, allowing the search bar to appear from the end -
of the screen as intended when clicked.
*/
document.addEventListener("DOMContentLoaded", () => {
    const searchIcon = document.querySelector('.search-icons')
    const searchForm = document.querySelector('.search-form')
    searchIcon.addEventListener('click', () => {
        searchForm.classList.add('active');
    });
})