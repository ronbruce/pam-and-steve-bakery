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
        cartItemsContainer.classList.remove('active');
    });

    const cartIcons = document.querySelector('.cart-icons')
    const cartItemsContainer = document.querySelector('.cart-items-container')

    cartIcons.addEventListener('click', () => {
        cartItemsContainer.classList.add('active');
        searchForm.classList.remove('active');
    });
    
    // This function will run once the entire page (including all scripts, images, etc.) has loaded
    window.onload = function() {
        // Get the height of the header element
        var headerHeight = document.querySelector('.header').offsetHeight;
        // Set the top margin of the home section to be the same as the height of the header
        // This aligns the top of the home section with the bottom of the header
        document.querySelector('.home').style.marginTop = headerHeight + 'px';
    }
    
})