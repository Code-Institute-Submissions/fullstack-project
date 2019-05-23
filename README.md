# Django Milestone Project

The purpose of this project is to create a website for a startup called Unicorn Attractor. 
This website allows users to register bugs and features. Bugs and features can also be upvoted. 
The community page shows graphs of bugs and features, as well as the highest-voted bugs and features.

 
## UX
 
Initial mockups were made using Balsamiq software to assist in creating the wireframe of website; a basic mockup was made of each area of the project.

- The wireframes can be located in the staticfiles folder.

User Stories
- As a user, I want to be able to see some graphs on bugs and features so that I can be well-aware of the issues
- As a user, I want to be able to see products on the website so that I can decide whether to purchase them or not.
- As a user, I want to be able to view the bugs and features so that I can edit, delete and add new feature/bug in the future.
- As a user, I want to be able to checkout the product after adding to cart so that the product will be bought.
- As the owner of this website, I want to be enable the user to checkout the products that user submitted so that payment will be received.

## Features

The project contain these features below:

**Bugs & Features:**
- Users can login to add new bug or feature so that the projects will be managed properly and ensuring the quality also.
- Users can choose to edit, delete or upvote the selected bug or feature.

**Products:**
- Users can view from a range of products available in the products page.
- Users can choose to add to cart whatever product they want to purchase and the quantity of the product.
- Users are able to search products that they want to see.
- Users are able to view cart after adding the product to cart.
- Users are able to remove selected product from the view cart page.
- Users are able to remove all products from cart.

**Checkout:**
- Users are required to have an account and log in in order to checkout the product.
- Users can checkout the product that they want to purchase by filling the form on the checkout page.

**Community:**
- Users are able to view graphs showing bugs and features as well as the highest-voted bugs and features.

### Features Left to Implement
- Another feature idea

## Technologies Used

List of tools and technologies used in this project are as follows:
- [Bootstrap](https://getbootstrap.com/docs/3.3/)
    - The project also uses some **Bootstrap** elements further simplify and maintain consistency throughout the project.
    
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [Python](https://www.python.org/)
    - The **Python** programming language was used to code the backend of the Issue Management project.

- [Django](https://www.djangoproject.com/)
    - The project uses **Django** which is a Python Web Framework used as the backend of the project and fulfilling functions such as; connecting to the SQL database, controlling routing and navigation across pages etc.

- [Stripe API](https://stripe.com/docs/api)
    - The project uses **Stripe** to take payments during the checkout feature.

- [Heroku](https://www.heroku.com/)
    - The project uses **Heroku** as the Hosting platform for this project; this was because GitHubPages only provides hosting for static projects, and not dynamic projects like this Issue Manager project.

- [Balsamiq](https://balsamiq.com/)
    - This tool was used to create the mockups of the website at the beginning of the project. 

- [ChartJS](https://www.chartjs.org/)
    - This javascript framework was used to display graphs for the project by including the cdn into the base.html


## Testing

### Python Tests

Python tests was written for the Django Project, on a app by app basis and each app was further broken down into 3 main areas of testing; *Models*, *Views* & if applicable, *Forms*.

#### Testing Models

Models are used in Django to model each Database object.
Models are also used to give a description of how each item looks like and their relationship with other models in the database (if applicable).
Model testing can be found in *test_models.py* file for each app.

#### Testing Views

Views are used to handle what users see on a page. 
They can also handle POST requests by submitting a form.
Views testing can be found in *test_views.py* file for each app.

#### Testing Forms

Forms are used to help create and update database objects.
Forms are usually submitted through a web page via a view.
Form testing can be found in *test_forms.py* file for each app.

### Coverage

Coverage.py is a tool for measuring code coverage of Python programs. 
It monitors your program, noting which parts of the code have been executed, then analyzes the source to identify code that could have been executed but was not.
Coverage measurement is typically used to gauge the effectiveness of tests. 
It can show which parts of your code are being exercised by tests, and which are not.

#### Steps Used To Generate A Coverage Report

1. Install Coverage by running the following command in a terminal window: **pip3 install coverage**
2. Then, CD into your django project directory and run the following command: **coverage run --source=app_name manage.py test** -> replace the app_name with the app you want to test.
3. After that, run the following command: **coverage report**
4. A report of your coverage will be shown in the terminal window
5. If you wish to view your coverage in html, run the following command: **coverage html** which will generate htmlconv
6. To view htmlcov, go to htmlcov folder and open the index.html file to view your coverage report.

### Different Type of Devices & Different Browsers

#### Devices

Using the debugger tools on Google Chrome via the command (ctrl+shift+i), I was able to view the website in different devices such as mobile devices, tablets, laptops and desktops.

#### Multi Browser Testing

Multi browser testing was carried out so that the website looks consistent in different browsers.
The following browser were tested in no particular order:
- Google Chrome
- Mozilla Firefox

## Deployment

This website was deployed to heroku. A git repository was also created for this project to keep track of git commits. 
I have also included a django heroku deployment cheatsheet in the staticfiles for future reference of deployment.

## Credits

### Content

### Media

- The photos used in this site were obtained from googling search images of products like shirt, belt and shoe.

### Acknowledgements

- I received inspiration for this project from this [github repository](https://github.com/Code-Institute-Submissions/full-stack-milestone).

