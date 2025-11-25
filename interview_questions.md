1. How do you collect user input?
In a script, we use the input() function: name = input("Enter name: "). In a web app like Flask, we use request.form or request.json to get data sent from the frontend.

2. What is the difference between == and =?
 * = is the assignment operator (e.g., x = 5 assigns the value 5 to x).
 * == is the comparison operator (e.g., if x == 5 checks if x is equal to 5).

3. What is a chatbot?
A chatbot is a software application designed to simulate human conversation, either via text or voice interactions. They can be rule-based (like this task) or AI-based (using Machine Learning).

4. What is the limitation of rule-based bots?
Rule-based bots can only respond to specific inputs they are programmed to understand. If a user asks a question in a way the developer didn't predict, the bot fails or gives a generic error response. They cannot "learn" new things.

5. How can you exit a loop on command?
You use the break statement inside an if condition.
while True:
    msg = input()
    if msg == "bye":
        break

6. What's the use of lower()?
.lower() converts a string to all lowercase letters. This is crucial for chatbots so that "Hello", "hello", and "HELLO" are all treated as the same greeting.

7. How would you handle multiple intents?
You can use elif statements to check for different keywords. For example: if "joke" in text: ... elif "weather" in text: .... In advanced bots, you would use NLP libraries (like NLTK or spaCy) to classify the intent.

8. How would you test this?
You test it by inputting various phrases (valid commands, invalid commands, different capitalizations, empty strings) to ensure the if-else logic covers all scenarios and doesn't crash.

9. How to organize code better?
Instead of one giant if-else block, you should separate the logic into functions (like get_bot_response()) or even separate files. You can also use dictionaries to map keywords to responses.

10. How can this evolve into an ML bot?
Instead of hardcoded rules, you would use a dataset of conversations to train a Machine Learning model (using libraries like TensorFlow or PyTorch) to predict the best response based on the input context.
