

# Day 2: Portfolio Build (v1) - Tailwind & Interactivity

This document tracks my progress and tasks for Day 2 of enhancing my personal portfolio.

## Achievements

* **Framework Switch:** Migrated from Bootstrap to **Tailwind CSS** (via CDN) for modern, utility-first styling.
* **Full Layout:** Built a complete Single Page Application structure including Hero, About, Skills, Projects, and Contact sections.
* **Image Handling:** Successfully implemented local image rendering using relative paths (fixing folder structure issues).
* **Custom Styling:** Created a custom "floating" scrollbar using external CSS to override browser defaults.
* **Interactivity:** Implemented JavaScript to handle form submissions (preventing page reload) and project card clicks.

## Concepts Learned / Reviewed

* **Tailwind Utility Classes:** Using classes like `p-6`, `grid-cols-3`, and `hover:scale-105` to style elements directly in HTML without writing custom CSS files.
* **Relative File Paths:** Understanding how to link assets correctly (e.g., `Images/project.jpg`) relative to the HTML file location.
* **Browser Caching:** Learned that browsers store old CSS files and how to use "Hard Refresh" (`Ctrl + F5`) to see changes.
* **Event Prevention:** Using `event.preventDefault()` in JavaScript to handle form data without reloading the page.

## Goals for Tomorrow

* Fix the mobile navigation menu (make it toggle open/close on small screens).
* Replace the "Alert" popups with actual links to my GitHub or live project demos.
* Add simple animations (like elements fading in when scrolling down).
* Learn how to deploy this website online (GitHub Pages or Netlify) so others can see it.