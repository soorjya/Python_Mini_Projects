# Quiz Program

This repository contains a Quiz Program developed in Python. It is a command-line based application that allows users to take a simple quiz and test their knowledge.

## Features

- Simple and interactive command-line quiz program.
- Questions and answer choices are stored in a dictionary for easy customization.
- Supports multiple choice questions.
- Provides immediate feedback on the correctness of user answers.
- Calculates and displays the final score at the end of the quiz.

## Usage

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/soorjya/quiz-program.git
  
 2. Navigate to the project directory:

```shell
cd quiz-program
```
3. Run the program:

  ```shell

quiz.py
  ```
  
4. Follow the on-screen instructions to answer the quiz questions.

## Customization

You can customize the Quiz Program by modifying the quiz questions in the quiz.py file. Here's how:

1. Open the `quiz.py` file in a text editor.

2. Modify the questions and answer choices in the quiz_questions dictionary. Each question is represented by a key-value pair, where the key is the question and the value is a list of answer choices.

```python
quiz = "Question 1":{
        "Question":"First Question",
        "Answer": "ANSWER"
      },
        "Question 2":{
        "Question":"Second Question",
        "Answer":"ANSWER"
      },
      #Add more question like this
```
3. Save the changes and run the program again to see your modified quiz.

4. Feel free to explore the code and make any necessary modifications to suit your needs.

## Contribution
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. Here are some ways you can contribute:

- Add more quiz questions to expand the program's content.
- Improve the user interface or add new features. 
- Fix any bugs or issues you encounter.
- When contributing, please follow the existing coding style and submit descriptive pull requests.

## License

This project is licensed under the MIT License.

## Acknowledgements

The quiz program is a simple implementation using Python's dictionary function.
The project structure and code organization are influenced by best practices in software development.
