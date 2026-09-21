Day 2: Frameworks & Interactivity
This document records my understanding of using external frameworks, managing files, and handling user inputs.

1. HTML (File Linking & Assets)
Purpose: Today, HTML was used not just for structure, but to connect different files and assets (images, CSS, JS) together to work as a system.

Relative Paths: The method of linking files based on their location relative to the current file (e.g., Images/project.jpg instead of D:\Folder...). This ensures links work on any computer.

External Linking: Using specific tags to connect separate code files:

<link> connects CSS files.

<script> connects JavaScript files or libraries.

CDN (Content Delivery Network): A method to use a library like Tailwind by adding a web link (<script src="...">) instead of downloading files to your computer.

2. CSS (Tailwind & Advanced Styling)
Purpose: We moved from writing custom CSS to using Utility Classes (Tailwind) and learned how to customize browser elements.

Utility Classes: Pre-defined classes that style elements immediately (e.g., text-center, p-6, bg-slate-900). Instead of writing CSS rules, you just add class names to the HTML.

Pseudo-Elements: Special selectors used to style specific parts of an element that aren't in the HTML, like the scrollbar (::-webkit-scrollbar).

Object-Fit: A property (object-cover) that defines how an image should resize to fit its container.

Cover: Fills the box completely (crops if necessary).

Contain: Shows the whole image (leaves empty space if necessary).

Caching: The browser behavior of "saving" old CSS files to load faster. We learned to use Hard Refresh (Ctrl + F5) to force the browser to see new changes.

3. JavaScript (Events & Forms)
Purpose: JavaScript was used to handle user actions (clicks and form submissions) and control how the browser reacts.

Event Listeners: Code that "waits" for a specific action to happen (e.g., form.addEventListener('submit', ...)).

Prevent Default: A method (event.preventDefault()) that stops the browser's standard behavior. We used this to stop the "Contact Form" from reloading the page when clicked.

Input Values: Accessing what the user typed into a form using the .value property (e.g., document.getElementById('name').value).

Console & Alerts:

console.log(): Sends messages to the developer tools (hidden from user).

alert(): Shows a pop-up message to the user.