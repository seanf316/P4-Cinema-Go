# **Cinema | Go Testing**

## **Testing Overview**

A wide range of testing was carried out during development by myself and also by my peers. 

## **Contents**

1. [Testing Overview](#testing-overview)
1. [Unit Testing](#unit-testing)
1. [Manual Testing](#manual-testing)
1. [Validators](#validators)

## **Unit Testing**

Unit tests were created to test functionality of the apps. These can be found in the tests.py files in the respective apps.

### **Home**

![Home](/docs/unit_testing/test_home.webp)

### **Movie**

**Views**

![Movie Views](/docs/unit_testing/test_movie_views.webp)

**Models**

![Movie Models](/docs/unit_testing/test_movie_models.webp)

### **Profiles**

**Views**

![Profiles Views](/docs/unit_testing/test_profiles_views.webp)

**Models**

![Profiles Models](/docs/unit_testing/test_profiles_models.webp)

**Forms**

![Profiles Forms](/docs/unit_testing/test_profiles_forms.webp)

### **Review**

**Views**

![Review Views](/docs/unit_testing/test_review_views.webp)

**Models**

![Review Models](/docs/unit_testing/test_review_models.webp)

**Forms**

![Review Forms](/docs/unit_testing/test_review_forms.webp)

### **Site Coverage Report**

Through my testing I was able to get a total of 95% coverage across the site. The remaining 5% will be covered through the manual testing.

![Coverage 1](/docs/unit_testing/coverage1.webp)
![Coverage 2](/docs/unit_testing/coverage2.webp)
![Coverage 3](/docs/unit_testing/coverage3.webp)

[Back to top &uarr;](#contents)

## **Manual Testing**

### **Functional Testing**

**User Not Registered**

| **Navbar**              |                                                                                                      |                                                                                                                                                                                              |               |
|-------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| **Test Case Id**        | **Action**                                                                                           | **Expected Result**                                                                                                                                                                          | **Pass/Fail** |
| 1                       | Clicking Sign Up in navbar                                                                           | User redirected to Sign Up page                                                                                                                                                              | Pass          |
| 2                       | Clicking Login in navbar                                                                             | User redirected to Login page                                                                                                                                                                | Pass          |
| 3                       | Selecting Search from Movies dropdown                                                                | User redirected to Search page                                                                                                                                                               | Pass          |
| 4                       | Selecting Trending from Movies dropdown                                                              | User redirected to Trending page                                                                                                                                                             | Pass          |
| 5                       | Selecting Top Rated from Movies dropdown                                                             | User redirected to Top Rated page                                                                                                                                                            | Pass          |
| 6                       | Clicking Home in navbar                                                                              | User redirected to Home page                                                                                                                                                                 | Pass          |
| 7                       | Clicking Cinema\|Go logo in navbar                                                                   | User redirected to Home page                                                                                                                                                                 | Pass          |
|                         |                                                                                                      |                                                                                                                                                                                              |               |
| **Home Page**           |                                                                                                      |                                                                                                                                                                                              |               |
| **Test Case Id**        | **Action**                                                                                           | **Expected Result**                                                                                                                                                                          | **Pass/Fail** |
| 1                       | User clicks Sign Up button                                                                           | User redirected to Sign Up page                                                                                                                                                              | Pass          |
|                         |                                                                                                      |                                                                                                                                                                                              |               |
| **Search Page**         |                                                                                                      |                                                                                                                                                                                              |               |
| **Test Case Id**        | **Action**                                                                                           | **Expected Result**                                                                                                                                                                          | **Pass/Fail** |
| 1                       | User enters query i.e. "Batman"                                                                      | User redirected to Search Results page                                                                                                                                                       | Pass          |
|                         |                                                                                                      |                                                                                                                                                                                              |               |
| **Trending Page**       |                                                                                                      |                                                                                                                                                                                              |               |
| **Test Case Id**        | **Action**                                                                                           | **Expected Result**                                                                                                                                                                          | **Pass/Fail** |
| 1                       | User selects one of the Movies from the results shown                                                | User redirected to Login page                                                                                                                                                                | Pass          |
|                         |                                                                                                      |                                                                                                                                                                                              |               |
| **Top Rated Page**      |                                                                                                      |                                                                                                                                                                                              |               |
| **Test Case Id**        | **Action**                                                                                           | **Expected Result**                                                                                                                                                                          | **Pass/Fail** |
| 1                       | User selects one of the Movies from the results shown                                                | User redirected to Login page                                                                                                                                                                | Pass          |
|                         |                                                                                                      |                                                                                                                                                                                              |               |
| **Search Results Page** |                                                                                                      |                                                                                                                                                                                              |               |
| **Test Case Id**        | **Action**                                                                                           | **Expected Result**                                                                                                                                                                          | **Pass/Fail** |
| 1                       | User selects one of the Movies from the results shown                                                | User redirected to Login page                                                                                                                                                                | Pass          |
|                         |                                                                                                      |                                                                                                                                                                                              |               |
| **Footer**              |                                                                                                      |                                                                                                                                                                                              |               |
| **Test Case Id**        | **Action**                                                                                           | **Expected Result**                                                                                                                                                                          | **Pass/Fail** |
| 1                       | Clicking Facebook icon                                                                               | User redirected to Facebook in a new tab                                                                                                                                                     | Pass          |
| 2                       | Clicking Twitter icon                                                                                | User redirected toTwitter in a new tab                                                                                                                                                       | Pass          |
| 3                       | Clicking Instagram icon                                                                              | User redirected to Instagram in a new tab                                                                                                                                                    | Pass          |
| 4                       | Clicking Github icon                                                                                 | User redirected to Cinema\|Go Github repository  in a new tab                                                                                                                                | Pass          |

**User Registered**

| **Navbar**              |                                                                                                      |                                                                                                                                                                                                       |               |
|-------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| **Test Case Id**        | **Action**                                                                                           | **Expected Result**                                                                                                                                                                                   | **Pass/Fail** |
| 1                       | Clicking Logout in navbar                                                                            | User redirected to Logout page                                                                                                                                                                        | Pass          |
| 2                       | Selecting Search from Movies dropdown                                                                | User redirected to Search page                                                                                                                                                                        | Pass          |
| 3                       | Selecting Trending from Movies dropdown                                                              | User redirected to Trending page                                                                                                                                                                      | Pass          |
| 4                       | Selecting Top Rated from Movies dropdown                                                             | User redirected to Top Rated page                                                                                                                                                                     | Pass          |
| 5                       | Clicking Home in navbar                                                                              | User redirected to Home page                                                                                                                                                                          | Pass          |
| 6                       | Clicking Cinema\|Go logo in navbar                                                                   | User redirected to Home page                                                                                                                                                                          | Pass          |
| 7                       | Clicking Reviews in navbar                                                                           | User redirected to Reviews page                                                                                                                                                                       | Pass          |
| 8                       | Clicking Profile in navbar                                                                           | User redirected to Profile page                                                                                                                                                                       | Pass          |
|                         |                                                                                                      |                                                                                                                                                                                                       |               |
| **Home Page**           |                                                                                                      |                                                                                                                                                                                                       |               |
| **Test Case Id**        | **Action**                                                                                           | **Expected Result**                                                                                                                                                                                   | **Pass/Fail** |
| 1                       | User clicks Search button                                                                            | User redirected to Search page                                                                                                                                                                        | Pass          |
| 2                       | User clicks Trending button                                                                          | User redirected to Trending page                                                                                                                                                                      | Pass          |
| 3                       | User clicks Top Rated button                                                                         | User redirected to Top Rated page                                                                                                                                                                     | Pass          |
|                         |                                                                                                      |                                                                                                                                                                                                       |               |
| **Search Page**         |                                                                                                      |                                                                                                                                                                                                       |               |
| **Test Case Id**        | **Action**                                                                                           | **Expected Result**                                                                                                                                                                                   | **Pass/Fail** |
| 1                       | User enters query i.e. "Batman"                                                                      | User redirected to Search Results page                                                                                                                                                                | Pass          |
|                         |                                                                                                      |                                                                                                                                                                                                       |               |
| **Trending Page**       |                                                                                                      |                                                                                                                                                                                                       |               |
| **Test Case Id**        | **Action**                                                                                           | **Expected Result**                                                                                                                                                                                   | **Pass/Fail** |
| 1                       | User selects one of the Movies from the results shown                                                | User redirected to Movie Details page                                                                                                                                                                 | Pass          |
|                         |                                                                                                      |                                                                                                                                                                                                       |               |
| **Top Rated Page**      |                                                                                                      |                                                                                                                                                                                                       |               |
| **Test Case Id**        | **Action**                                                                                           | **Expected Result**                                                                                                                                                                                   | **Pass/Fail** |
| 1                       | User selects one of the Movies from the results shown                                                | User redirected to Movie Details page                                                                                                                                                                 | Pass          |
|                         |                                                                                                      |                                                                                                                                                                                                       |               |
| **Search Results Page** |                                                                                                      |                                                                                                                                                                                                       |               |
| **Test Case Id**        | **Action**                                                                                           | **Expected Result**                                                                                                                                                                                   | **Pass/Fail** |
| 1                       | User selects one of the Movies from the results shown                                                | User redirected to Movie Details page                                                                                                                                                                 | Pass          |
|                         |                                                                                                      |                                                                                                                                                                                                       |               |
| **Movie Details Page**  |                                                                                                      |                                                                                                                                                                                                       |               |
| **Test Case Id**        | **Action**                                                                                           | **Expected Result**                                                                                                                                                                                   | **Pass/Fail** |
| 1                       | User clicks Trailer button                                                                           | Trailer modal opens and user can view Trailer                                                                                                                                                         | Pass          |
| 2                       | User clicks IMDb                                                                                     | User redirected to IMDb in a new tab                                                                                                                                                                  | Pass          |
| 3                       | User clicks Add to Watchlist + button                                                                | Button text changed to Remove from Watchlist -                                                                                                                                                        | Pass          |
| 4                       | User clicks Review button                                                                            | User redirected to Review form page                                                                                                                                                                   | Pass          |
| 5                       | User has reviewed Movie                                                                              | Review button text changed to Reviewed                                                                                                                                                                | Pass          |
| **Reviews Page**     |                                                                                                      |                                                                                                                                       |               |
| **Test Case Id**     | **Action**                                                                                           | **Expected Result**                                                                                                                   | **Pass/Fail** |
| 1                    | Review author clicks Edit Review button                                                              | User redirected to Review form page                                                                                                   | Pass          |
| 2                    | User clicks View Movie button                                                                        | User redirected to Movie Details page                                                                                                 | Pass          |
| 3                    | User clicks Comment button                                                                           | User redirected to Comment form page                                                                                                  | Pass          |
| 4                    | User clicks review Movie title                                                                       | User redirected to Movie Details page                                                                                                 | Pass          |
| 5                    | User clicks on Review author username                                                                | User redirected to Profile page of Review author                                                                                      | Pass          |
| 6                    | User clicks on Review author profile image                                                           | User redirected to Profile page of Review author                                                                                      | Pass          |
| 7                    | User has created a comment on Review (Review currently has no comments)                              | "Comments" title appears under review                                                                                                 | Pass          |
|                      |                                                                                                      | Users comment is rendered                                                                                                             | Pass          |
|                      |                                                                                                      | Edit & Delete icons are rendered only for Comment author                                                                              | Pass          |
|                      |                                                                                                      | Date/Time of comment is rendered                                                                                                      | Pass          |
|                      |                                                                                                      | Comment author username is rendered                                                                                                   | Pass          |
| 8                    | User adds another comment                                                                            | Users comment is rendered under earlier comments                                                                                      | Pass          |
|                      |                                                                                                      | Edit & Delete icons are rendered                                                                                                      | Pass          |
|                      |                                                                                                      | Date/Time of comment is rendered                                                                                                      | Pass          |
|                      |                                                                                                      | Comment author username is rendered                                                                                                   | Pass          |
| 9                    | Comment author clicks Edit button                                                                    | User redirected to Comment form page                                                                                                  | Pass          |
| 10                   | Comment author clicks Delete button                                                                  | Comment is deletedMessage shown advising comment is deleted                                                                           | Pass          |
| 11                   | User clicks on Comment author username                                                               | User redirected to Profile page of Comment author                                                                                     | Pass          |
|                      |                                                                                                      |                                                                                                                                       |               |
| **Review Form Page** |                                                                                                      |                                                                                                                                       |               |
| **Test Case Id**     | **Action**                                                                                           | **Expected Result**                                                                                                                   | **Pass/Fail** |
| 1                    | User enters text in the Review field and value between 1-10 in Rating field and clicks Update button | User redirected to Reviews page and review is rendered                                                                                | Pass          |
| 2                    | User clicks Delete button on an empty Review form                                                    | Message shown advising "You are not authorized to delete this review"                                                                 | Pass          |
| 3                    | Review author clicks Delete button on their existing review                                          | Delete modal rendered and Review author asked if they are sure about deleting                                                         | Pass          |
| 4                    | Review author confirms review deletion                                                               | Review author(User) redirected to Reviews Page                                                                                        | Pass          |
|                      |                                                                                                      | Message shown advising Review has been deleted                                                                                        | Pass          |
|                      |                                                                                                      | Reviews page no longer renders that review or comments related to Review                                                              | Pass          |
| **Comments Form Page** |                                                                                 |                                                                                                            |               |
| **Test Case Id**       | **Action**                                                                      | **Expected Result**                                                                                        | **Pass/Fail** |
| 1                      | User enters text in the Comment field and clicks Update button                  | User redirected to Reviews page and comment is rendered under Review                                       | Pass          |
|                        |                                                                                 |                                                                                                            |               |
| **Profile Page**       |                                                                                 |                                                                                                            |               |
| **Test Case Id**       | **Action**                                                                      | **Expected Result**                                                                                        | **Pass/Fail** |
| 1                      | Profile owner has not added any Movies to watchlist                             | Text under My Watchlist shows "Watchlist is empty!"                                                        | Pass          |
| 2                      | Profile owner has not reviewed any Movies                                       | Text under My Reviews shows "Review list is empty!"                                                        | Pass          |
| 3                      | Profile owner has added Movies to watchlist                                     | Movie name and Remove link appear under My Watchlist                                                       | Pass          |
| 4                      | Profile owner has not reviewed any Movies                                       | Movie name and Manage link appear under My Watchlist                                                       | Pass          |
| 5                      | Profile owner clicks Movie name link under My Watchlist                         | User redirected to Movie Details page                                                                      | Pass          |
| 6                      | Profile owner clicks Remove link beside Movie name under My Watchlist           | Movie is removed from Profile owners watchlist                                                             | Pass          |
|                        |                                                                                 | Movie name & Remove link no longer appears under My Watchlist                                              | Pass          |
| 7                      | Profile owner clicks Movie name link under My Reviews                           | User redirected to Movie Details page                                                                      | Pass          |
| 8                      | Profile owner clicks Manage link beside Movie name under My Reviews             | User redirected to Review form page                                                                        | Pass          |
| 9                      | If Profile/Review onwer deletes review                                          | Movie is removed from Profile owners My Reviews list                                                       | Pass          |
|                        |                                                                                 | Movie name & Manage link no longer appears under My Reviews list                                           | Pass          |
| 10                     | Profile owner can see and click the Edit Profile button                         | Profile owner redirected to Edit Profile form                                                              | Pass          |
| 11                     | User viewing another users Profile                                              | Edit Profile button not renderedRemove text not rendered under My Watchlist                                | Pass          |
|                        |                                                                                 | Manage button not shown under My Reviews                                                                   | Pass          |
| 12                     | User viewing another users Profile clicks Movie name link under My Watchlist    | User redirected to Movie Details page                                                                      | Pass          |
| 13                     | User viewing another users Profile clicks Movie name link under My Reviews      | User redirected to Movie Details page                                                                      | Pass          |
|                        |                                                                                 |                                                                                                            |               |
| **Edit Profile Page**  |                                                                                 |                                                                                                            |               |
| **Test Case Id**       | **Action**                                                                      | **Expected Result**                                                                                        | **Pass/Fail** |
| 1                      | Profile owner fills out fields and clicks Update button                         | Profile owner redirected to Profile page updated fields are renderedMessage shown advising Profile updated | Pass          |
| 2                      | Profile owner leaves fields as is  and clicks Update button                     | Profile owner redirected to Profile page updated fields are renderedMessage shown advising Profile updated | Pass          |
| 3                      | Profile owner uploads new Profile image  and clicks Update button               | Profile owner redirected to Profile page and Profile image is updated                                      | Pass          |
| 4                      | Profile owner clicks Delete button                                              | Delete modal rendered and Profile owner asked if they are sure about deleting                              | Pass          |
| 5                      | Profile confirms Profile deletion                                               | Profile is deleted along with User accountUser redirected to Home page                                     | Pass          |
|                        |                                                                                 | Message shown "Sorry to see you go"User is no longer registered                                            | Pass          |

**Authentication**

| **Sign Up Page** |                                                                                 |                                                          |               |
|-------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| **Test Case Id** | **Action**                                                                      | **Expected Result**                                      | **Pass/Fail** |
| 1                | User fills out all required fields and clicks Sign Up button                    | User is redirected to Verify Email Page                  | Pass          |
| 2                | User  receives Verification email and clicks the link                           | User is directed to the Confirm Email Page               | Pass          |
| 3                | User clicks Confirm button on Confirm Email Page                                | Message shown advising User they confirmed email address | Pass          |
|                  |                                                                                 | User redirected to Login Page                            | Pass          |
|                  |                                                                                 |                                                          |               |
| **Login Page**   |                                                                                 |                                                          |               |
| **Test Case Id** | **Action**                                                                      | **Expected Result**                                      | **Pass/Fail** |
| 1                | User enters valid login credentials and clicks Login button                     | User redirected to registered users Home Page            | Pass          |
| 2                | User clicks sign up link                                                        | User redirected to Sign Up Page                          | Pass          |
| 3                | User clicks Forgot Password button                                              | User redirected to Password Reset Page                   | Pass          |
| 4                | User enters the Users account email address and clicks Reset My Password button | User redirected to Password Reset Email Sent Page        | Pass          |
| 5                | User recieves Password Reset email and clicks the link                          | User directed to Change Password Page                    | Pass          |
| 6                | User changes Password and clicks Change Password button                         | Message shown advising User Password has been changed    | Pass          |
|                  |                                                                                 | User redirected to Change Password Confirmed Page        | Pass          |
| 7                | User clicks Home button on Change Password Confirmed Page                       | User redirected to non registered Home Page              | Pass          |
|                  |                                                                                 |                                                          |               |
| **Logout Page**  |                                                                                 |                                                          |               |
| **Test Case Id** | **Action**                                                                      | **Expected Results**                                     | **Pass/Fail** |
| 1                | User clicks Sign Out button                                                     | User redirected to non registered Home Page              | Pass          |


[Back to top &uarr;](#contents)

## **Validators**

### **CI Python Linter**

The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python code used throughout the project. Results are outlined in the below:

![PEP8 Results](/docs/validation/pep_results.webp)

### **JSHint**

[JSHint](https://jshint.com/) was used to validate the Javascript code used in project. Only one undefined variable is showing "bootstrap" - this was taken from the walkthrough and altered to fix console error. No other issues to report.

![JSHint Results](/docs/validation/jshint.webp)

### **W3C CSS Validator**

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the sites css code.

![W3C CSS Validator](/docs/validation/css_results.webp)

### **W3C Markup Validator**

All pages were run through the [W3C Markup Validator](https://validator.w3.org/nu/). Initially there were some errors due to missing closing tags, image height values and richtextfield inputs. All of these issues were corrected and all pages passed validation.

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

### **Lighthouse Errors**

The errors encountered in the various reports are outlined below:

- "Eliminate render-blocking resources" - this was pointing towards bootstrap.min.css throughout, I am unaware of how to fix at this time
- "Displays images with incorrect aspect ratio", "Properly size images", "Serve images in next-gen formats" - I have tried resizing how the images are displayed but due to the fact they are being retrieved from the API there is not much I can do here.

I have tested the site on various devices and networks (3g, 4g & WIFI) and the above is not affecting the site, load times are good and no issues/delays reported by test users.

There is one console error due to the embedded Youtube video that cannot be fixed at this time, it refers to "Ensure CORS response header values are valid". Error only occurs when user clicks play on the video. I have reserached this previously and the issue appears to be between Google and Youtube so I am unable to fix this error. Please not this error does not seem to affect the performance of the site.

![Lighthouse Console Error](/docs/validation/lighthouse/trailer_console.webp)

## **Bugs & Fixes**

|   **Bug**                                                    |   **Issue**                                                                                                                                                                                                                                                                                                                  |   **Resolution**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   Directional buttons used for Name input                |   When user entered directional buttons in the Name input text was shifted upwards and over lapped ascii text                                                                                                                                                                                                             |   Added isalnum() to the input to resolve the issue and handled errors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|   Guardian Luck stat > than 10                           |   When multiple luck loot dropped players luck stat would go above 10, this meant player always hit the enemy which wasn’t intended                                                                                                                                                                                       |   After every loot drop I set the function to check if the luck stat was > than 10 and if it was I used the Guardian set_luck method to set the Luck stat to 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|   Guardian Defence Stat > than Enemy Attack              |   When multiple Defence loot dropped the player's Defence stat could become higher then the Enemy's attack stat which ended up applying a minus attack value which added health to the Player instead of taken health away                                                                                                |   After every loot drop I set the function to check if the Defence stat was > than 13 and if it was I used the Guardian set_defence method to set the Defence stat to 13 as the Enemy stat is between 14 & 20 for base enemy and 15 & 25 for Boss                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|   Enemy Defence Stat > than Gaurdians lowest Attack      |   Guardian attack stats are set values depending on class chosen, some attack stats were set to 5. When testing I originally had the Enemy Defence stat set to a random value between 1& 10 so when it was above 5 and Player used that attack instead of health being taken off the Enemy it was adding health to them.  |   To resolve I set the Enemy Defence stat to the max value of the lowest Player attack                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|   Path choice function was showing previous input        |   As the path_choice function takes in the users input as an argument when it was incorrect the user would be asked for the input again but would display the last input entered - this was occuring because I was trying to change the variable when the user was asked again to input choice                            |   To resolve I changed choice to choice2 in the function and issue was resolved.     `   def path_choice(choice, select_1, select_2,                   error, function_1, function_2):       '''       Function used throughout the game to       direct the story depending on your choice.       '''       choice2 = input(Fore.GREEN + Style.BRIGHT + choice +                       Style.RESET_ALL).lower().strip(" ")       if choice2 == select_1:           function_1()       elif choice2 == select_2:           function_2()       else:           print(error)           path_choice(choice, select_1, select_2, error, function_1, function_2)       print(Style.RESET_ALL)   `  |
|   Guardian Luck stat set to random value between 7 & 10  |   For the enemy to drop loot the Guardians luck stat would have to be above 7, with the initaial values this meant the enemy always dropped loot which was not intended                                                                                                                                                   |   To resolve I changed the Guardians luck stat to start between a value of 4 & 6 to vary loot drops                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|   Ascii art showing error                                |   When I pasted in Ascii art I received a lot of errors like the below:   invalid escape sequence '\'   Anomalous backslash in string: '\'                                                                                                                                                                                |   Upon investigating and many searches on Stackoverflow I was advised to convert the string to a raw string by placing a lowercase "r" in front of the text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|   App not launching after Heroku deployment              |   App would not open when deployed on Heroku - this was caused by the Requirements.txt being empty                                                                                                                                                                                                                        |   To resolve I entered the command pip3 list to get the list of modules being used and manually placed them in the Requirements.txt       I later found you could use the below commands to avoid manually doing this:       pip freeze > requirements.txt       pip install -r requirements.txt                                                                                                                                                                                                                                                                                                                                                                                              |

[Return to README.md](README.md)