# QA task#1
## Cucumber with Behave


Cucumber is available for most mainstream programming languages. Behave allows Cucumber to support step definitions written in python.

Behave is a tool used for Behaviour driven development (BDD) in Python
programming language. In an Agile development framework, BDD creates a culture where
testers, developers, business analysts, and other stakeholders of the project can
contribute towards the software development.


## The Gherkin Language 

Gherkin uses a set of special keywords to give structure and meaning to executable specifications. Each keyword is translated to many spoken languages

For more reference click [here](https://cucumber.io/docs/gherkin/reference/)

### [Gherkin: Feature Testing Language](https://behave.readthedocs.io/en/stable/gherkin.html#gherkin-feature-testing-language)
Behave features are written using a language called Gherkin (with some modifications) and are named “name.feature”.

#### Features
Features are composed of scenarios. They may optionally have a description, a background and a set of tags


## Behave Installation
Behave installation can be done by the following ways:

To install pip with Behave, run the command given below:
```sh
 pip install behave 
```
Also need Selenium to interact with the webdriver
```sh
pip install selenium
```

For executing a Feature file we need to run

````shell
behave featurename.feature
````
