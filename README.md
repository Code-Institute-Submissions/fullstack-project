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

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X