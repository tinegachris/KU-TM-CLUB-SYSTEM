document.addEventListener("DOMContentLoaded", function () {
    let menuItems = document.querySelectorAll(".side-panel ul li a");

    // Get the default tab URL from a data attribute in the HTML
    let defaultTab = document.body.getAttribute("data-default-tab") || "/leader_dash/"; 

    // Get last active tab from localStorage, or fallback to default
    let activeTab = localStorage.getItem("activeTab") || defaultTab;

    function setActiveTab(tabHref) {
        // Remove 'active' class from all menu items
        menuItems.forEach(item => item.parentElement.classList.remove("active"));

        // Find the item matching the stored URL and add 'active' class
        menuItems.forEach(item => {
            if (item.getAttribute("href") === tabHref) {
                item.parentElement.classList.add("active");
            }
        });
    }

    // Redirect to the last active tab if not already on it
    if (window.location.pathname !== new URL(activeTab, window.location.origin).pathname) {
        window.location.href = activeTab;
    } else {
        // Set the active tab if already on the correct page
        setActiveTab(activeTab);
    }

    // Handle menu item clicks
    menuItems.forEach(item => {
        item.addEventListener("click", function (event) {
            event.preventDefault();

            let selectedTab = this.getAttribute("href");

            // Store selected tab in localStorage
            localStorage.setItem("activeTab", selectedTab);

            // Redirect to the selected page
            window.location.href = selectedTab;
        });
    });
});
