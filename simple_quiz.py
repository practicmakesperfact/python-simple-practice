questions = [
    { 
     'prompt': "what is the capital of Ethiopia ?",
      'options':['A. Baherdar','B. markos', 'C. AdisAbeba', 'D. wollo'],
      'answer': "C"
        
    },
    { 
     'prompt': "what is the capital of Sudan ?",
      'options':['A. Kartum','B. suahiry', 'C. kagi', 'D. junki'],
      'answer': "A"
        
    },
    { 
     'prompt': "what is the capital of USA ?",
      'options':['A. NewYork','B. Washington D.C', 'C. Canada', 'D. kamerun'],
      'answer': "B"
        
    },
    { 
     'prompt': "what is the smallest prime number ?",
      'options':['A. 1','B. -1', 'C. 0', 'D. 2'],
      'answer': "D"
        
    },
    { 
     'prompt': "what is the largest continent in the world?",
      'options':['A. Asia','B. Africa', 'C. Australia', 'D. Europ'],
      'answer': "A"
        
    },
]


def test_quiz(questions):
    score=0
    for question in questions:
        print(question['prompt'])
        for option in question['options']:
           print(option)
        ansewr=input('What is your answer : ')
        if ansewr==question['answer']:
           print('correct!!\n')
           score+=1
        else:
           print("Incorrect!! , the correct answer is",question["answer"])
    print(f"You got {score} out of {len(questions)} questions correct!")
    
test_quiz(questions)