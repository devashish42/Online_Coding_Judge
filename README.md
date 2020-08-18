<div align="center">
  <img src="https://github.com/arch888/Coding_Judge/blob/master/static/Documentation/Coding-Judge.png">
</div>

# Coding Judge

[![Github licence](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/arch888/Coding_Judge/blob/master/LICENSE) [![Generic Badge](https://img.shields.io/badge/Python_Version-3.7.2-brightgreen.svg)](https://github.com/arch888/Coding_Judge) [![Generic Badge](https://img.shields.io/badge/Django-3.0.2-brightgreen.svg)](https://docs.djangoproject.com/en/3.0/) [![Generic Badge](https://img.shields.io/badge/Vulnerabilities-0-brightgreen.svg)](https://github.com/arch888/Coding_Judge) 

## About Problem

An online platform for organising timed contests and practising programming problems by checking code on certain constraints such as time, space, and correctness.

##  Features

<details>
    <summary>REST API for running, and testing the code with custom input.</summary><br>
    A RESTful API for running and testing code in various programming languages.<br>
Supported Programming Languages -
<ul>
    <li>C / C++ (Language Code: 001)</li>
    <li>Java (Language Code: 002)</li>
    <li>Python (Language Code: 003)</li>
</ul>
</details>

<details>
    <summary>REST API for fetching current and previous contests.</summary>
</details>

<details>
    <summary>REST API for fetching questions for contest id.</summary>
</details>

<details>
    <summary>REST API for testing code in a programming language on open test-cases of a problem.</summary>
</details>

<details>
    <summary>REST API for submitting code for a problem of a contest / practice.</summary><br>
    Practice will also be a type of contest which have a very large end time. Due to which we will have the Leaderboard for overall Practice. Kind of All time Leaderboards.
    <br>
    Also it must have a feature of generating shortend URL of the submission Link. If the submitted solution is not submitted to a current ongoing contest.
</details>

<details>
    <summary>REST API for signing up or signing in for the users.</summary>
</details>

<details>
    <summary>REST API for contributing problems to the Coding_Judge.</summary>
</details>

<details>
    <summary>REST API for fetching leaderboard of a contest.</summary>
</details>


## Technology Stack

### Front-end Technologies

<ul>
    <li>HTML</li>
    <li>CSS</li>
</ul>

<details>
    <summary>Bootstrap</summary>
    <h4>
        What is Bootstrap?
    </h4>
    <p>
        Bootstrap is a CSS Framework for developing responsive and mobile-first websites.
    </p>
    <h4>
        Why Bootstrap?
    </h4>
    <p>
        This question can have two percepective which is -
        <ul>
            <li>Why to use Bootstrap?</li>
            <li>Why Bootstrap not Foundation or Pure?</li>
    	</ul>
    	<h5>
        	Why to use Bootstrap?
    	</h5>
    	To make the web-app responsive and mobile-friendly.
        <h5>
        	Why Bootstrap not Foundation or Pure?    
    	</h5>
    	The main advantage of Foundation or Pure over Bootstrap is that they are more customizable over Bootstrap. But in this project most of the users will visit from PC due to which the Bootstrap is the best choice for responsive and mobile-first website.<br>
        <b>Reference:</b> <a href="https://azmind.com/bootstrap-vs-foundation/#difference">Bootstrap vs Foundation</a>
    </p>
</details>

<details>
    <summary>Javascript</summary>
    <h4>
        What is Javascript?
    </h4>
    <p>
        Javascript is a programming language for web which can update and change both HTML and CSS.
    </p>
    <h4>
        Why Javascript?
    </h4>
    <ul>
        <li>For submitting code asynchronously.</li>
        <li>For updating the submmision results asynchronously.</li>
    </ul>
</details>

<details>
    <summary>ReactJS</summary>
    <h4>
        What is React?
    </h4>
    <p>
        React is a JavaScript library that builds user interfaces for single-page applications by dividing UI into composable components.
    </p>
    <h4>
        Why React?
    </h4>
    <ul>
        <li>Fast Rendering of web-pages using virtual DOM - Web-pages rending is a critical major task of the project as per percepective of performance./li>
        <li>Abstraction - Not Exposing complex internals of the code to the user.</li>
        <li>Reusable Components - There are lots of places where the same components of the webpage can be used.
        <br>For Example:
            <ul>
                <li>Coding Environment on the Practice page / Contest page.</li>
                <li>Problems Addition page as a individual component / on addition of a problem for a contest.</li>
            </ul>
        </li>
    </ul>
    <br><b>Reference:</b> <a href="https://stories.jotform.com/7-reasons-why-you-should-use-react-ad420c634247">Reasons to use React</a>
</details>

### Back-end Technology

<details>
	<summary>Django</summary>
    <h4>
        What is Django?
    </h4>
    Django is a high-level python web framework that encourages rapid Development and clean, pragmatic design.
    <h4>
        Why Django?
    </h4>
    <ul>
        <li>Scalable & Reliable - It's been 13 years Django started developing its framework</li>
        <li>Secure - As it have inbuilt authentication, authorization and session management which makes it secure.</li>
        <li>In-built Admin.</li>
        <li>MVC Architecture</li>
    </ul>
    <br><b>Reference:</b> <a href="https://djangostars.com/blog/why-we-use-django-framework/">Why Django?</a>
</details>

### Database

<details>
    <summary>MySQL</summary>
    <h4>
        What is MySQL?
    </h4>
    MySQL is a open-source relational database management system.
    <h4>
        Why MySQL?
    </h4>
    To understand the fact that why we have chosen MySQL over MongoDB or Cassandra. We have to understand CAP Theorem.<br>
    <b>CAP Theorem:</b> CAP theorem stands for "Consistency", "Availability", and "Partition Tolerance". According to CAP Theorem we can choose any two things at a time in a database. That is either "CP", "AP", or "CA" and for each of these type of the these we have several database from which we can choose.
    <ul>
        <li>CP: MongoDB</li>
        <li>CA: MySQL</li>
        <li>AP: Cassandra</li>
    </ul>
    <div align="center">
      <img src="https://miro.medium.com/max/1342/1*7mDBUO-j0yws52wZlSxbAg.png">
    </div>
    <br><br>As in our project the consistency and availability are the most important factor because there will be several users which will hit at the same time during the contest due to which the availability of the website is important. For Short-contest the updatation of the submission results should be consistent as much as possibile.
    <br><b>For Example:</b> Let's say the database is replicated into two parts that is A and B. Their is a user named "X" who submitted the solution for some problem after which a Docker Container is created for running the code into an isolated environment. After successfully running the code, the results are updated to the database replica A. But due to inconsistency issue in the database it is not updated on the database replica B. Due to which the submission results are not getting updated on the user-end. Therefore, consistency is very important for our system.<br>
    <b>Reference:</b> <a href="https://medium.com/@bikas.katwal10/mongodb-vs-cassandra-vs-rdbms-where-do-they-stand-in-the-cap-theorem-1bae779a7a15">What is CAP Theorem?</a>
</details>

### Version Control

<details>
    <summary>Github</summary>
</details>

### ER Diagram

<div align="center">
  <img src="https://github.com/arch888/Coding_Judge/blob/master/static/Documentation/ERD.jpg" alt="ERD">
</div>

## Pre-requisites of Project

<ul>
    <li>Python 3 (<a href="https://docs.python-guide.org/starting/install3/linux/">Installation</a>)</li>
    <li>Pip 3 (<a href="https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/">Installation</a>)</li>
    <li>Pipenv (<a href="http://manpages.ubuntu.com/manpages/eoan/man1/pipenv.1.html">Installation</a>)</li>
    <li>NPM (<a href="https://www.npmjs.com/get-npm">Installation</a>)</li>
    <li>Git (<a href="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git">Installation</a>)</li>
</ul>

## Installation of Project

### Clone the Repository

To clone the repository open the terminal and run below command:

```
git clone https://github.com/arch888/Coding_Judge
```

Change the current directory to the project directory:

```
cd Coding_Judge
```

### Install Dependencies

#### Django Dependencies

To create a fresh virtual environment run the below command in the terminal:

```
pipenv shell .
```

To install the django dependencies run the below command in the terminal:

```
pipenv install
```

### Setting up Database

Create a file name `Coding_Judge/db_conf.py` to store the configuration of the local Database:

```
touch Coding_Judge/db_conf.py
```

Variables in the configuration file should be:

```
DBNAME = 'database_name'
DBUSER = 'username'
DBPASSWORD = 'password'
DBHOST = '127.0.0.1'
DBPORT = ''
```

## More to Cover

<ul>
    <li>Contribution Guidelines</li>
    <li>Screenshots & Videos</li>
</ul>