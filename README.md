**Brewbook**

Brewbook is a web application. It can be used by baristas or anyone who is interested in coffee making. 
The user can add drinks to the website, where thay can include videos, pictures and other descriptions 
about the coffee. The user can also like the drinks. I implemented this feature so that the user can 
see the liked drinks and learn making them. For example, when I was working as a barista, it was a bit
confusing to distinguish between the coffees (as an always matcha lover). So, in this web app the user 
can keep track of the drinks that they need to learn by liking them. 

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
