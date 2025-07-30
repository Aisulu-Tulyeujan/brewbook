**Brewbook**

Brewbook is a comprehensive web application designed for baristas, coffee enthusiasts, and anyone 
interested in learning more about coffee making. The app allows users to create and share detailed 
drink recipes, including images, instructional videos (both uploaded and YouTube), and rich 
descriptions. Additionally, users can “like” drinks to keep track of their favorites or the ones 
they want to learn more about.

**Distinctiveness and Complexity**

Unlike many projects that simply display static content or focus on frontend styling, this project 
emphasizes interactive backend functionality, integrating user-specific data persistence using Django 
models. While CRUD-based apps are common, I extended the traditional flow by implementing asynchronous 
features like AJAX-based like/unlike buttons, modal-based video previews, and real-time UI updates 
without page reloads.

At first glance, the app may appear simple, but beneath the surface, it requires handling multiple moving 
parts: file uploads (videos), dynamic ingredient entry, user authentication, conditional rendering of 
data (liked vs. unliked drinks), and database relationships (many-to-many). Building modals with embedded 
iframes and managing their lifecycle was a surprisingly difficult part of the UX. Also, coordinating 
frontend logic with backend endpoints using vanilla JavaScript instead of frameworks like React or Vue 
demanded precision and thoughtful structuring.

**Installation**:
1. Clone the repository: https://github.com/Aisulu-Tulyeujan/brewbook
2. Navigate to the folder: cd brewbook
3. Install dependencies:
4. Run the development server: python3 manage.py runserver
