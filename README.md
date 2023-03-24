# **Cinema | Go**

## **Overview**

Cinema | Go is a Movie site designed to allow a User to find and review Movies. The site features a search function using the TMDB API that allows users to search for any Movie they wish. There is a Trending and Top Rated section too so users can view the most popular Movies today and the highest rated of all time. Users will be able to view Movie details such as Title, Director, Overview, Trailers, etc. Users will also be able to review Movies and add Movies to a watchlist that can be displayed on their customizable Profile page, here they will be able to enter information about themselves and upload their Profile picture. You are not authorized to delete this review.

Developed by Sean Finn.

![EZGIF Animation](/docs/gifs/cinema-go.gif)

[Cinema | Go - Live Webpage](https://cinema-go-p4.herokuapp.com/) (Right-click to open in a new tab)

## **Project Goals**

This is my fourth portfolio project for [Code Institute](https://codeinstitute.net/) and my goal with this project is to display my newly acquired skills with frameworks such as Bootstrap and Django. I decided to build a Movie based review site that works in tandem with the TMDB API.

## **Contents**

1. [Overview](#overview)
1. [Project Goals](#project-goals)
1. [UX](#ux)
    - [The Strategy Plane](#the-strategy-plane)
    - [The Ideal User](#the-ideal-user)
    - [Site Goals](#site-goals)
    - [Agile Planning](#agile-planning)
1. [Design](#design)
    - [Imagery](#imagery)
    - [Color Scheme](#color-scheme)
1. [How to Play](#how-to-play)
    - [Setup Phase](#setup-phase)
    - [How to Win](#how-to-win)
1. [User Stories](#user-stories)
1. [Data Model](#data-model)
    - [Classes](#classes)
    - [Game Flow](#game-flow)
1. [Features](#features)
1. [Libraries](#libraries)
1. [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks and Tools Used](#frameworks-and-tools-used)
1. [Testing](#testing)
1. [Future Updates](#future-updates)
1. [Deployment](#deployment)
1. [Credits](#credits)
1. [Acknowledgements](#acknowledgements)

## **UX**

### **The Strategy Plane**

Cinema | Go is intended to bring together all Movie lover's to find their favourite Movies and discover new ones. Users will be able to review and rate Movies and create their watchlist which they can manage from their custom Profile page. The graphical elements and overall design of the site provide the user with an enjoyable experience with an aesthetically pleasing display.

#### **The Ideal User**

- Someone who enjoys movies and would like to discover new movies
- Someone who would like to review/rate movies and share those reviews with fellow movies lovers
- Someone who would like to create a watchlist of movies and share it with others
- Someone who would like to create their own custom Profile page, share some information about themselves and their Movie interests

#### **Site Goals**

- To provide users with a place to find movies they have seen and discover new ones
- To provide users with the ability to review/rate movies
- To provide users with the ability to create their own Profile and movie watchlist
- To provide users with the ability to view other users reviews and watchlists

### **Agile Planning**

This project was developed using agile methodologies by delivering small features across the duration of the project. All User Stories were assigned to Epics, prioritized under the labels, Must Have, Should Have and Could Have. They were assigned story points according to complexity. Story points were adjusted mid-project to use the common Fibonacci sequence correctly. "Must Have" stories were completed first, "Should Have's" and then finally "Could Have's".

It was done this way to ensure that all core requirements were completed first to give the project a complete feel. In some scenarios, certain "Could Have's" were implemented before schedule due to the easy nature of the implementation i.e. Trending/Top Rated Movies. The rest were applied based on capacity and timing.

The Kanban board was created using Github projects and can be located [here](https://github.com/users/seanf316/projects/7)  and can be viewed to see more information on the project cards. All stories have a full set of acceptance criteria to define the functionality that marks that story as complete.

![Project Kanban](docs_screenshots/kanban-board.webp)

### **Epics**

11 Epics (milestones) were created which were then further developed into 34 User Stories. The details on each epic, along with the user stories linked to each one can be found in the project kanban board linked above. 2 extra unplanned User Stories were created during development as an extra feature for the user - Trending Movies & Toprated Movies. They were added as the time to implement was very short and did not require an Epic.

#### **EPIC: Initial Django Setup [#1](https://github.com/seanf316/P4-Cinema-Go/issues/1)**
`
As a Developer, I can setup Django and start project, so that I can develop the site
`

The Initial Django Setup epic was required to setup the project and confirm libraries, frameworks etc were installed correctly. Only then could further development progress.

#### **EPIC: Initial Deployment [#2](https://github.com/seanf316/P4-Cinema-Go/issues/2)**
`
As a Developer, I can deploy my site with Heroku, so that user's can view and interact with the site
`

The Initial Deployment epic was completed early on as we were advised during the course material that early deployment is critical to avoid any issues down the line with the production app. Heroku app was creating and config vars were updated, app was linked to my projects Github repo for automatic deployments.

#### **EPIC: Base Html/Homepage [#9](https://github.com/seanf316/P4-Cinema-Go/issues/9)**
`
As a Developer, I can design a nice aesthetically pleasing Homepage, so that the user has an enjoyable experience when navigating site
`

The Base Html/Homepage epic was used to link various User Stories based around the design and responsiveness of the site. The Base template was created first so I could extend within further templates and then the homepage(index.html) was built using bootstrap and styled. Nav and Footer were progressed under seperate User Stories.

#### **EPIC: User Account/Profile [#3](https://github.com/seanf316/P4-Cinema-Go/issues/3)**
`
As a Developer, I can provide account/profile creation functionality, so that user can create/read/update or delete their account/profile
`

The User Account/Profile epic is for all User Stories related to the setup of the account/profile and the CRUD functionality and templates design.

#### **EPIC: User Signup/Login/Logout [#4](https://github.com/seanf316/P4-Cinema-Go/issues/4)**
`
As a Developer, I can provide Signup/Login/Logout functionality, so that user can safely signup/login/logout and prevent access to their profile
`

The User Signup/Login/Logout epic is for all User Stories related to the registration, login and authorization of views.

#### **EPIC: Movie Search [#5](https://github.com/seanf316/P4-Cinema-Go/issues/5)**
`
As a Developer, I can provide the Movie search functionality, so that User can easily search for movies to review
`

The Movie Search epic is for all User Stories related to the setup of the Movie search functionality and the use of the TMDB API. Any templates created or styled were linked also.

#### **EPIC: View Search Results [#6](https://github.com/seanf316/P4-Cinema-Go/issues/6)**
`
As a Developer, I can provide search results display, so that the user can view all Movies related to their search
`

The View Search Results epic is for all User Stories related to the search results page and displaying the results from the API call. Any templates created or styled were linked also.

#### **EPIC: View Movie Details [#7](https://github.com/seanf316/P4-Cinema-Go/issues/7)**
`
As a Developer, I can provide a display of the Movie details, so that user can view the Movie details for the Movie they selected
`

The View Movie Details epic is for all User Stories related to the Movie details page and displaying the Movie information such as Title, Overview, Director etc. Any templates created or styled were linked also.

#### **EPIC: Movie Reviews/Comments [#8](https://github.com/seanf316/P4-Cinema-Go/issues/8)**
`
As a Developer, I can provide review/comment functionality, so that registered users can review a Movie or comment on an existing Movie review
`

The Movie Reviews/Comments epic is for all User Stories related to the Review and Comment functionality. Any templates created or styled were linked also.

#### **EPIC: Status Error Templates [#11](https://github.com/seanf316/P4-Cinema-Go/issues/29)**
`
As a Developer, I can create Status Error templates, so that I can secure my views and advise User when there is an issue
`

The Status Error Templates epic is for all User Stories related to providing status error feedback to the User like 403, 404 and 500 status errors. Any templates created or styled were linked also.

#### **EPIC: Complete Documentation [#10](https://github.com/seanf316/P4-Cinema-Go/issues/10)**
`
As a Developer, I can create documentation, so that fellow developers can understand what the site is and how it was built
`

This epic is for all document related stories and tasks that are needed to document the software development lifecycle of the application. It aims to deliver quality documentation, explaining all stages of development and necessary information on running, deploying and using the application.

### **User Stories**

The following user stories (by epic) were completed throughout development.

#### **EPIC: Initial Django Setup [#1](https://github.com/seanf316/P4-Cinema-Go/issues/1)**

- As a Developer I can set up Django and install the supporting libraries predicted to be needed so that I am ready to start development [#11](https://github.com/seanf316/P4-Cinema-Go/issues/11)
- As a Developer I need to create the env.py and add to .gitignore so that I can securely deploy the site without exposing developer keys/information [#12](https://github.com/seanf316/P4-Cinema-Go/issues/12)

#### **EPIC: Initial Deployment [#2](https://github.com/seanf316/P4-Cinema-Go/issues/2)**

- As a Developer I can deploy site to Heroku early so that I can confirm everything works before development of the site and to enable continuous testing within the production environment [#13](https://github.com/seanf316/P4-Cinema-Go/issues/13)

#### **EPIC: Base Html/Homepage [#9](https://github.com/seanf316/P4-Cinema-Go/issues/9)**

- As a User I would like to view the site on my different devices so that I can review the site on the go [#14](https://github.com/seanf316/P4-Cinema-Go/issues/14)
- As a User I want to see a clear way of navigating the site so that I can find the information relative to my needs [#15](https://github.com/seanf316/P4-Cinema-Go/issues/15)
- As a User I want to be able to get in touch with the Developer so that I can enquire about issues/suggestions I may have [#16](https://github.com/seanf316/P4-Cinema-Go/issues/16)

#### **EPIC: User Account/Profile [#3](https://github.com/seanf316/P4-Cinema-Go/issues/3)**

- As a User I would like access to my Profile so that I can upload an image or alter my details where needed [#18](https://github.com/seanf316/P4-Cinema-Go/issues/18)
- As a Developer I can create an aesthetically pleasing display of the User's Profile so that the experience of viewing their Profile is a pleasant one [#23](https://github.com/seanf316/P4-Cinema-Go/issues/23)
- As a Developer I can create an edit Profile template so that the User has a nice display for when they want to update their Profile [#40](https://github.com/seanf316/P4-Cinema-Go/issues/40)
- As a Developer I can create a Delete Profile view so that the User has access to delete their account. [#41](https://github.com/seanf316/P4-Cinema-Go/issues/41)
- As a User I would like the ability to add Movies to a watchlist so that so that I can have a list of movies that I can refer to when looking for something to watch [#42](https://github.com/seanf316/P4-Cinema-Go/issues/42)

#### **EPIC: User Signup/Login/Logout [#4](https://github.com/seanf316/P4-Cinema-Go/issues/4)**

- As a User I want to Sign Up/Login and Logout so that I can see what features are available to registered users like reviewing/commenting [#17](https://github.com/seanf316/P4-Cinema-Go/issues/17)

#### **EPIC: Movie Search [#5](https://github.com/seanf316/P4-Cinema-Go/issues/5)**

- As a User I want to have a section where I can search for a Movie so that I can easily find the Movie I want to review [#19](https://github.com/seanf316/P4-Cinema-Go/issues/19)
- As a Developer I can create the Movie Search Template so that the User has an nice experience on the site [#20](https://github.com/seanf316/P4-Cinema-Go/issues/20)
- As a Developer I need to setup an account with TMDB so that I can use the sites API and implement into my site [#21](https://github.com/seanf316/P4-Cinema-Go/issues/21)

#### **EPIC: View Search Results [#6](https://github.com/seanf316/P4-Cinema-Go/issues/6)**

- As a Developer I can create the Movie Search Results template so that the User has a clear display of the results from their search [#37](https://github.com/seanf316/P4-Cinema-Go/issues/37)

#### **EPIC: View Movie Details [#7](https://github.com/seanf316/P4-Cinema-Go/issues/7)**

- As a User I want to view the Movie details from my search so that I can read the synopsis and check reviews [#22](https://github.com/seanf316/P4-Cinema-Go/issues/22)
- As a Developer I can build a page to display the Movie Details for the users selected Movie so that they have a clear overview of the Movie [#24](https://github.com/seanf316/P4-Cinema-Go/issues/24)
- As a Developer I will create a Movie model so that the movie details that the user references can be saved to the database for use with Reviews/Profile etc [#38](https://github.com/seanf316/P4-Cinema-Go/issues/38)

#### **EPIC: Movie Reviews/Comments [#8](https://github.com/seanf316/P4-Cinema-Go/issues/8)**

- As a User I want the ability to review Movies so that I can share my thoughts of the Movie with family and friends [#25](https://github.com/seanf316/P4-Cinema-Go/issues/25)
- As a Developer I can create a nice display for the User to review so that they have an enjoyable experience reviewing Movies on the site [#26](https://github.com/seanf316/P4-Cinema-Go/issues/26)
- As a User I would like the ability to edit my review so that I can fix and spelling or format issues [#43](https://github.com/seanf316/P4-Cinema-Go/issues/43)
- As a User I would like the ability to delete my review so that I can manage my reviews and in the case of accidentally selecting the wrong Movie and reviewing it [#44](https://github.com/seanf316/P4-Cinema-Go/issues/44)
- As a User I would like the ability to view all movie reviews so that I can see what my fellow reviewers think of other movies [#45](https://github.com/seanf316/P4-Cinema-Go/issues/45)
- As a Developer I can create an All Reviews page so that the User can have a nice display containing all reviews [#46](https://github.com/seanf316/P4-Cinema-Go/issues/46)
- As a User I would like the ability to comment on Reviews so that so that I can participate in conversations with fellow reviewer's [#27](https://github.com/seanf316/P4-Cinema-Go/issues/27)
- As a Developer I can create a section on the Review page for comments so that User's can comment on reviews [#28](https://github.com/seanf316/P4-Cinema-Go/issues/28)

#### **EPIC: Status Error Templates [#11](https://github.com/seanf316/P4-Cinema-Go/issues/29)**

- As a Developer I can implement a 403 error page to redirect unauthorised users so that I can secure my views [#30](https://github.com/seanf316/P4-Cinema-Go/issues/30)
- As a Developer I can implement a 404 error page so that I can alert users when they have accessed a page that doesn't exist [#31](https://github.com/seanf316/P4-Cinema-Go/issues/31)
- As a Developer I can implement a 500 error page so that I can alert users when an internal server error occurs [#32](https://github.com/seanf316/P4-Cinema-Go/issues/32)

#### **EPIC: Complete Documentation [#10](https://github.com/seanf316/P4-Cinema-Go/issues/10)**

- Create/Write README.md [#33](https://github.com/seanf316/P4-Cinema-Go/issues/33)
- Create/Write TESTING.md [#34](https://github.com/seanf316/P4-Cinema-Go/issues/34)

### **The Skeleton Plane**

#### **Wireframes**

This is the prototype of the project that may change during its development.
<details><summary>Desktop</summary>

![Desktop Part 1](/docs/wireframes/desktop/home.webp)
![Desktop Part 2](/docs/wireframes/desktop/search.webp)
![Desktop Part 3](/docs/wireframes/desktop/searchresults.webp)
![Desktop Part 4](/docs/wireframes/desktop/category.webp)
![Desktop Part 5](/docs/wireframes/desktop/movie.webp)
![Desktop Part 6](/docs/wireframes/desktop/review.webp)
![Desktop Part 7](/docs/wireframes/desktop/signup.webp)
![Desktop Part 8](/docs/wireframes/desktop/login.webp)
![Desktop Part 9](/docs/wireframes/desktop/signout.webp)

</details>


## **How to Play**

Reclaim The Light is a very easy game to play, all the player needs to do is input letters that correspond to the choices provided to the player. The player's goal is to retrieve the Light crystal that was stolen by the evil creatures known as the Darkness. The Player will be sent on an adventure to the planet Nessus to fight the Darkness and Reclaim The Light.

### **Setup Phase:**

The player will be asked for their name and be requested to pick a class for their "Guardian", the classes are "W" for "Warrior", "A" for "Assasin" or "M" for "Mage". After that, they will be shown a screen containing their Guardian stats.

### **How to Win:**

The player will make choices that will lead them into battles on occasion, if the player survives they will move on to the next part of the adventure leading to a boss battle at the end. If they defeat the boss they will Reclaim The Light and win the game. 

## **User Stories**
As a user, I want to be able to:
* Understand the aim of the story.
* Have a straightforward way to read the game instructions from within.
* To access a fun engaging story narrative throughout the game.
* Find loot and upgrade my stats.

[Back to top &uarr;](#contents)

## **Data Model**

### **Classes**
With Object-Oriented Programming in mind, I have created two classes for my project Guardian & Enemy.

The Guardian class is called once throughout the adventure. The Guardian object is created when called by the gen_char() function. The Enemy class is called upon several times throughout various battles. The Enemy Object is created when called by the gen_enemy() function.

The classes and their associated methods are stored in separate files to allow for separating the code into parts that hold related data and functionality. This will allow any future expansion and development of this project to have a clear structure and also for any code re-use and sharing as well as maintenance.
See class details below:

![Classes](/docs/flowchart/classes.webp)

### **Game Flow**
I created the below flowchart to visualize the flow of the game and the functions used.
![Flowchart](/docs/flowchart/reclaim_flowchart.webp)

[Back to top &uarr;](#contents)

## **Features**

### **Welcome Screen**
The user is met with a bright Welcome Screen with some colored Ascii text to provide an aesthetically pleasing experience. There are 3 options to choose from Start, Mission Log, or About.
![Welcome Screen](/docs/screenshots/welcome.webp)

### **Mission Log**
`
User Story: As a user, I want to be able to understand the aim of the story.
`

The Mission Log provides the user with the backstory and the aim of the game. It is displayed to the user using the type print animation followed up with the pause function imported from the py-getch Library. This allows the user to take their time reviewing the Mission Log text before pressing any key to return to Welcome Screen.
![Mission Log](/docs/screenshots/mission_log.webp)

### **About**
`
User Story: As a user, I want to have a straightforward way to read the game instructions from within.
`

The About section provides the user with details of what the game is and the instructions for the game. There is also a section that provides information on each Guardian class Warrior, Assassin, or Mage. This will give the user a better idea of what class they would like to pick for the game.
![About](/docs/screenshots/about.webp)

### **Start**

When the user selects Start they will be brought to a screen with some bright Ascii text welcoming them to the game. They will then be prompted to enter a name for their Guardian which consists of only letters and numbers. The user upon completing that stage will be prompted to select 1 of the 3 possible classes provided Warrior, Assassin, or Mage. After the user completes that step they will see the text - "Generating Guardian"
![Start](/docs/screenshots/setup.webp)

### **Stats**

When the user has completed the Start setup they will be provided with a screen that displays some weapon-related ASCII art along with their Guardian stats. The stats consist of 6 values (Attack, Defense, Health, Luck, Magic, and Range) followed by the user's name. The stats are all generated using the gen_char() function that calls on the Guardian class. The stats change based on the class chosen by the user i.e. If they choose Mage the Magic stat will be higher compared to the other classes. The only stat that doesn't have a set value is the Luck stat which is generated within the gen_char() function and is set up to be a random value i.e. luck = random.randint(4, 6)
![Stats](/docs/screenshots/stats.webp)

### **Adventure Story**
`
User Story: As a user, I want to access a fun engaging story narrative throughout the game.
`

When the user has reviewed their stats they can press any button to begin the adventure. Each of the main narratives provides the user with either bright Ascii text or some ASCII art that is related to the narrative the user is currently viewing. The text will again be displayed using the type print animation to draw the user's attention to the screen. At the end of the narrative, the user will be offered 2 choices, each choice sends the user on a different path allowing for a fun and engaging game.
![Adventure Story](/docs/screenshots/nessus.webp)

### **Loot**
`
User Story: As a user, I want to find loot and upgrade my stats.
`

There are three forms of loot in the game - Common, Legendary & Exotic. Each item of loot contains a Rarity, Name, Value & stat Assignment i.e. Common - Worn Sword - 1 - Attack.

Common items have a Value of 1, Legendary items have a Value of 2 and Exotic items have a Value of 3. Loot values are added to the player's stats when they are found in chests or dropped from enemies. The image below consists of what the user will see (examples):

Common items are displayed in the color CYAN

Legendary items are displayed in the color MAGENTA

Exotic items are displayed in the color YELLOW
![Loot](/docs/screenshots/loot.webp)

### **Battle Sequence**

#### **Initiating Battle**
`
User Story: As a user, I want to access a fun engaging story narrative throughout the game.
`

When the user has entered into a fight with an enemy a new screen will display containing the following:

Ascii art - I choose a skull head to engage the user and it is colored in red to draw the user's attention to the screen.

Enemy name - The enemy name is taken randomly from the enemy.txt file. It is colored in red to draw the user's attention to the screen.

Enemy stats - The enemy stats are generated using the gen_enemy() function that calls the Enemy class. The stats consist of Health, Attack, Defense, Chance, and Name. Each stat generates a random number between the values set in the function i.e. health = random.randint(80, 100)
![Initiating Battle](/docs/screenshots/battle.webp)

#### **Engaged in Battle**
`
User Story: As a user, I want to access a fun engaging story narrative throughout the game.
`

When the battle begins users will have the first turn to attack, they will be prompted to enter "C" for "Close attack", "R" for "Ranged" attack, or "M" for "Magic" attack.

After selecting an attack the following text will display: "You wind up for the attack..."

The strike_chance() function is called to determine whether the player's attack is successful. If the attack is successful the amount of health lost by the enemy is calculated by the attack value used minus the enemy's defense value i.e. 

if choice == "c":
            damage = guardian.get_attack() - enemy.get_e_defence()

The user will be alerted that their attack was successful and the enemy's new health stat will be displayed. If the user's attack was not successful the following text will be displayed: "You missed! Enemy dodged your attack".

It will be the enemy's turn now, the enemy_attack() function is now called to determine if the enemy attack will be successful. If the attack is successful the amount of health lost by the user is calculated by the attack value used minus the user's defence value i.e. 

loss = attack_value - defence

If the enemy attack is successful the user will be alerted and their new health stat will be displayed.

Some of the text is displayed with the color Red to engage the user and signify the imagery of blood loss.

![Engaged in Battle](/docs/screenshots/battle1.webp)

#### **Battle Victory**
`
User Story: As a user, I want to find loot and upgrade my stats.
`

If the enemy is defeated by the user the user will be alerted i.e. "Centurian, has been slain!"

The loot() function is then called. It picks a random.int between 0 and 7 and if the value provided is greater than the user's current luck value the enemy won't drop any loot and the following text will display: "That creature dropped no loot..."

If the user's luck value is greater than the random.int then the enemy will drop loot. It will be displayed to the user with the text "The enemy dropped an....." along with the loot values retrieved from the loot .txt files. The value of the loot will be added to the user's current stats and stats will be displayed to the user.

![Battle Victory](/docs/screenshots/battle2.webp)

#### **Battle Lost**
`
User Story: As a user, I want to access a fun engaging story narrative throughout the game.
`

If the user is defeated a new screen will be displayed alerting the user that they have been slain along with some Game Over ASCII art. The user will also see some text advising to press any key to return to Welcome Screen.

![Battle Lost](/docs/screenshots/gameover.webp)

### **Adventure Victory Screen**
`
User Story: As a user, I want to access a fun engaging story narrative throughout the game.
`

If the user completes the adventure without dying they will be provided a message stating that they "Reclaimed The Light" and a thank you message. Ascii Text along with Ascii art is used here to grab the user's attention. The user will be then prompted to return to the Welcome Screen where they can start another adventure if they choose to do so.

![EZGIF Animation](/docs/gifs/reclaim_2.gif)

[Back to top &uarr;](#contents)

## **Libraries**
For this project I used the following libraries:

### ***random:***
-   randint was used throughout the project to produce random stats or pick a random index in the choice list for loot.

### ***time:***
-   time was imported to make use of the sleep function which was used throughout the adventure. It was implemented to increase the time between narrative text's showing and it also provided a level of intrigue for the user i.e. when opening a loot box

### ***math:***
-   math.ceil was used to make sure the calculated loss from enemy or character strike was rounded upward to its nearest integer.

### ***pprint:***
-   pprint was used to print out the user's/enemy's stats and nicely display them for the user.

### ***getch:***
-   pause imported from getch to pause the gameplay and give the user more time to review the story.

### ***os:***
-   system used in conjunction with the clear/cls command to clear the display so the user would not get overwhelmed by reams of outdated data from previous narratives.

### ***colorama:***
-   Fore & Style were imported from colorama to style the font, ASCII text, and ASCII art with color.

[Back to top &uarr;](#contents)

## **Technologies Used**

### **Languages Used**

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### **Frameworks and Tools Used**

1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
1. [Heroku](https://www.heroku.com/)
    - Heroku was used to deploy the app.
1. [XConvert](www.xconvert.com)
    - XConvert was used to convert images to webp or png where required.
1. [Stackoverflow](https://stackoverflow.com/)
    - Stackoverflow was used on many occasions to figure out some troublesome code.
1. [CI Python Linter](https://pep8ci.herokuapp.com/)
    - I used CI Python Linter for the validation of the site's Python code.
1. [Grammarly](https://www.grammarly.com/)
    - Grammarly was used to check typography.
1. [Quicktime Player](https://support.apple.com/downloads/quicktime)
    - Quicktime Player was used to take recordings of the screen.
1. [ezgif.com](https://ezgif.com/)
    - ezgif.com was used to convert screen recordings to gif.
1. [Xnip](https://www.xnipapp.com/)
    - Xnip was used to capture all the game screenshots.
1. [Lucidchart.com](https://www.lucidchart.com/pages/)
    - The Lucidchart app was used to create the app's flowcharts.

[Back to top &uarr;](#contents)

## **Testing**
I have included details of testing both during development and post-development in a separate document called [TESTING.md](TESTING.md)

## **Future Updates**

I would like to add the following updates in the future when time permits:

1. Enemy Weakness - I would like to add a weakness stat for the enemy to a specific Guardian attack, it wasn't part of my original scope for the adventure but something I would be interested in implementing in the future.
2. Battle graphic animations - show the user and enemy in battle with moving Graphics.
3. Sound Effects - I would like to apply sound effects for the different Narratives and for the battle sequences.

[Back to top &uarr;](#contents)

## **Deployment**

### **GitHub**

This project was developed by forking a specialized [Code Institute template](https://github.com/Code-Institute-Org/python-essentials-template) which simulates a terminal in the web browser. 

1. Click Use this template
2. Name the repository
3. Launch using the Gitpod web extension
4. Pin project in Gitpod workspaces

### **Version Control**

For version control the following steps were made:

1. Changes made to files in Gitpod
2. Files made ready for commit with command - git add .
3. For the commits the following command was run along with commit description - git commit -m "This is my commit etc"
4. To move the changes to Github the following command was run - git push  

### **Forking the GitHub Repository**

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the repository [P3-Reclaim-The-Light](https://github.com/seanf316/P3-Reclaim-The-Light)
2. At the top of the Repository (not the top of the page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### **Final Deployment with Heroku**

The below steps were followed to deploy this project to Heroku:
1. Go to [Heroku](https://dashboard.heroku.com/apps) and click "New" to create a new app.
2. After choosing the app name and setting the region, press "Create app".
3. Go to "Settings" and navigate to Config Vars. Add a Config Var with a keyword called PORT and a value of 8000.
4. Still in the "Settings", navigate to Buildpacks and add buildpacks for Python and NodeJS (in order).
5. Leave "Settings" and go to "Deploy". Scroll down and set Deployment Method to GitHub.
Once GitHub is chosen, find your repository and connect it to Heroku.
6. Scroll down to Manual Deploy, make sure the "main" branch is selected and click "Deploy Branch". 
7. The deployed app can be found [here](https://reclaim-the-light-p3.herokuapp.com/).

[Back to top &uarr;](#contents)

## **Credits**

1. [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - This repository was created using the template provided by Code Institute. Also, without the knowledge gained through the coursework, I would not be able to create this site so thank you Code Institute.
1. [Corey Schafer](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)
    - Corey Schafer for the Python OOP Tutorial series for general reference on working with classes and OOP in general.
1. [delftstack.com](https://www.delftstack.com/howto/python/python-clear-console/)
    - Provided the clear display function used in the project.
1. [Stackoverflow](https://stackoverflow.com/)
    - I found myself on Stackoverflow so many times researching issues with python code. This a fantastic place to learn and troubleshoot code.
1. [Slack](https://slack.com/intl/en-ie/)
    - The slack community is great and I reached out to fellow students who had already completed their P3 for their advice and got some nice tips and feedback.
1. [pixabay.com](https://pixabay.com/)
    - Favicon image was taken from [pixabay.com](https://pixabay.com/), the image was free to use. The creaters name is OpenClipart-Vectors.

## **Acknowledgements**

- To my amazing wife Denise who has supported me every day and kept me motivated. After P1 & P2 it was a short and stressful turnaround for P3, Denise consistently encouraged me to work on the project while keeping our 5-year-old son entertained. I couldn't do this without her.
- My son Alex for always making me laugh and never getting mad when Dad had to study.
- My classmate Sean Johnston for the continuous testing of my project throughout and for being there to bounce ideas off.
- My classmates Victoria Traynor & Monica Murray for reviewing and testing my Project thanks guys.
- To my mentor Daisy Mc Girr, this was my first full project with Daisy and she goes above and beyond. Even outside of project planning she is great for advice and is a great help to the Slack community too.

[Back to top &uarr;](#contents)