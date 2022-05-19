# Lazzzy Wordle
> ## Wordle game created using python
> ### Description :<br>
> A CLI based wordle game inspired by [New york times wordle game](https://www.nytimes.com/games/wordle/index.html) This game will help you to improve your thinking skills, enhance vocabulary, and analytical skills.
> When it comes to difficulty level CLI based game is better than UI based game though UI based is more interactive. But in CLI based wordle games will make you compelled to use the pen and paper as you will not be able to see the different colors of alphabets and keyboard keys vanishing which are not present in the word.<br><br>
> In this game you will have to guess a word in six attemps if guessed correctly, you will get the <b>meaning</b>,<b>example</b>,<b>phonetics</b> of that word. If you will not be able to guess the word in the given attemps you will be asked to play again.
> 
> ### Rules:
> 1. You will have to guess the word of length of 5 letters
> 2. The inputted letters should be from english aplhabets i.e. a to z or A to Z. 
> 3. You will have 6 attemtps to guess the word correctly
> 4. If a letter or letters are present in the word to be guessed, then they will be outputted on the CLI.
>     * If a letter is at correct position the position will be outputted
>     * if a letter is not at correct position the position of that letter will not be outputted
>     * if a letter is repeated in the word then their response will be outputted in serial manner form left to right.
>
> ### Libraries used:
> * requests: for calling dictionary API [dictionary API](https://dictionaryapi.dev)
> * regex: for handeling user input
> * urllib: for getting text from [internet](https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt)
> * random: for generating random word
