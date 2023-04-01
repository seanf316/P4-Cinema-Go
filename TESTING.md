# **Cinema | Go Testing**

## **Testing Overview**

A wide range of testing was carried out during development by myself and also by my peers.

## **Contents**

1. [Testing Overview](#testing-overview)
2. [Automated Testing](#automated-testing)
    - [Unit Testing](#unit-testing)
    - [Site Coverage Report](#site-coverage-report)
3. [Manual Testing](#manual-testing)
    - [User Story Testing](#user-story-testing)
    - [Negative Testing](#negative-testing)
    - [Javascript Testing](#javascript-testing)
4. [Validators](#validators)
    - [CI Python Linter](#ci-python-linter)
    - [JSHint](#jshint)
    - [W3C CSS Validator](#w3c-css-validator)
    - [W3C Markup Validator](#w3c-markup-validator)
    - [Lighthouse](#lighthouse)
    - [Lighthouse Errors](#lighthouse-errors)
    - [Wave Accessibility Tests](#wave-accessibility-tests)
5. [Responsiveness](#responsiveness)
6. [Bugs & Fixes](#bugs--fixes)
7. [Unresolved Bugs/Issues](#unresolved-bugsissues)

## **Automated Testing**

### **Unit Testing**

Unit tests were created to test the functionality of the apps. These can be found in the tests.py files in the respective apps.

#### **Home**

![Home](/docs/unit_testing/test_home.webp)

#### **Movie**

**Views**

![Movie Views](/docs/unit_testing/test_movie_views.webp)

**Models**

![Movie Models](/docs/unit_testing/test_movie_models.webp)

#### **Profiles**

**Views**

![Profiles Views](/docs/unit_testing/test_profiles_views.webp)

**Models**

![Profiles Models](/docs/unit_testing/test_profiles_models.webp)

**Forms**

![Profiles Forms](/docs/unit_testing/test_profiles_forms.webp)

#### **Review**

**Views**

![Review Views](/docs/unit_testing/test_review_views.webp)

**Models**

![Review Models](/docs/unit_testing/test_review_models.webp)

**Forms**

![Review Forms](/docs/unit_testing/test_review_forms.webp)

[Back to top &uarr;](#contents)

### **Site Coverage Report**

Through my testing, I was able to get a total of 95% coverage across the site. The remaining 5% will be covered through manual testing.

![Coverage 1](/docs/unit_testing/coverage1.webp)
![Coverage 2](/docs/unit_testing/coverage2.webp)
![Coverage 3](/docs/unit_testing/coverage3.webp)

[Back to top &uarr;](#contents)

## **Manual Testing**

### **User Story Testing**

Some features of the site are restricted to registered users such as viewing Movie details, Reviewing movies, Commenting on Reviews, and editing a Profile. The functional tests take this into account. There is also one Epic below as this included the Homepage.

#### **Homepage**

`
As a Developer, I can design a nice aesthetically pleasing Homepage, so that the user has an enjoyable experience when navigating site
`

The Homepage view is adjusted for registered Users, non-registered Users will see some information about the site along with the features offered to registered Users along with a "Sign Up" button. Registered Users will be met with a thank you message and some movie-related links to get them started on the site like "Search", "Trending" & "Top Rated".

**User Not Registered**

![Homepage 1](/docs/testing_screenshots/homepagenotreg.webp)
![Homepage 1 Test](/docs/testing_screenshots/homepagesign.webp)

**User Registered**

![Homepage 2](/docs/testing_screenshots/homepagereg.webp)
![Homepage 2 Test](/docs/testing_screenshots/homepagereglinks.webp)

The Home page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

#### **Navbar**

`
As a User I want to see a clear way of navigating the site so that I can find the information relative to my needs
`

**Acceptance Criteria**
- Create a nice Navbar with relevant links to parts of the site
- Create a Hamburger menu for mobiles and smaller Tablets

Functional testing was carried out on the Navbar and all links go to their relevant pages as expected. Navbar is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

**User Not Registered**

![Navbar 1](/docs/testing_screenshots/navbar.webp)

**User Registered**

![Navbar 2](/docs/testing_screenshots/navbar1.webp)

#### **Footer**

`
As a User I want to be able to get in touch with the Developer so that I can enquire about issues/suggestions I may have
`

**Acceptance Criteria**
- Responsive Footer created for multiple Devices
- Social Links implemented
- Copyright implemented

Functional testing was carried out on the Footer and all links go to the relevant social media site as expected. All links open in a separate tab. The Footer is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

![Footer 1](/docs/testing_screenshots/footer.webp)

[Back to top &uarr;](#contents)

#### **Movie Search**

`
As a User I want to have a section where I can search for a Movie so that I can easily find the Movie I want to review
`

**Acceptance Criteria**
- User has a search input that would get their Query from the API

Functional testing was carried out on the Search page, link in Navbar was working as expected. I have tested entering a query i.e. "Batman" in the search input and confirmed redirection to the Search Results page.

`
As a Developer I can create the Movie Search Template so that the User has an nice experience on the site
`

**Acceptance Criteria**
- Create a responsive template that allows the user to quickly search for a specific Movie

The Search page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

![Search 1](/docs/testing_screenshots/search.webp)

#### **Movie Search Results**

`
As a Developer I can create the Movie Search Results template so that the User has a clear display of the results from their search
`

**Acceptance Criteria**
- Create a responsive template that allows the user to quickly display the results from their search

The Search Results page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

**User Not Registered**

![Search Results 1](/docs/testing_screenshots/searchresults1.webp)

**User Registered**

![Search Results 2](/docs/testing_screenshots/searchresults2.webp)

#### **Movie Categories**

`
As a Developer I can build a page to display the Top Rated Movies so that the User can easily get access to the Top Rated Movies of all time
`

**Acceptance Criteria**
- When the User selects Top Rated from the Movies dropdown they will be met with a page that displays the Top Rated Movies

The Top Rated page link can be accessed in the Movie dropdown list in the Navbar. The link has been tested and is working as expected. The Top Rated page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

**User Not Registered**

![Top Rated 1](/docs/testing_screenshots/toprated1.webp)

**User Registered**

![Top Rated 2](/docs/testing_screenshots/toprated2.webp)

`
As a Developer I can build a page to display Trending Movies so that the User can see the latest Trending Movies
`

**Acceptance Criteria**
- When the User selects Trending from the Movies dropdown they will be met with a page that displays the Trending Movies

The Trending page link can be accessed in the Movie dropdown list in the Navbar. The link has been tested and is working as expected. The Trending page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

**User Not Registered**

![Trending 1](/docs/testing_screenshots/trending1.webp)

**User Registered**

![Trending 2](/docs/testing_screenshots/trending2.webp)

#### **Movie Details**

`
As a User I want to view the Movie details from my search so that I can read the synopsis and check reviews
`

**Acceptance Criteria**
- User's can select the relevant Movie from their search and be sent to a new page containing the movies information

`
As a Developer I can build a page to display the Movie Details for the users selected Movie so that they have a clear overview of the Movie
`

**Acceptance Criteria**
- When User selects the Movie from the search query they will land at a page that displays that Movie Detail


The Movie details page was originally planned to work with just the Search Results page but during development, I decided to add some category pages Trending & Top Rated. When a user selects View Movie from the Search Results or clicks on a Movie Poster in the category pages they will be redirected to the Movie Details page. This was covered in the functional link testing above. The Movie Details page will display all the information for the Movie selected by User, the page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

Originally I had planned to display the reviews for the Movie under the details but decided as a Design choice to move all reviews to a specific Reviews page.

Further functional testing was carried out on the Movie Details links/buttons. Movie Details page is only accessible to registered users. 

![Movie Details](/docs/testing_screenshots/moviedetails.webp)

[Back to top &uarr;](#contents)

#### **Watchlist**

`
As a User I would like the ability to add Movies to a watchlist so that I can have a list of movies that I can refer to when looking for something to watch
`

**Acceptance Criteria**
- User can search for movies and add them to a list for watching later

Clicking the "Add to Watchlist +" or "Remove from Watchlist -" button on the Movie Details page has been tested and works as expected, User watchlist can also be managed on the Profile page under the My Watchlist section.

![Add to Watchlist](/docs/testing_screenshots/addtowatchlist.webp)
![Remove from Watchlist](/docs/testing_screenshots/removewatchlist.webp)
![Profile Watchlist](/docs/testing_screenshots/profilewatchlist.webp)

[Back to top &uarr;](#contents)

#### **Reviewing/Commenting & Reviews**

`
As a User I want the ability to review Movies so that I can share my thoughts of the Movie with family and friends
`

**Acceptance Criteria**
- Registered Users would have the ability to review Movies they have selected to review
- Users that are not registered will be alerted to sign-up to Review

`
As a Developer I can create a nice display for the User to review so that they have an enjoyable experience reviewing Movies on the site
`

**Acceptance Criteria**
- When registered User clicks the Review button they will be brought to the review page

Review functionality is only available to registered users. Users not registered will not be able to access the Movie Details page so they wont have access to the Review button. When a registered User clicks the Review button in the Movie Details page they will be redirected to the Review form page. When the User has entered details in all required fields and clicks Update they will be redirected to the Reviews page and their Review will be rendered. The Users Profile page will show the Reviewed Movies name and a Manage link under the My Reviews section.

The Review Form page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

![Review Form](/docs/testing_screenshots/reviewsiteform.webp)
![Review Rendered](/docs/testing_screenshots/reviewrendered.webp)
![Profile Reviews](/docs/testing_screenshots/profilereviews.webp)

The Movie Details "Review" button for the Movie reviewed will now read as "Reviewed".

![Review Button](/docs/testing_screenshots/reviewed.webp)

`
As a User I would like the ability to edit my review so that I can fix any spelling or format issues
`

**Acceptance Criteria**
- When user creates the review they have the ability to edit it again

Registered Users can edit their reviews via the Edit Review button on the Review card located on the Reviews page or by clicking the Manage link beside the Movie name under the My Reviews section of the Profile page. Users will be redirected to the Review form to edit their review.

![Edit Review](/docs/testing_screenshots/editreview.webp)
![Edit Review Profile](/docs/testing_screenshots/profilemanage.webp)

`
As a User I would like the ability to delete my review so that I can manage my reviews and in the case of accidentally selecting the wrong Movie and reviewing it
`

**Acceptance Criteria**
- User has access to a Delete view where they can delete the selected Review

Registered Users can delete their reviews via the Edit Review button on the Review card located on the Reviews page or by clicking the Manage link beside the Movie name under the My Reviews section of the Profile page. Users will be redirected to the Review form to delete their review. User can click the Delete button on the Review form, a modal will pop up asking the User if they are sure about deleting their Review. Once User confirms deletion the review and any comments related to the review will be deleted, and the review will be removed from the Reviews page & the My Reviews section on the Profile page. 

The Movie Details "Review" button for the Movie reviewed will now read as "Review" again.

![Edit Review](/docs/testing_screenshots/editreview.webp)
![Edit Review Profile](/docs/testing_screenshots/profilemanage.webp)
![Delete Review](/docs/testing_screenshots/reviewdelete.webp)
![Delete Modal](/docs/testing_screenshots/deletemodal.webp)
![Review Testing](/docs/testing_screenshots/reviewform.webp)

`
As a User I would like the ability to comment on Reviews so that I can participate in conversations with fellow reviewer's
`

**Acceptance Criteria**
- Registered Users would have the ability to comment on Movie reviews from fellow reviewer's

`
As a Developer I can create a section on the Review page for comments so that User's can comment on reviews
`

**Acceptance Criteria**
- Registered Users can comment on Reviews
- Comment form created for User to add comment

Comment functionality is only available to registered Users. Users can Comment on reviews by clicking the "Comment" button on the review card shown on the Review page. They will be redirected to the Comment form page where once they fill out the required fields and click the "Update" button their comment will be then rendered within the review card on the Reviews page. Along with the comment text, the following will be rendered - commenter name, date/time of comment, an Edit icon, and a Delete icon.

The Comment Form page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

![Comment Button](/docs/testing_screenshots/comment.webp)
![Comment Form](/docs/testing_screenshots/commentform.webp)
![Comments](/docs/testing_screenshots/comments.webp)
![Comment Form Testing](/docs/testing_screenshots/commentformpage.webp)

Comments can be edited by clicking the Edit icon under the comment text. When clicked User will be redirected to the Comment form page to update their comment. Once updated the comment text will be updated on the Review card.

![Edit Comment](/docs/testing_screenshots/editcomment.webp)
![Updated Comment](/docs/testing_screenshots/commentedit.webp)

Comments can be deleted by clicking the Delete icon under the comment text. When clicked the comment will be deleted from the Review.

![Delete Comment](/docs/testing_screenshots/deletecomment.webp)
![Comment Removed](/docs/testing_screenshots/commentremoved.webp)

`
As a User I would like the ability to view all movie reviews so that I can see what my fellow reviewers think of other movies
`

**Acceptance Criteria**
- User selects the Reviews link in Nav and all Movie Reviews are displayed to user

`
As a Developer I can create an All Reviews page so that the User can have a nice display containing all reviews
`

**Acceptance Criteria**
- User selects the Reviews link in Nav and all Movie Reviews are displayed to user

Registered Users have access to the Reviews page, here they can view all reviews created by registered Users. The Reviews link in Navbar was tested and works as expected. The Reviews page renders each Review in a card, each card contains the reviewer's Profile image, the review date/time, their username, the Movie title, review text, and 2 buttons "View Movie" & "Comment". A third button will render if the review belongs to the logged-in User - "Edit Review".

The Reviews page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

Functional testing was carried out on the Reviews page.

![Reviews Page Testing](/docs/testing_screenshots/reviewspage.webp)

[Back to top &uarr;](#contents)

#### **Profile**

`
As a User I would like access to my Profile so that I can upload an image or alter my details where needed
`

**Acceptance Criteria**
- User can access Profile and can Create/Read/Update/Delete their personal details

`
As a Developer I can create an aesthetically pleasing display of the User's Profile so that the experience of viewing their Profile is a pleasant one
`

**Acceptance Criteria**
- When User clicks on their Profile a nice responsive display is shown


Only registered Users have access to the Profile page as the Profile is automatically created when a User signs up to the site. On the Profile page, the User can view the information that they signed up with and add extra information about themselves if they wish to. They will also be able to manage their Watchlist and Reviews list from the Profile page.

The Profile page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

![Profile Page](/docs/testing_screenshots/profilepage.webp)
![Profile Page Test](/docs/testing_screenshots/profiletest.webp)

`
As a Developer I can create an edit Profile template so that the User has a nice display for when they want to update their Profile
`

**Acceptance Criteria**
- User selects Edit on Profile template and Edit Profile template is rendered.

On the Profile page, the User will find an "Edit Profile" button under all their information, if clicked it will redirect the User to the Edit Profile form page. Here the User will be able to update information like first name, surname, about, favourite movie, favourite actor, favourite director and also will have the ability to upload their own Profile image. Once User is happy with the information entered and the fields are valid they can click the "Update" button and they will be redirected back to the Profile page where new information will be rendered.

The Edit Profile form page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

![Edit Profile](/docs/testing_screenshots/profilebutton.webp)
![Profile Page](/docs/testing_screenshots/profileedited.webp)

The User can delete their Profile/User account by clicking the "Delete" button on the Edit Profile form page. When the User clicks the "Delete" button a modal will pop up asking the User if they are sure they want to delete and advising all information related to their account will be deleted, if they confirm deletion Profile/User account will be deleted and User will be returned to the Homepage for unregistered Users.

![Delete Profile Button](/docs/testing_screenshots/profiledeletebutton.webp)
![Delete Profile](/docs/testing_screenshots/profiledelete.webp)
![Edit Profile Page Test](/docs/testing_screenshots/editprofiletest.webp)

[Back to top &uarr;](#contents)

#### **Authentication**

`
As a User I want to Sign Up/Login and Logout so that I can see what features are available to registered users like reviewing/commenting
`

**Acceptance Criteria**
- Users are able to Sign Up
- Registered Users are able to Login/Logout

`
As a Developer I can add functionality to verify email and reset password so that the user has better security over their email being used and can reset password if they forget it
`

**Acceptance Criteria**
- Users are able verify their email when signing up
- Registered Users are able to reset password if they forgot it

Allauth is used to manage the authentication of the site, Users can Sign up, Login and Logout. Email verification and Password rest functionality were also added.

The Sign Up page can be accessed via the link in Navbar, the Sign Up link on the Login page, or lastly via the Sign Up button on the Homepage for unregistered Users. All links have been tested and work as expected.

For Sign Up the user will fill out the required fields on the Sign Up form page and once valid they click the "Sign Up" button. They will be redirected to the Verify Email Address page where the User will be advised that an email is sent to them. Once the User receives the email they can click the confirmation link. This will bring the User to the Confirm E-mail Address page on the site, the User will click the "Confirm" button and be redirected to the Login page.

The Sign Up page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

![Sign Up](/docs/testing_screenshots/signup.webp)
![Email Verify](/docs/testing_screenshots/emailverify.webp)
![Email](/docs/testing_screenshots/email.webp)
![Confirm Email](/docs/testing_screenshots/confirmemail.webp)
![Sign Up Testing](/docs/testing_screenshots/signuptest.webp)

The Login page can be accessed via the link in the Navbar, the link has been tested and works as expected.

For Login, the User will enter either their Username or Email Address and their password in the required fields, once the fields are valid they can click the "Login" button to gain access to site features restricted to registered Users. If User has forgotten their password they can click the "Forgot Password" button. They will then be redirected to the Password Reset page where they will need to enter the email address they registered with before clicking the "Reset My Password" button. They will now be redirected to the Password Reset email sent page where a message will display advising an email has been sent to the User. When the email is received the User can click on the link to reset the password which will then direct them to the Change Password page on the site. Once the User enters a new password in the fields required they will be redirected to the Change Password confirmed page, here they will be able to click the "Home" button to be redirected to the site Homepage for unregistered Users. They can proceed to log in again with new details.

The Login page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

![Login](/docs/testing_screenshots/loginpage.webp)
![Password Reset](/docs/testing_screenshots/passwordreset.webp)
![Password Email Sent](/docs/testing_screenshots/passwordemailsent.webp)
![Password Email](/docs/testing_screenshots/passwordemail.webp)
![Change Password](/docs/testing_screenshots/changepassword.webp)
![Password Change Confirmed](/docs/testing_screenshots/passwordconfirmed.webp)
![Login Test](/docs/testing_screenshots/logintest.webp)

The Logout page can be accessed via the link in the Navbar, the link has been tested and works as expected.

For Logout the User can click the "Sign Out" button on the Logout page, they will then be redirected to the Homepage for unregistered Users.

The Logout page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

![Logout](/docs/testing_screenshots/logout.webp)
![Logout Test](/docs/testing_screenshots/logouttest.webp)

[Back to top &uarr;](#contents)

#### **Error Pages**

`
As a Developer I can implement a 403 error page to redirect unauthorised users so that I can secure my views
`

**Acceptance Criteria**
- 403 page created and Error message explained to User

A custom 403 error page & 403_csrf error page were created to handle 403 status errors. Pages were tested by changing URLs to access other Users' information and delete their Profiles, 403 status page displayed as expected. I also removed the csrf token from a form to test the 403_csrf page and 403_csrf status page displayed as expected.

`
As a Developer I can implement a 404 error page so that I can alert users when they have accessed a page that doesn't exist
`

**Acceptance Criteria**
- 404 page created and Error message explained to User

A custom 404 error page was created to handle 404 status errors. To test I tried to access a page that does not exist, and this worked, 404 status page displayed as expected.

`
As a Developer I can implement a 500 error page so that I can alert users when an internal server error occurs
`

**Acceptance Criteria**
- 500 page created and Error message explained to User

A custom 500 error page was created to handle 500 status errors. To test I would repeatedly and quickly hit the delete icon for a comment by doing this too fast and not allowing the time for the comment to be deleted the error 500 page was rendered.


All error pages are fully responsive, I do not have any current screenshots of the errors on Mobile/Tablet but you can view the Desktop screenshots in the Features section of the [README.md](README.md)

[Back to top &uarr;](#contents)

### **Negative Testing**

Negative testing was done on the Edit/Delete functionality for Reviews, Comments & Profile. Sign Up username field min length was tested also.

![Testing 7](/docs/testing/test7.webp)

[Back to top &uarr;](#contents)

### **Javascript Testing**

**base.html Javascript**

The JS script in the base.html handles the alert messages for the site. There is a timeout of 2 seconds set for the alert messages to close. This has been manually tested and works as expected. See below example:

![Alert Gif](/docs/gifs/alert.gif)

**Review.js**

The review.js is setup with a mouse leave event on the review cards, when user has moved the mouse outside the review card the text will smoothly scroll back to the top. There is a timeout of 3 seconds applied for this to happen. This has been manually tested and works as expected. See below example:

![Review Gif](/docs/gifs/review.gif)

**Modal.js**

The modal.js was taken from Bootstrap but has been altered slightly to to remove the iframe scource for the trailer once the modal is hidden as well as managing the closing/hiding of the modal. This was done to avoid the trailer continuing to play in the background once modal was closed. This has been manually tested and works as expected. See below example, please note I could not show the sound playing in the gif but you will be able to see the sound icon in the tab:

![Trailer Gif](/docs/gifs/trailer.gif)

[Back to top &uarr;](#contents)

## **Validators**

### **CI Python Linter**

The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python code used throughout the project. The results are outlined in below:

![PEP8 Results](/docs/validation/pep_results.webp)

[Back to top &uarr;](#contents)

### **JSHint**

[JSHint](https://jshint.com/) was used to validate the Javascript code used in the project. Only one undefined variable is showing "bootstrap" - this was taken from the walkthrough and altered to fix a console error. No other issues to report.

![JSHint Results](/docs/validation/jshint.webp)

[Back to top &uarr;](#contents)

### **W3C CSS Validator**

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the site's CSS code.

![W3C CSS Validator](/docs/validation/css_results.webp)

[Back to top &uarr;](#contents)

### **W3C Markup Validator**

All pages were run through the [W3C Markup Validator](https://validator.w3.org/nu/). Initially, there were some errors due to missing closing tags, image height values, and Richtextfield inputs. All of these issues were corrected and all pages passed validation.

Due to the Django templating language code used in the HTML files, these could not be copied and pasted into the validator and due to the secured views, pages with login required or a secured view cannot be validated by direct URI. To test the validation on the files, open the page to validate, right click and view page source. Paste the raw HTML code into the validator as this will be only the HTML-rendered code.

![W3C Markup Validator](/docs/validation/html_check.webp)

[Back to top &uarr;](#contents)

### **Lighthouse**

<details><summary>Desktop Results</summary>

Home(User not signed in)

![Lighthouse Desktop Score](/docs/validation/lighthouse/nosignin_desktop.webp)

Home(User signed in)

![Lighthouse Desktop Score](/docs/validation/lighthouse/signedin_desktop.webp)

Trending Movies

![Lighthouse Desktop Score](/docs/validation/lighthouse/trending_desktop.webp)

Top Rated Movies

![Lighthouse Desktop Score](/docs/validation/lighthouse/toprated_desktop.webp)

Movie Search

![Lighthouse Desktop Score](/docs/validation/lighthouse/search_desktop.webp)

Movie Search Results

![Lighthouse Desktop Score](/docs/validation/lighthouse/searchresults_desktop.webp)

Movie Details

![Lighthouse Desktop Score](/docs/validation/lighthouse/moviedetails_desktop.webp)

All Reviews

![Lighthouse Desktop Score](/docs/validation/lighthouse/allreviews_desktop.webp)

Review

![Lighthouse Desktop Score](/docs/validation/lighthouse/review_desktop.webp)

Comment

![Lighthouse Desktop Score](/docs/validation/lighthouse/comment_desktop.webp)

Profile

![Lighthouse Desktop Score](/docs/validation/lighthouse/profile_desktop.webp)

Sign Up

![Lighthouse Desktop Score](/docs/validation/lighthouse/signup_desktop.webp)

Login

![Lighthouse Desktop Score](/docs/validation/lighthouse/login_desktop.webp)

Logout

![Lighthouse Desktop Score](/docs/validation/lighthouse/logout_desktop.webp)

</details>

<details><summary>Mobile Results</summary>

Home(User not signed in)

![Lighthouse Mobile Score](/docs/validation/lighthouse/nosignin_mobile.webp)

Home(User signed in)

![Lighthouse Mobile Score](/docs/validation/lighthouse/signedin_mobile.webp)

Trending Movies

![Lighthouse Mobile Score](/docs/validation/lighthouse/trending_mobile.webp)

Top Rated Movies

![Lighthouse Mobile Score](/docs/validation/lighthouse/toprated_mobile.webp)

Movie Search

![Lighthouse Mobile Score](/docs/validation/lighthouse/search_mobile.webp)

Movie Search Results

![Lighthouse Mobile Score](/docs/validation/lighthouse/searchresults_mobile.webp)

Movie Details

![Lighthouse Mobile Score](/docs/validation/lighthouse/moviedetails_mobile.webp)

All Reviews

![Lighthouse Mobile Score](/docs/validation/lighthouse/allreviews_mobile.webp)

Review

![Lighthouse Mobile Score](/docs/validation/lighthouse/review_mobile.webp)

Comment

![Lighthouse Mobile Score](/docs/validation/lighthouse/comment_mobile.webp)

Profile

![Lighthouse Mobile Score](/docs/validation/lighthouse/profile_mobile.webp)

Sign Up

![Lighthouse Mobile Score](/docs/validation/lighthouse/signup_mobile.webp)

Login

![Lighthouse Mobile Score](/docs/validation/lighthouse/login_mobile.webp)

Logout

![Lighthouse Mobile Score](/docs/validation/lighthouse/logout_mobile.webp)

</details>

[Back to top &uarr;](#contents)

### **Lighthouse Errors**

The errors encountered in the various reports are outlined below:

- "Eliminate render-blocking resources" - this was pointing towards bootstrap.min.css throughout, I am unaware of how to fix it at this time
- "Displays images with incorrect aspect ratio", "Properly size images", "Serve images in next-gen formats" - I have tried resizing how the images are displayed but due to the fact they are being retrieved from the API, there is not much I can do here.

I have tested the site on various devices and networks (3g, 4g & WIFI) and the above is not affecting the site, load times are good and no issues/delays reported by test users.

There is one console error due to the embedded Youtube video that cannot be fixed at this time, it refers to "Ensure CORS response header values are valid". The error only occurs when the user clicks play on the video. I have researched this previously and the issue appears to be between Google and Youtube so I am unable to fix this error. Please note this error does not seem to affect the performance of the site.

![Lighthouse Console Error](/docs/validation/lighthouse/trailer_console.webp)

[Back to top &uarr;](#contents)

### **Wave Accessibility Tests**

Every page of the site was passed through the [Wave Evaluation Tool](https://wave.webaim.org/) via the Chrome extension. Only 1 page returned errors which was the Reviews Page. It showed 91 contrast errors due to no fallback contrast being in place if the image does not populate, to resolve I added a background colour to the Review cards and all contrast errors were cleared.

![Wave](/docs/validation/wave.webp)

[Back to top &uarr;](#contents)

## **Responsiveness**

All pages were tested to ensure responsiveness on screen sizes from 320px and upwards. The site was tested on multiple browsers and devices as outlined below.

| **Browser Tested** | **Actual Result** | **Pass/Fail** |
|--------------------|-------------------|---------------|
| Chrome             | As Expected       | Pass          |
| Firefox            | As Expected       | Pass          |
| Edge               | As Expected       | Pass          |
| Mac OS Safari      | As Expected       | Pass          |

| **Device Tested** | **Actual Result** | **Pass/Fail** |
|-------------------|-------------------|---------------|
| Mac Air M2 | As Expected       | Pass          |
| HP Elite Laptop | As Expected       | Pass          |
| HP 23 Monitor | As Expected       | Pass          |
| Samsung Note 10+  | As Expected       | Pass          |
| Samsung Note 20   | As Expected       | Pass          |
| Samsung S21+      | As Expected       | Pass          |
| Samsung Tab S7+   | As Expected       | Pass          |
| iPhone 13 Pro Max | As Expected       | Pass          |
| iPhone 11         | As Expected       | Pass          |
| iPad Pro 12 inch  | As Expected       | Pass          |
| One Plus 8T  | As Expected       | Pass          |
| Xiaomi Redmi Note 11 | As Expected       | Pass          |

[Back to top &uarr;](#contents)

## **Bugs & Fixes**

| **Bug**                                                     | **Issue**                                                                                                                                                                                           | **Resolution**                                                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Current Profile image URL not showing in Edit Profile form  | When a user wants to change their Profile picture the current profile link would not display in the crispy form                                                                                     | Upon researching this issue I found that there was an issue between the Bootstrap version I was running and Crispy Bootstrap 5. To resolve the issue I changed the Crispy Template pack to bootstrap 4 and removed Crispy Bootstrap 5. Users can now view the image URL in the Edit Profile form.                                   |
| Summernote not displaying toolbar items                     | Summernote was installed and settings were applied in settings.py, unfortunately, the buttons were not displaying or working correctly when used with Crispy forms.                                 | After much testing, I changed the editor to Richtextfield editor, and the fields/toolbars are displaying and working as expected.                                                                                                                                                                                                   |
| Richtextfield max length issue                              | Richtextfield was not reading the max length applied in the model field                                                                                                                             | To resolve I added the MaxLength Validator to the model field                                                                                                                                                                                                                                                                       |
| Richtextfield counts the background HTML tags as characters | I noticed while doing negative testing that I had set the max characters of the Review field to 2500 characters but the max I could enter was only 2493 - This was due to the background p tags ( ) | To resolve I raised the max length in the review model field to 2507 characters. Now users can enter 2500 characters although if styling is used this will cause more issues. This is a Richtextfield limitation at this time. Impact on the user would be very rare considering the max length allowed should be more than enough. |
| Search Result cards of different sizes                      | I noticed while building the Search Results page that the cards being displayed were different sizes when API results did not contain a background image.                                           | To resolve I created a fallback background image and scaled it to match the image size received from the TMDB API.                                                                                                                                                                                                                  |
| Heroku builds failing                                       | I was receiving emails from time to time saying the app build failed from Heroku - after researching it seemed to be related to a version of Cloudinary                                             | To resolve this I just manually deployed the app when required.                                                                                                                                                                                                                                                                     |

[Back to top &uarr;](#contents)

## **Unresolved Bugs/Issues**

The console error related to the Youtube embedded video is the main unresolved bug for the site, I have mentioned the error to CI staff on calls and the consensus was it was out of my control and to make sure it was documented in README.md

The other bug that I have encountered is that a User can enter just white spaces in the Richtextfield inputs and submit. This issue only occurs with Richtextfields, I have tried adding clean functions but nothing works. To resolve this issue you could remove all the Richtextfields and Richtext widgets and place a standard Textfield. After speaking with my Mentor and the Users that tested the site the consensus was to keep the editor that they would miss the functionality and that 99.9% of people reviewing a Movie would not enter blank spaces. I have decided to leave the editors in place based on the feedback received.

[Return to README.md](README.md)
