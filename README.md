[Link to the web site](https://motion-painter.herokuapp.com/)

# Motion Painter:

Motion Painter was designed and developed by Mate Barbir, for third milestone Code Institute Project. The idea is to have web site for all cinephiles who wants to have place to share ratings of movies but also can set up their own watching lists (bucket list). Name 'Motion Painter' is playing with phrase 'motion picture' which is another name for a movie. Design is simple, with a little but of an retro vibe. 
Users can create the profile and then add their own reviews, see other user's reviews, as well as set up their to-watch bucket list to never wonder again what to watch on a rainy Sunday.
 
## UX:
 
Target audiance for Motion Painter are cinephiles who like to:
- share their raiting of the movies they saw 
- follow up with other people's raitings
- organise their must-watch-list in a simple and efficient way.
User goals are:
- explore what people think of their most and least favourite movies
- share their own opinions
- never to wonder again what to watch on your next day off.

#### User Stories
As a user of the Motion Painter, I expect:
- US_1 Easy and intinuitve UI.
- US_2 Login system to be simple and fast.
- US_3 Option to logout.
- US_4 Option to add, edit and delete my review.
- US_5 Option to view other users reviews.
- US_6 Other users not to be able to edit & delete my reviews.
- US_7 Option to create my to-watch bucket list and edit/delete items.


## Design:
Motion Painter has a simple, a bit of an retro design. Logo and icon was done by developer Mate Barbir, by adapting the image from Favicon. 

Colour Scheme
- #ff5252 red accent-2
- #5c6bc0 indigo lighten-1
- #424242 grey darken-3

Fonts
- Fredoka One
- Ubuntu

Icons
- Font Awesome


## Features

#### Launch page 
Once you launch the site, 'Welcome' message with a short description is displayed. In the navigation bar, two choices are present: Log in or Register. 
If user has to register (once only), when clicking Register button, Register form displays with User name and Password field with specified requirement fro each (minimun 5 letters or numbers).
After choosing user name and password, when clicking Register button at the bottom of the form, user is now able to log in with his new credentials. 
If user is alrady registered, when clicking log in button, Log in form displays with User name & Password fields. 

#### After login look
After sucsesful log in, user then lands on Review page, with simple welcome message at the top. 
Navigation bar looks different after log in, it has following buttons: Review, Add review, Update bucket list, Bucket list, Log out.

#### Reviews
On Reviews page, users can see all movie reviews posted by them and other users. Only user can edit or delete their own review. 

#### Add Reviews
On Add review page, form is dispayed with follwoing fields:
- Movie genre (dropdown choice)
- Raiting (drowpdown choice)
- Movie name (text entry field)
- Your Critique (text entry field)
At the bottom, user can confirm the adding the review by clicking on Add review button.

#### Bucket List
On bucket list page, by clicking Add movie button, user can add movie they want to add on their to-watch bucket list. Once new bucket list item has been created, user can edit or delete it. 
Note, there is a known bug on this part: other users can edit & delete your bucket list items, while the intention was only for other users to see them.

#### Update Bucket List
On Update bucket list page, user can add a movie to their bucket list.

#### Log out process
When user clicks on Log Out button in navigation bar, user is immediately logged out and navigates to the Login form, with short message at the top which confirm to the user they have
been logged out sucessfully.

#### Potential future version impovements
- Bucket list: Other users should be able to view your bucket list but only you to edit or delete an item.
- Adding page with movie recommendations which can be accessed without having to register/login first. 



## Technologies Used

- IDE: VS Code
- Languages: HTML, CSS, jQuery, Python (Flask framework) 
- Verison control: Git
- Code repository: GitHub
- Database: Mongo DB
- Deployment: Heroku, Git Hub
- Design: Illustrator (Icon and logo), Materialize



## Testing User Stories

US_1 Easy and intinuitve UI. 
- When user is on any page, navigation bar with all feature buttons makes access to all features easily and guides user through the web site options.
US_2 Login/Register system to be simple and fast.
- When user clicks on the register button, register form opens with user name & password requirements specified in the entry fields.
- When user clicks on the log in button, log in form opens and after enterying valid credentials, user is logged in and navigates to the Reviews page.
US_3 Option to logout.
- When user clicks on the log out button, user is logged out and navigates to the log in form, with simple log out confimation message.
US_4 Option to add, edit and delete my review.
- There is option for user to add review, when clicking Add Review button in the navigation bar. Add review form opens, with easy to fill out filleds.
- On each review from single user, that user can see edit & delete buttons next to their review.
US_5 Option to view other users reviews.
- All reviews are visible to all users on the Review page.
US_6 Other users not to be able to edit & delete my reviews.
- Only user who added the review can delete it or edit it.
US_7 Option to create my to-watch bucket list and edit/delete items.
- Users can add memo notes on the Bucket List page, for the movies they want to watch.



#### Website is tested on three different web-browsers:

- Google Chrome:
    - Tested and working perfectly.

- Mozilla Firefox:
    - Tested and working perfectly.

- Microsoft Edge:
    - Tested and working perfectly.

#### Website is tested for fluidity, speed and responsiveness on different devices using Chrome Dev tools:

- Galaxy S5:
    - Tested and working perfectly.

- Pixel 2:
    - Tested and working perfectly.

- Pixel 2 XL:
    - Tested and working perfectly.

- iPhone 5/SE:
    - Tested and working perfectly.

- iPhone 6/7/8:
    - Tested and working perfectly.

- iPhone 6/7/8 Plus:
    - Tested and working perfectly.

- iPhone X:
    - Tested and working perfectly.

- Regular tablet size:
    - Tested and working perfectly.


#### Werkzeug debugger

- Werkzeug debugger as a part of Flask framework
    - Tested and corrected all the errors.



## Deployment

Steps for GitHub deployment:
1. In the project's repository, click on 'Settings'
2. Go to 'GitHub Pages', and under 'Score' select the branch you want to deploy. In this case, it was 'Main'.
3. Choos the folder to deploy from.
4. Click 'Save', and visit your URL (above 'Source')

[Final version of project is uploaded to Github Pages, it can be visited here - [Motion Painter](https://motion-painter.herokuapp.com/)




### Credits and Acknowledgements

- Code Institute team for teaching me necessary skills for the project, guiding me through the course and fully support anytime needed.
