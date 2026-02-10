// MCQ Quiz App (20 questions, only decision statements, no function, no import, no main)

int score;
int total;
int repeat;
int i;
int wrongAnswers[20];
char userAns;

repeat = 1;

while(repeat == 1) {
    score = 0;
    total = 20;
    i = 0;
    while(i < 20) {
        wrongAnswers[i] = 0;
        i = i + 1;
    }

    printf("Welcome to the 20 Question MCQ Quiz!\n");
    printf("Enter your answer in capital letters.\n\n");

    // Q1
    printf("Q1. What is the capital of France?\nA) Berlin\nB) Madrid\nC) Paris\nD) Rome\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'C') { score = score + 1; } else { wrongAnswers[0] = 1; }

    // Q2
    printf("\nQ2. Which planet is known as the Red Planet?\nA) Venus\nB) Mars\nC) Jupiter\nD) Saturn\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'B') { score = score + 1; } else { wrongAnswers[1] = 1; }

    // Q3
    printf("\nQ3. What is 9 + 10?\nA) 19\nB) 21\nC) 20\nD) 22\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'A') { score = score + 1; } else { wrongAnswers[2] = 1; }

    // Q4
    printf("\nQ4. Who invented the telephone?\nA) Thomas Edison\nB) Alexander Graham Bell\nC) Nikola Tesla\nD) Albert Einstein\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'B') { score = score + 1; } else { wrongAnswers[3] = 1; }

    // Q5
    printf("\nQ5. Water freezes at what temperature (Celsius)?\nA) 0\nB) 32\nC) -10\nD) 100\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'A') { score = score + 1; } else { wrongAnswers[4] = 1; }

    // Q6
    printf("\nQ6. Which element has the chemical symbol 'O'?\nA) Gold\nB) Oxygen\nC) Iron\nD) Silver\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'B') { score = score + 1; } else { wrongAnswers[5] = 1; }

    // Q7
    printf("\nQ7. Which country is famous for pizza and pasta?\nA) Spain\nB) Italy\nC) Mexico\nD) India\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'B') { score = score + 1; } else { wrongAnswers[6] = 1; }

    // Q8
    printf("\nQ8. How many continents are there?\nA) 5\nB) 6\nC) 7\nD) 8\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'C') { score = score + 1; } else { wrongAnswers[7] = 1; }

    // Q9
    printf("\nQ9. Who wrote 'Romeo and Juliet'?\nA) Charles Dickens\nB) Leo Tolstoy\nC) William Shakespeare\nD) Victor Hugo\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'C') { score = score + 1; } else { wrongAnswers[8] = 1; }

    // Q10
    printf("\nQ10. The process by which plants make food is?\nA) Photosynthesis\nB) Evaporation\nC) Condensation\nD) Respiration\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'A') { score = score + 1; } else { wrongAnswers[9] = 1; }

    // Q11
    printf("\nQ11. Which is the largest mammal?\nA) Elephant\nB) Giraffe\nC) Blue Whale\nD) Hippopotamus\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'C') { score = score + 1; } else { wrongAnswers[10] = 1; }

    // Q12
    printf("\nQ12. Which number comes next in the series: 2, 4, 6, ?\nA) 7\nB) 8\nC) 9\nD) 10\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'B') { score = score + 1; } else { wrongAnswers[11] = 1; }

    // Q13
    printf("\nQ13. The sun rises in the?\nA) East\nB) West\nC) North\nD) South\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'A') { score = score + 1; } else { wrongAnswers[12] = 1; }

    // Q14
    printf("\nQ14. What color do you get by mixing red and yellow?\nA) Green\nB) Blue\nC) Orange\nD) Purple\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'C') { score = score + 1; } else { wrongAnswers[13] = 1; }

    // Q15
    printf("\nQ15. In which ocean is the Bermuda Triangle located?\nA) Atlantic\nB) Pacific\nC) Indian\nD) Arctic\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'A') { score = score + 1; } else { wrongAnswers[14] = 1; }

    // Q16
    printf("\nQ16. Who was the first President of the USA?\nA) Abraham Lincoln\nB) Thomas Jefferson\nC) George Washington\nD) John Adams\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'C') { score = score + 1; } else { wrongAnswers[15] = 1; }

    // Q17
    printf("\nQ17. Which gas do we breathe in to survive?\nA) Nitrogen\nB) Carbon Dioxide\nC) Oxygen\nD) Hydrogen\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'C') { score = score + 1; } else { wrongAnswers[16] = 1; }

    // Q18
    printf("\nQ18. Which of these is a programming language?\nA) Snake\nB) Python\nC) Eagle\nD) Lion\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'B') { score = score + 1; } else { wrongAnswers[17] = 1; }

    // Q19
    printf("\nQ19. What is the value of Pi (approx)?\nA) 2.14\nB) 3.14\nC) 4.14\nD) 5.14\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'B') { score = score + 1; } else { wrongAnswers[18] = 1; }

    // Q20
    printf("\nQ20. Which instrument measures temperature?\nA) Barometer\nB) Telescope\nC) Thermometer\nD) Speedometer\nYour answer: ");
    scanf(" %c", &userAns);
    if(userAns == 'C') { score = score + 1; } else { wrongAnswers[19] = 1; }

    printf("\nQuiz Completed!\n");
    printf("Your score: %d/%d\n", score, total);

    if(score < total) {
        printf("You got these wrong:\n");
        if(wrongAnswers[0] == 1)  { printf("Q1. Correct answer: C) Paris\n"); }
        if(wrongAnswers[1] == 1)  { printf("Q2. Correct answer: B) Mars\n"); }
        if(wrongAnswers[2] == 1)  { printf("Q3. Correct answer: A) 19\n"); }
        if(wrongAnswers[3] == 1)  { printf("Q4. Correct answer: B) Alexander Graham Bell\n"); }
        if(wrongAnswers[4] == 1)  { printf("Q5. Correct answer: A) 0\n"); }
        if(wrongAnswers[5] == 1)  { printf("Q6. Correct answer: B) Oxygen\n"); }
        if(wrongAnswers[6] == 1)  { printf("Q7. Correct answer: B) Italy\n"); }
        if(wrongAnswers[7] == 1)  { printf("Q8. Correct answer: C) 7\n"); }
        if(wrongAnswers[8] == 1)  { printf("Q9. Correct answer: C) William Shakespeare\n"); }
        if(wrongAnswers[9] == 1)  { printf("Q10. Correct answer: A) Photosynthesis\n"); }
        if(wrongAnswers[10] == 1) { printf("Q11. Correct answer: C) Blue Whale\n"); }
        if(wrongAnswers[11] == 1) { printf("Q12. Correct answer: B) 8\n"); }
        if(wrongAnswers[12] == 1) { printf("Q13. Correct answer: A) East\n"); }
        if(wrongAnswers[13] == 1) { printf("Q14. Correct answer: C) Orange\n"); }
        if(wrongAnswers[14] == 1) { printf("Q15. Correct answer: A) Atlantic\n"); }
        if(wrongAnswers[15] == 1) { printf("Q16. Correct answer: C) George Washington\n"); }
        if(wrongAnswers[16] == 1) { printf("Q17. Correct answer: C) Oxygen\n"); }
        if(wrongAnswers[17] == 1) { printf("Q18. Correct answer: B) Python\n"); }
        if(wrongAnswers[18] == 1) { printf("Q19. Correct answer: B) 3.14\n"); }
        if(wrongAnswers[19] == 1) { printf("Q20. Correct answer: C) Thermometer\n"); }
    } else {
        printf("Congratulations! You got all answers correct!\n");
    }

    // Repeat
    printf("\nDo you want to play again? (1 for Yes, 0 for No): ");
    scanf("%d", &repeat);
    printf("\n\n");
}
printf("Thank you for playing!\n");
